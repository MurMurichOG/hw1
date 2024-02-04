from django.urls import path
from .views import MovieListView, search_movies, movie_detail, create_movie, update_movie, delete_movie, create_review

urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie_list'),
    path('search/', search_movies, name='search_movies'),
    path('movies/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('movies/create/', create_movie, name='create_movie'),
    path('movies/<int:movie_id>/update/', update_movie, name='update_movie'),
    path('movies/<int:movie_id>/delete/', delete_movie, name='delete_movie'),
    path('movies/<int:movie_id>/review/create/', create_review, name='create_review'),
]