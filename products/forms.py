from django import forms
from django.contrib.auth.models import User

from .models import Product, NewsLetter, ContactUs


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'url', 'category', 'description', 'product_logo']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class NewsLetterForm(forms.ModelForm):

    class Meta:
        model = NewsLetter
        fields = ['email']


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'phoneNumber', 'company','message']


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='first_name',)
    last_name = forms.CharField(max_length=30, label='last_name')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
