from django.urls import path
from .views import movies_list, movies_detail, MovieListView, search_movies

urlpatterns = [
    path('movies/', movies_list),
    path('movies/<int:id>', movies_detail),
    path('movies/', MovieListView.as_view(), name='movie_list'),
    path('search/', search_movies, name='search_movies')
]