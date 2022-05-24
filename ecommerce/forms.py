from django import forms 
from .models import Product, register, customer, contact
from django.contrib.auth.models import User 

class userform(forms.ModelForm):
    userchoices = [('buyer', 'Buyer'),('seller', 'Seller')] 
    opt_user = forms.ChoiceField(choices=userchoices, widget=forms.RadioSelect(attrs={'class':'form-control'}))
    class meta:
        model = User
        fields = ('opt_user')