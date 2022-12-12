from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView

from watch_demo.common.forms import MovieCommentForm, MovieRateForm, SearchMoviesForm
from watch_demo.common.models import MovieRating
from watch_demo.movies.models import Movie

UserModel = get_user_model()


class IndexListView(ListView):
    template_name = 'common/home-page.html'
    model = UserModel


@login_required
def comment_movie(request, movie_id):
    movie = Movie.objects.filter(id=movie_id).get()
    form = MovieCommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.movie = movie
        comment.user = request.user
        comment.save()

    return redirect(request.META['HTTP_REFERER'])


@login_required
def rate_movie(request, movie_id):
    movie = Movie.objects.filter(id=movie_id).get()
    form = MovieRateForm(request.POST)
    if form.is_valid():
        rating = form.save(commit=False)
        rating.movie = movie
        rating.user = request.user
        rating.save()

    return redirect(request.META['HTTP_REFERER'])
    # MovieRating.objects.create(movie_id=movie_id, user_id=request.user.pk,)


class MoviesSearchListView(LoginRequiredMixin, ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'common/search-movies.html'
    search_form = SearchMoviesForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['pattern'] = self.__get_pattern()
        context['search_form'] = self.search_form
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        pattern = self.__get_pattern()

        if pattern:
            queryset = queryset.filter(movie_genre__icontains=pattern)
            print(queryset)
            # queryset = queryset1 | queryset2
        return queryset

    def __get_pattern(self):
        pattern = self.request.GET.get('pattern', None)
        return pattern.lower() if pattern else None



