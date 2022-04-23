''' products  = product.objects.all()
    print(products)
    n = len(products)
    nslide = n // 4 + ceil ((n/4)- (n//4))
    #params = {'no_sileds': nslide,'range':range(1,nslide),'product':products}
    allProds=[[products, range(1, len(products)), nslide],[products, range(1, len(products)), nslide]]
    params={'allProds':allProds }'''
    