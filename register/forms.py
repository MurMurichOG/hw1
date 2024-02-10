from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=25, required=True)
    password = forms.CharField(max_length=100, required=True)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    birth_date = forms.DateField()
    phone_number = forms.CharField(max_length=20, required=False)
    address = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=100, required=False)
    country = forms.CharField(max_length=100, required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'birth_date', 'phone_number', 'address', 'city', 'country', 'password1', 'password2')
