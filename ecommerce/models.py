
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
userchoices = [('buyer', 'Buyer'),('seller', 'Seller')] 
class register(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    pswd = models.CharField(max_length=100)
    user = models.CharField(choices=userchoices, max_length=100)
    

    def __str__(self):
        return self.username

category_opt = [('dresses', 'Dresses'), ('shirts', 'Shirts'), ('jeans', 'Jeans'), ('jumpsuits', 'Jumpsuits'), ('blazers', 'Blazers'), ('jacket', 'Jackets')]
class Product(models.Model):
    objects = None
    p_name = models.CharField(max_length=50)
    category = models.CharField(choices=category_opt, max_length=50)
    desc = models.CharField(max_length=300)
    price = models.FloatField()
    discount_price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to="img", default="")

    def __str__(self):
        return str(self.id)

country_opt = [('india', 'India'), ('us', 'US'), ('afghanistan', 'Afghanistan'), ('albania', 'Albania'), ('algeria', 'Algeria')]
class customer(models.Model):
    uname = models.ForeignKey(User, on_delete=models.CASCADE)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    country = models.CharField(choices=country_opt, max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    code = models.IntegerField()

    def __str__(self):
        return str(self.id)

class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.user)


class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    msg = models.CharField(max_length=200)

    def __str__(self):
        return self.name