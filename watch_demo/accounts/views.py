from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login
from django.shortcuts import render
from watch_demo.accounts.forms import UserCreateForm
from watch_demo.movies.models import Movie

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'

    def get_success_url(self):
        return reverse_lazy('movie suggestions')


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('movie suggestions')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserDetailsView(LoginRequiredMixin, views.DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movies = self.object.movie_set.all()
        user_movies = ', '.join(str(m.name) for m in movies)
        context['movie_list'] = movies
        context['user_movies'] = user_movies
        context['is_owner'] = self.request.user == self.object
        context['movie_count'] = self.object.movie_set.count()

        return context


class UserEditView(LoginRequiredMixin, views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email', 'gender')

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(LoginRequiredMixin, views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')


class UserMovieListView(LoginRequiredMixin, views.ListView):
    model = Movie
    template_name = 'accounts/movies-user.html'
    # context_object_name = 'movies'
    # default_paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        movies = Movie.objects.filter(user=user.pk)
        context['movies'] = movies
        return context

    # def get_paginate_by(self, queryset):
    #     return self.request.GET.get('page_size', self.default_paginate_by)