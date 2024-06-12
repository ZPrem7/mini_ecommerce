from django import forms
from django.contrib.auth.models import User
from .models import Product
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['categories','title', 'description', 'price', 'stock_quantity', 'image', 'tags']        


class UserUpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            return password
        return self.instance.password 