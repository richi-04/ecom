from unicodedata import category
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Product, register, customer, contact, cart
from math import ceil
from django.contrib.auth import authenticate,login
from django.contrib.auth.hashers import make_password
from django.views import View
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.models import User, auth 

# Create your views here.
def home(request):
    p = Product.objects.all()

    return render(request, 'index.html', {'p':p})


def userdata(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        print("🚀 ~ file: views.py ~ line 22 ~ fname", fname)
        lname = request.POST.get('lname')
        print("🚀 ~ file: views.py ~ line 24 ~ lname", lname)
        username = request.POST.get('username')
        print("🚀 ~ file: views.py ~ line 22 ~ username", username)
        email = request.POST.get('email')
        print("🚀 ~ file: views.py ~ line 24 ~ email", email)
        pswd = request.POST.get('pswd')
        print("🚀 ~ file: views.py ~ line 30 ~ pswd", pswd)
        pswd2 = request.POST.get('pswd2')

        
        users = User.objects.create_user(first_name=fname,last_name=lname,username=username, email=email, password=pswd)
        users.save()

        messages.success(request, "Your account has been created...!!!!")
            
        return redirect('login')


    return render(request, 'register.html')

def login_data(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        print("🚀 ~ file: views.py ~ line 48 ~ uname", uname)
        pswd = request.POST.get('pswd')
        print("🚀 ~ file: views.py ~ line 50 ~ pswd", pswd)

        user = authenticate(username=uname, password=pswd)
        print("🚀 ~ file: views.py ~ line 53 ~ user", user)

        if user is not None:
            login(request,user)

            return redirect('home')

        else:
            messages.error, "Incorrect username or password"
            return HttpResponse("enter again the correct detail")

    return render(request, 'login.html') 


def shop(request, data=None):
    products = Product.objects.all().order_by("id")
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if data == None:
        shop = Product.objects.all()
    elif data == 'dresses':
       shop = Product.objects.filter(category='dresses').filter(category=data)
    elif data == 'shirts':
        shop = Product.objects.filter(category=data)
    elif data == 'jeans':
        shop = Product.objects.filter(category='jeans')
    elif data == 'jumpsuits':
        shop = Product.objects.filter(category='jumpsuits')
    elif data == 'blazers':
        shop = Product.objects.filter(category='blazers')
    elif data == 'jacket':
        shop = Product.objects.filter(category='jacket')

        return redirect('shopfilter')

    return render(request, "shop.html", {'page_obj': page_obj, 'shop':shop})


def checkout(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('email')
        address = request.POST.get('address', '') + " " + request.POST.get('address1', '')
        country = request.POST.get('country')
        city = request.POST.get('city')
        state = request.POST.get('state')
        code = request.POST.get('code')

        ship_detail = customer(uname=uname, lname=lname, email=email, phone=phone, address=address, country=country, city=city, state=state, code=code)
        ship_detail.save()

    return render(request, 'checkout.html')

def Contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print("🚀 ~ file: views.py ~ line 89 ~ name", name)
        email = request.POST.get('email')
        print("🚀 ~ file: views.py ~ line 91 ~ email", email)
        subject = request.POST.get('subject')
        print("🚀 ~ file: views.py ~ line 93 ~ subject", subject)
        msg = request.POST.get('msg')
        print("🚀 ~ file: views.py ~ line 95 ~ msg", msg)

        customer_dtl = contact(name=name, email=email, subject=subject, msg=msg)
        print("🚀 ~ file: views.py ~ line 98 ~ customer_dtl", customer_dtl)
        customer_dtl.save()

    return render(request, 'contact.html')

def search(request):
    search_cat = request.GET.get('search')
    if search_cat:
        cat_search = Product.objects.filter(Q(category__icontains=search_cat))
        return render(request, 'search.html', {'cat_search': cat_search})
    return render(request, 'search.html')

def detail(request, id):
    product =  Product.objects.filter(id=id)

    d_p = Product.objects.all()
    context = {
        'product': product,
        'd_p': d_p
    }

    return render(request, 'detail.html', context)

def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        carts = cart.objects.filter(user=user)
        print("🚀 ~ file: views.py ~ line 150 ~ cart1", carts)
        amount = 0.0
        shipping_amt = 80.0
        total_amt = 0.0
        cart_p = [p for p in cart.objects.all() if p.user == user]
        if cart_p:
            for p in cart_p:
                tamt = (p.quantity * p.product.price)
                amount += tamt
                totalamt = amount + shipping_amt
            return render(request, 'cart.html', {'carts':carts, 'totalamt':totalamt, 'amount':amount})
        else:
            return render(request, 'cart.html')

def add_cart(request):
    user = request.user 
    print("🚀 ~ file: views.py ~ line 134 ~ user", user)
    p_id = request.GET.get('p_id')
    p_c = Product.objects.get(id=p_id)
    print("🚀 ~ file: views.py ~ line 135 ~ product", p_c)
    # quantity = request.POST.get('q')
    # print("🚀 ~ file: views.py ~ line 154 ~ quantity", quantity)
    cart1 = cart.objects.create(user=user, product=p_c)
    cart1.save()
    
    return redirect('show_cart')


def shopfilter(request, data=None):
    if data == None:
        shopfilter = Product.objects.all()
    elif data == 'dresses':
       shopfilter = Product.objects.filter(category='dresses').filter(category=data)
    elif data == 'shirts':
        shopfilter = Product.objects.filter(category=data)
    elif data == 'jeans':
        shopfilter = Product.objects.filter(category='jeans')
    elif data == 'jumpsuits':
        shopfilter = Product.objects.filter(category='jumpsuits')
    elif data == 'blazers':
        shopfilter = Product.objects.filter(category='blazers')
    elif data == 'jacket':
        shopfilter = Product.objects.filter(category='jacket')

    return render(request, 'shopfilter.html', {'shopfilter':shopfilter})

def checkout(request):
    return render(request, 'checkout.html')
