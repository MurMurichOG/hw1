from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название книги')
    description = models.TextField(verbose_name='Описание книги')
    image = models.ImageField(upload_to='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title