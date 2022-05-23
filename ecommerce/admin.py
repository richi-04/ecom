from django.contrib import admin
from .models import register, Product, customer, contact, cart
# Register your models here.
admin.site.register(register)
admin.site.register(Product)
admin.site.register(customer)
admin.site.register(contact)
admin.site.register(cart)