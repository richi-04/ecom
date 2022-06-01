from django.contrib import admin
from .models import Product, contact, cart, shipping, Check_pdtl
# Register your models here.
admin.site.register(Product)
admin.site.register(shipping)
admin.site.register(contact)
admin.site.register(cart)
admin.site.register(Check_pdtl)