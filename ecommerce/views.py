
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.contrib import messages
from .models import Product, register, contact, cart, shipping
from math import ceil
from django.contrib.auth import authenticate,login
from django.contrib.auth.hashers import make_password
from django.views import View
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.models import User 
# from django import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import stripe

# Create your views here.
#----------------------------home page------------------------------------

def home(request):
    p = Product.objects.all()

    return render(request, 'index.html', {'p':p})

# ----------------------------------registration---------------------------------
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
# ------------------------login-----------------------------
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

# ---------------------displaying all product------------------------
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

# ----------------------------customer query message.-----------------
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

# -----------------------cart------------------------
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


def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        carts = cart.objects.filter(user=user)
        print("🚀 ~ file: views.py ~ line 150 ~ cart1", carts)
        amount = 0.0
        shipping_amt = 80.0
        totalamt = 0.0
        cart_p = [p for p in cart.objects.all() if p.user == user]
        if cart_p:
            for p in cart_p:
                tamt = (p.quantity * p.product.price)
                amount += tamt
                totalamt = amount + shipping_amt
            return render(request, 'cart.html', {'carts':carts, 'totalamt':totalamt, 'amount':amount})
        
    return render(request, 'cart.html')

def pluscart(request):
    if request.method == 'GET':
        pro_id = request.GET['pro_id']
        print("🚀 ~ file: views.py ~ line 168 ~ pro_id", pro_id)
        c = cart.objects.get(Q(product=pro_id) & Q(user=request.user))
        print("🚀 ~ file: views.py ~ line 170 ~ c", c)
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amt = 80.0
        cart_p = [p for p in cart.objects.all() if p.user == request.user]
        for p in cart_p:
            tamt = (p.quantity * p.product.price)
            amount += tamt
            totalamt = amount + shipping_amt

        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamt': totalamt
        } 

    return JsonResponse(data)          


def minuscart(request):
    if request.method == 'GET':
        pro_id = request.GET['pro_id']
        c = cart.objects.get(Q(product=pro_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amt = 80.0
        cart_p = [p for p in cart.objects.all() if p.user == request.user]
        for p in cart_p:
            tamt = (p.quantity * p.product.price)
            amount += tamt
            totalamt = amount + shipping_amt

        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamt': totalamt
        } 

    return JsonResponse(data)  

def remove(request):
    if request.method == 'GET':
        pro_id = request.GET['pro_id']
        c = cart.objects.get(Q(product=pro_id) & Q(user=request.user))
        c.delete()
        print("🚀 ~ file: views.py ~ line 217 ~ c1", c)
        amount = 0.0
        shipping_amt = 80.0
        cart_p = [p for p in cart.objects.all() if p.user == request.user]
        for p in cart_p:
            tamt = (p.quantity * p.product.price)
            amount += tamt 
        data = {
            'amount':amount,
            'totalamt': amount + shipping_amt
        } 

    return JsonResponse(data)  

# ----------------shop category wise diaplay-----------------------
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

# --------------checkout---------------------
def checkout(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address', '') + " " + request.POST.get('address1', '')
        country = request.POST.get('country')
        city = request.POST.get('city')
        state = request.POST.get('state')
        code = request.POST.get('code')

        ship_detail = shipping(email=email, phone=phone, address=address, country=country, city=city, state=state, code=code)
        ship_detail.save()

    return render(request, 'checkout.html')


def checkout(request):
    if request.user.is_authenticated:
        user = request.user
        check_c = cart.objects.filter(user=user)
        print("🚀 ~ file: views.py ~ line 150 ~ cart1", check_c)
        amount = 0.0
        shipping_amt = 80.0
        totalamt = 0.0
        cart_c = [p for p in cart.objects.all() if p.user == user]
        if cart_c:
            for p in cart_c:
                tamt = (p.quantity * p.product.price)
                amount += tamt
                totalamt = amount + shipping_amt
        return render(request, 'checkout.html', {'check_c':check_c, 'totalamt':totalamt, 'amount':amount})
        
    return render(request, 'checkout.html')

#--------------------checkout product view ----------------------

def pview(request):
    user = request.user 
    p_id = request.GET.get('p_id')
    p_c = Product.objects.get(id=p_id)
    cart1 = cart.objects.create(user=user, product=p_c)
    cart1.save()
    return render(request, 'payment/productview.html')





# ------------------payment--------------------

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=domain_url + 'cancelled/',
            payment_method_types=['card'],
            mode='payment',
            checkout = cart.objects.filter(id),
            line_items=[
                {
                    'name': 'T-shirt',
                    'quantity': '1',
                    'currency': 'INR',
                    'amount': '500',
                }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})







# # payment
# razorpay_client = razorpay.Client(
#     auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))