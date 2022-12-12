from django.urls import path

from watch_demo.common.views import IndexListView, comment_movie, rate_movie, MoviesSearchListView
from watch_demo.movies.views import MovieListView

urlpatterns = (
    path('', IndexListView.as_view(), name='index'),
    path('create-comment/<int:movie_id>/', comment_movie, name='comment movie'),
    path('rate-movie/<int:movie_id>/', rate_movie, name='rate movie'),
    path('search-movies/', MoviesSearchListView.as_view(), name='search movies')
)