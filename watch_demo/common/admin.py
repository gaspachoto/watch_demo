from django.contrib import admin

from watch_demo.common.models import MovieComment, MovieRating
from watch_demo.movies.models import Movie


@admin.register(MovieComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('movie_id', 'user')


@admin.register(MovieRating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('movie_id', 'user')