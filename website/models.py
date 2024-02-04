from django.db import models

class ParsedData(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название сайта')
    content = models.TextField(verbose_name='Содержимое сайта')