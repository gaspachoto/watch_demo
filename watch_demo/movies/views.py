from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy

from django.shortcuts import render

from watch_demo.common.forms import MovieCommentForm, MovieRateForm
from watch_demo.common.models import MovieComment, MovieRating
from watch_demo.movies.forms import MovieAddForm, MovieEditForm, ActorAddForm
from watch_demo.movies.models import Movie
from watch_demo.movies.utils import calculate_rating

UserModel = get_user_model()


class MovieAddView(LoginRequiredMixin, CreateView):
    model = Movie
    template_name = 'movies/add-movie.html'
    form_class = MovieAddForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context['form'])
        return context


class MovieListView(LoginRequiredMixin, ListView):
    model = Movie
    template_name = 'movies/movie-suggestions.html'
    context_object_name = 'movies'
    default_paginate_by = 4

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # actors = ', '.join(str(full_name) for full_name in Movie.tagged_actors.all())
    #     # context[actors] = actors
    #     return context

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.default_paginate_by)


class MovieDetailView(LoginRequiredMixin, DetailView):
    template_name = 'movies/details-movie.html'
    model = Movie
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = self.object
        movie_rating = calculate_rating(movie)
        print(movie_rating)
        movie_rated = MovieRating.objects.filter(movie_id=movie.pk, user_id=self.request.user.pk)
        context['user_rated_movie'] = movie_rated
        context['rating'] = movie_rating
        context['comments'] = self.object.moviecomment_set.all() or None
        context['comment_form'] = MovieCommentForm
        context['rate_form'] = MovieRateForm
        context['is_owner'] = self.request.user.pk == self.object.user_id
        return context


class MovieEditView(LoginRequiredMixin, UpdateView):
    template_name = 'movies/edit-movie.html'
    model = Movie
    context_object_name = 'movie'
    fields = ('name', 'genre', 'movie_poster', 'year_of_release', 'description')

    def get_success_url(self):
        return reverse_lazy('movie details', kwargs={
            'slug': self.object.slug,
        })


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = 'movies/delete-movie.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        MovieComment.objects.filter(movie_id=self.object.id).delete()
        MovieRating.objects.filter(movie_id=self.object.id).delete()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class ActorAddView(LoginRequiredMixin, CreateView):
    model = Movie
    template_name = 'movies/add-actor.html'
    form_class = ActorAddForm
    success_url = reverse_lazy('index')