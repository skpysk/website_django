from django.shortcuts import render

from django.http import HttpResponse 
from .models import blogpost
import math
# Create your views here.

def index(request):
    myposts = blogpost.objects.all()
    print(myposts)
    return render(request,"blog/index.html",{'myposts': myposts})

def blogposts(request, id):
    post = blogpost.objects.filter(post_id = id)[0]
    return render(request, 'blog/blogpost.html',{'post':post})

def nextprev(request):
    posts = blogpost.query.filter_by().all()
    post = blogpost.objects.filter(post_id = id)
    last = math.ceil(len(posts)/int(len(post)))
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page-1)*int(len(post)):(page-1)*int(len(post))+ int(len(post))]
    if page==1:
        prev = "#"
        next = "/?page="+ str(page+1)
    elif page==last:
        prev = "/?page="+ str(page-1)
        next = "#"
    else:
        prev = "/?page="+ str(page-1)
        next = "/?page="+ str(page+1)
    
    return render(request,'index.html', {'posts':posts, 'prev':prev, 'next':next})
