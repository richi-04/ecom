from unicodedata import category
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Product, register, customer, contact
from math import ceil
from django.contrib.auth import authenticate,login
from django.contrib.auth.hashers import make_password
from django.views import View
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, 'index.html')


def userdata(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        number = request.POST.get('number')
        pswd = request.POST.get('pswd')
        print("🚀 ~ file: views.py ~ line 30 ~ pswd", pswd)
        pswd2 = request.POST.get('pswd2')

        if len(number)<10 or (pswd!=pswd2):
            messages.error, "Please fill the form correctly"
            return HttpResponse("fill the form again")
          
        else:
            users = register(username=username, email=email, number=number, pswd=make_password(pswd))
            users.save()


    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        print("🚀 ~ file: views.py ~ line 48 ~ uname", uname)
        pswd = request.POST.get('pswd')
        print("🚀 ~ file: views.py ~ line 50 ~ pswd", pswd)

        user = authenticate(username=uname, pswd=pswd)
        print("🚀 ~ file: views.py ~ line 53 ~ user", user)

        if user is not None:
            login(request,user)

            return redirect('home')
        else:
            messages.error, "Incorrect username or password"
            return HttpResponse("enter again the correct detail")

    return render(request, 'login.html') 


def shop(request):
    products = Product.objects.all().order_by("id")
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    

    return render(request, "shop.html", {'page_obj': page_obj})


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

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        msg = request.POST.get('msg')

        customer_dtl = contact(name=name, email=email, subject=subject, msg=msg)
        customer_dtl.save()

    return render(request, 'contact.html')

def search(request):
    search_cat = request.GET.get('search')
    if search_cat:
        cat_search = Product.objects.filter(Q(category__icontains=search_cat))
        return render(request, 'search.html', {'cat_search': cat_search})
    return render(request, 'search.html')

def detail(request):
    return render(request, 'detail.html')

def checkout(request):
    return render(request, 'checkout.html')

def cart(request):
    return render(request, 'cart.html')