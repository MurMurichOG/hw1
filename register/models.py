from django.db import models
from django.contrib.auth.models import User

class Info(User):
    username = models.CharField(max_length=25, verbose_name='Ваш никнейм')
    password = models.CharField(max_length=100, verbose_name='Ваш пароль')
    email = models.EmailField(null=True, verbose_name="Ваш email")
    first_name = models.CharField(max_length=20, verbose_name="Ваше имя")
    last_name = models.CharField(max_length=50, verbose_name="Ваша фамилия")
    birth_date = models.DateField(null=True, verbose_name='Ваша дата рождения')
    phone_number = models.CharField(max_length=20, verbose_name="Ваш номер телефона")
    address = models.CharField(max_length=255, verbose_name="Ваш адрес")
    city = models.CharField(max_length=100, verbose_name="Ваш город проживания")
    country = models.CharField(max_length=100, verbose_name="Ваша страна проживания")


