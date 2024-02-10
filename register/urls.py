from django.urls import path
from .views import register, user_list

urlpatterns = [
    path('register/', register, name='register'),
    path('user-list/', user_list, name='user_list'),
]

