from django.shortcuts import render
from . models import Product,Orders, OrderUpdate,Pay
from math import ceil
# Create your views here.
def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'resale/index.html', params)
    
def about(request):
    return render(request, 'resale/about.html')

def wishlist(request):
    return render(request, 'resale/wishlist.html')

def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query)<4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'resale/search.html', params)

def productView(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'resale/prodView.html', {'product':product[0]})



def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        
        return render(request, 'resale/payment.html', {'thank':thank, 'id': id})
    return render(request, 'resale/checkout.html')

def succes(request):
    return render(request, 'resale/succes.html')
def payment(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        card = request.POST.get('card', '')
        expiry = request.POST.get('expiry', '')
        cvv = request.POST.get('cvv', '')
        
        payy = Pay(name=name,card=card,expiry=expiry, cvv=cvv)
        payy.save()
        return render(request, 'resale/succes.html')
    return render(request, 'resale/payment.html')

def form(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        price = request.POST.get('price', '')
        phone = request.POST.get('phone', '')
        desc  = request.POST.get('desc','')
        category = request.POST.get('dropdown','')
        image = request.POST.get('img','')
        product_name = request.POST.get('prodName','')
        size = request.POST.get('size','')
        address=request.POST.get('address','')
        prod = Product(user_name=name, product_name=product_name, phone=phone, price=price, desc=desc, category=category, image=image, size=size,address=address)
        prod.save()
    
    return render(request, 'resale/form.html')