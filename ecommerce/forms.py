from django import forms 
from .models import Product, register, customer, contact
from django.contrib.auth.models import User 

class userform(forms.ModelForm):
    userchoices = [('buyer', 'Buyer'),('seller', 'Seller')] 
    user = forms.ChoiceField(choices=userchoices, widget=forms.RadioSelect())
    number = forms.CharField(max_length=50)
    class meta:
        model = register
        fields = ('username', 'email', 'password','user')