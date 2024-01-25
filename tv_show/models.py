from django.db import models

class Movie(models.Model):
    GENRE = (
        ('Боевик', 'Боевик'),
        ('Комедия', 'Комедия'),
        ('Романтика', 'Романтика'),
        ('Триллеры', 'Триллеры')
    )
    title = models.CharField(max_length=100, verbose_name='Название фильма')
    description = models.TextField(max_length=300, verbose_name='Опасние')
    image = models.ImageField(verbose_name='Изображение', upload_to='')
    actor = models.CharField(max_length=100, verbose_name='Актеры')
    director = models.CharField(max_length=100, verbose_name='Режиссер')
    trailer_url = models.URLField(verbose_name='Ссылка на трейлер')
    genre = models.CharField(choices=GENRE, max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title