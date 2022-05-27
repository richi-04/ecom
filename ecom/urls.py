"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecommerce import views
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name="home"),
    path('register', views.userdata, name="register"),
    path('login', views.login_data, name="login"),
    path('shop', views.shop, name="shop"),
    path('shopfilter/<slug:data>', views.shopfilter, name="shopfilter"),
    path('contact', views.Contact, name="contact"),
    path('search', views.search, name="search"),
    path('detail<int:id>', views.detail, name="detail"),
    path('show_cart', views.show_cart, name="show_cart"),
    path('pluscart', views.pluscart),
    path('minuscart', views.minuscart),
    path('remove', views.remove),
    path('add_cart', views.add_cart, name="add_cart"),
    path('logout',auth_views.LogoutView.as_view(next_page='home'),name="logout"),
    path('checkout', views.checkout_dtl),
    path('checkout', views.check_add),
    path('checkout', views.checkout, name="checkout"),
    path('pview', views.pview, name="pview"),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
