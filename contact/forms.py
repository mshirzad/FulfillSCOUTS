from django import forms
from django.forms.widgets import TextInput, PasswordInput, Textarea

class ContactUsForm(forms.Form):
    f_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'django-form', 'placeholder': 'Full Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'django-form','placeholder': 'Email Address'}))
    skype_id = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'django-form', 'placeholder': 'Skype ID'}))
    orders = forms.CharField(required=True, widget=forms.NumberInput(attrs={'class':'django-form', 'placeholder': 'Orders per Day'}))
    countries = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'django-form', 'placeholder': 'Countries Ship to'}))
    product = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'django-form', 'placeholder': 'Alibaba/AliExpress Product Link'}))
    message = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'django-form', 'placeholder': 'Additional Message'}))
