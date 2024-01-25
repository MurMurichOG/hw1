from django.urls import path, include
from .views import movies_list, movies_detail

urlpatterns = [
    path('movies/', movies_list),
    path('movies/<int:id>', movies_detail)
]