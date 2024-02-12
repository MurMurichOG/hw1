from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from . import models, forms
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm

class SignUpView(generic.CreateView):
    model = models.Info
    form_class = forms.AccountForm
    template_name = 'verify/register.html'
    context_object_name = 'form'
    success_url = '/signin/'
    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect(self.get_success_url())
        else:
            return redirect('/')
    def get_success_url(self):
        return self.success_url


class SignIn(LoginView):
    form_class = AuthenticationForm
    template_name = 'verify/login.html'
    def get_success_url(self):
        return reverse('accounts_list')


class SignOut(LogoutView):
    next_page = '->'


class AccountList(generic.ListView):
    template_name = 'verify/list.html'
    model = models.Info
    context_object_name = 'account'
    def get_queryset(self):
        return models.Info.objects.all()
