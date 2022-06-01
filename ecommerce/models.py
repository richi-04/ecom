
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


category_opt = [('dresses', 'Dresses'), ('shirts', 'Shirts'), ('jeans', 'Jeans'), ('jumpsuits', 'Jumpsuits'), ('blazers', 'Blazers'), ('jacket', 'Jackets')]
class Product(models.Model):
    objects = None
    p_name = models.CharField(max_length=50)
    category = models.CharField(choices=category_opt, max_length=50)
    desc = models.CharField(max_length=300)
    price = models.FloatField()
    discount_price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to="img", default="")
    stripe_product_id = models.CharField(max_length=100)
    

    def __str__(self):
        return str(self.id)

country_opt = [('india', 'India'), ('us', 'US'), ('afghanistan', 'Afghanistan'), ('albania', 'Albania'), ('algeria', 'Algeria')]

class shipping(models.Model):
    uname = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    country = models.CharField(choices=country_opt, max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    code = models.IntegerField()

    

class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    

    def __str__(self):
        return str(self.product)


class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    msg = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Check_pdtl(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    productquantity = models.ForeignKey(cart, on_delete=models.CASCADE)
    amt = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_amt = models.CharField(max_length=100)
    
class OrderDetail(models.Model):

    id = models.BigAutoField(primary_key=True)
    customer_email= models.EmailField(verbose_name='Customer Email')
    product= models.ForeignKey(to =cart, verbose_name='Product',  on_delete=models.CASCADE, null=True)
    amount = models.IntegerField(verbose_name='Amount')
    stripe_payment_intent= models.CharField(max_length=200)
    has_paid = models.BooleanField(default=False, verbose_name='Payment Status')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)