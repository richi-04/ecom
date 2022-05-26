from django.contrib import admin
from .models import register, Product, contact, cart, shipping
# Register your models here.
admin.site.register(register)
admin.site.register(Product)
admin.site.register(shipping)
admin.site.register(contact)
admin.site.register(cart)