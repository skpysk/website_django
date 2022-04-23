from turtle import update
from django.shortcuts import render
from .models import product , contact , orders , orderupdate
from math import ceil
import json
import paytmchecksum

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import HttpResponse
from paytm import Checksum
MERCHANT_KEY = 'C%KsNOjphEKP7s_x'



def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shop/css.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contacts(request):
    cont = False
    if request.method =="POST":
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        dsc=request.POST.get('dsc', '')
        contac = contact(name=name,email=email,phone=phone,dsc=dsc)
        contac.save()
        cont = True
        return render(request, "shop/contact.html",{'cont':cont})
    return render(request, "shop/contact.html")
    
def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        print(email,orderId)
        try:
            order = orders.objects.filter(order_id=orderId, email=email)
            print(order)
            if len(order)>0:
                update = orderupdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates,order[0].items_json],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')
def searchmatch(query, item):
    if query in item.product_name.lower() or query in item.category:
        print(query)
        print(item.product_name.lower())
        return True
    else:
        return False
def search(request):
    query = request.GET.get('search')
    print(query)
    allProds = []
    catprods = product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchmatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod)!= 0:
         allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds , 'msg':""}
    if len(allProds) == 0 or len(query)<4 :
        params = {"msg":"Please make sure to enter relevant search query"}

    return render(request, 'shop/search.html', params)
   

def productView(request, myid):
    prod = product.objects.filter(id=myid)
    return render(request, 'shop/prodview.html',{'product':prod[0]})

def checkout(request):
    if request.method =="POST":
        print(request)
        items_json=request.POST.get('itemsjson', '')
        name=request.POST.get('name', '')
        amount=request.POST.get('amount', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')
        order = orders(items_json=items_json,name=name,amount=amount,email=email,address = address, city = city,state=state,zip_code=zip_code,phone=phone)
        order.save()
        thank = True
        update = orderupdate(order_id = order.order_id, update_desc = "order has been placed" )
        update.save()
        id = order.order_id
        #return render(request, 'shop/chekout.html',{"thank":thank, 'id':id})
        # paytm ko ko bolna pdega user se amount lekr meri account me de
        
        params ={

            'MID': 'nmCuHC98839638287047',
            'ORDER_ID': order.order_id,
            'TXN_AMOUNT': 1,
            'CUST_ID': 'email',
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/shop/requesthandler/',
            }
        params['CHECKSUMHASH'] = Checksum.generate_checksum(params, MERCHANT_KEY)

        

        return  render(request, 'shop/paytm.html', {'params': params})

    return render(request, 'shop/chekout.html')

@csrf_exempt

def requesthandler(request):
    # pathm bhejega status to uske leyai web me allow krna pdega csrf allow ne krta but ham log allow kraw dengi decorator functionality
    # ko change ker deta hai
    return HttpResponse('done')