from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

class AccountForm(UserCreationForm):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
    email = forms.EmailField(required=False)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    birth_date = forms.DateField(required=False)
    phone_number = forms.CharField(required=False)
    address = forms.CharField(required=False)
    city = forms.CharField(required=False)
    country = forms.CharField(required=False)

    class Meta:
        model = models.Info
        fields = ('username', 'email', 'first_name', 'last_name', 'birth_date', 'phone_number', 'address', 'city', 'country')

    def save_data(self, commit=True):
        user = super(AccountForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.password = self.cleaned_data['password']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.birth_date = self.cleaned_data['birth_date']
        user.phone_number = self.cleaned_data['phone_number']
        user.address = self.cleaned_data['address']
        user.city = self.cleaned_data['city']
        user.country = self.cleaned_data['country']

        if commit:
            user.save()
            return user