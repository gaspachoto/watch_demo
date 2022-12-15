from django.db import models

from django.contrib.auth import get_user_model
from django.db import models

from watch_demo.movies.models import Movie

UserModel = get_user_model()


class MovieComment(models.Model):
    MAX_TEXT_LENGTH = 300

    text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True,
    )

    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class MovieRating(models.Model):
    CHOICES = [(i, i) for i in range(1, 11)]

    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    rating = models.IntegerField(
        choices=CHOICES,
        null=False,
        blank=False,
    )