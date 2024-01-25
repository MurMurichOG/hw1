from django.shortcuts import render, get_object_or_404
from .models import Movie

def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movies.html',{'movies': movies})

def movies_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'movies/movies_detail.html', {'movie': movie})
