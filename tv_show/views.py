from django.shortcuts import get_object_or_404
from .models import Movie, Review
from .forms import ReviewForm, Movie
from django.views import generic


class MovieListView(generic.ListView):
    template_name = 'movies/movies.html'
    model = Movie
    context_object_name = 'movies'
    extra_context = {'form': Review.objects.all()}

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        movie_comments_count = {}

        for movie in context['movies']:
            comments_count = movie.reviews.count()
            movie_comments_count[movie] = comments_count

        context['movie_comments_count'] = movie_comments_count
        return context


class MovieDetailMovie(generic.DetailView):
    model = Movie
    template_name = 'movies/movies_detail.html'
    extra_context = {'form': Review.objects.all()}

    def get_object(self, **kwargs):
        movie = self.kwargs.get('id')
        return get_object_or_404(Movie, id=movie)


class RewiewCreateView(generic.CreateView):
    template_name = 'movies/crud/comments.html'
    form_class = ReviewForm
    context_object_name = 'form'
    success_url = '/'
    queryset = Movie.objects.all()

    def form_valid(self, form):
        return super(RewiewCreateView, self).form_valid(form=form)


class MovieDeleteView(generic.DeleteView):
    template_name = 'movies/crud/confirm_delete.html'
    success_url = '/'
    queryset = Movie.objects.all()

    def get_object(self, **kwargs):
        movie = self.kwargs.get('id')
        return get_object_or_404(Movie, id=movie)


class MovieUpdateView(generic.UpdateView):
    template_name = 'movies/crud/update.html'
    form_class = Movie
    model = Movie
    context_object_name = 'form'
    extra_context = {'movie': Movie.objects.all()}
    queryset = Movie.objects.all()
    success_url = '/'

    def get_object(self, **kwargs):
        movie = self.kwargs.get('id')
        return get_object_or_404(Movie, id=movie)

    def form_valid(self, form):
        return super(MovieUpdateView, self).form_valid(form=form)


class MovieCreateView(generic.CreateView):
    template_name = 'movies/crud/create.html'
    success_url = '/'
    model = Movie
    form_class = Movie
    queryset = Movie.objects.all()
    context_object_name = 'form'
    extra_context = {'movie': model.objects.all()}

    def form_valid(self, form):
        return super(MovieCreateView, self).form_valid(form=form)


class SearchView(generic.ListView):
    model = Movie
    template_name = 'movies/movies.html'
    paginate_by = 5
    def get_queryset(self):
        query = self.request.GET.get('q', '')
        print(f"Query: {query}")
        return Movie.objects.filter(title__icontains=query)

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            self.context_object_name = 'movies'
            return Movie.objects.filter(title__icontains=query)
        else:
            return Movie.objects.all()