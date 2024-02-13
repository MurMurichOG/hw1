from django.db import models

class Tags(models.Model):
    name = models.CharField(max_length=50, verbose_name='Теги категорий', default='#')

    def __str__(self):
        return self.name


class Clothes(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(max_length=250, blank=True, verbose_name='Описание')
    tags = models.ManyToManyField(Tags, verbose_name='Категория')

    def __str__(self):
        return self.title