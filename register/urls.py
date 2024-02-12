from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='register'),
    path('signin/', views.SignIn.as_view(), name='login'),
    path('signout/', views.SignOut.as_view(), name='logout'),
    path('accounts_list/', views.AccountList.as_view(), name='accounts_list')
]

