from django.db import models

class Movie(models.Model):
    GENRE = (
        ('Боевик', 'Боевик'),
        ('Комедия', 'Комедия'),
        ('Романтика', 'Романтика'),
        ('Триллеры', 'Триллеры')
    )
    title = models.CharField(max_length=100, verbose_name='Название фильма')
    description = models.TextField(max_length=300, verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение', upload_to='')
    actor = models.CharField(max_length=100, verbose_name='Актеры')
    director = models.CharField(max_length=100, verbose_name='Режиссер')
    trailer_url = models.URLField(verbose_name='Ссылка на трейлер')
    genre = models.CharField(choices=GENRE, max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

class TVShow(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название шоу')
    description = models.TextField(max_length=300, verbose_name='Описание')
    release_date = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(max_length=2)

class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    tv_show = models.ForeignKey(TVShow, on_delete=models.CASCADE, related_name='reviews')
    def __str__(self):
        return self.title