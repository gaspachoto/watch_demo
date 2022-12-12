from django.urls import path, include

from watch_demo.movies.views import MovieListView, MovieDetailView, MovieEditView, MovieDeleteView, MovieAddView, \
    ActorAddView

urlpatterns = (
    path('suggest/', MovieAddView.as_view(), name='movie add'),
    path('add-actor', ActorAddView.as_view(), name='actor add'),
    path('all-movies/', MovieListView.as_view(), name='movie suggestions'),
    path('/<slug:slug>/', include([
        path('movie-details/', MovieDetailView.as_view(), name='movie details'),
        path('movie-edit/', MovieEditView.as_view(), name='movie edit'),
        path('movie-delete/', MovieDeleteView.as_view(), name='movie delete'),
    ]))
)
