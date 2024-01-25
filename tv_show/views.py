from django.shortcuts import render, get_object_or_404
from .models import Movie
from .models import TVShow
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TVShowForm, ReviewForm

def tv_show_detail(request, pk):
    tv_show = get_object_or_404(TVShow, pk=pk)
    reviews = tv_show.reviews.all()
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.tv_show = tv_show
            review.save()
            return HttpResponseRedirect(reverse('tv_show_detail', args=[pk]))
    else:
        review_form = ReviewForm()

    return render(request, 'tv_show_detail.html', {'tv_show': tv_show, 'reviews': reviews, 'review_form': review_form})

def tv_show_list(request):
    tv_shows = TVShow.objects.all()
    return render(request, 'tv_show_list.html', {'tv_shows': tv_shows})

def tv_show_detail(request, pk):
    tv_show = get_object_or_404(TVShow, pk=pk)
    return render(request, 'tv_show_detail.html', {'tv_show': tv_show})

def tv_show_create(request):
    if request.method == 'POST':
        form = TVShowForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tv_show_list'))
    else:
        form = TVShowForm()

    return render(request, 'tv_show_form.html', {'form': form})

def tv_show_update(request, pk):
    tv_show = get_object_or_404(TVShow, pk=pk)

    if request.method == 'POST':
        form = TVShowForm(request.POST, instance=tv_show)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tv_show_list'))
    else:
        form = TVShowForm(instance=tv_show)

    return render(request, 'tv_show_form.html', {'form': form})

def tv_show_delete(request, pk):
    tv_show = get_object_or_404(TVShow, pk=pk)
    tv_show.delete()
    return HttpResponseRedirect(reverse('tv_show_list'))

def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movies.html',{'movies': movies})

def movies_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'movies/movies_detail.html', {'movie': movie})
