from datetime import date
from enum import Enum

from django.conf import settings
from django.core import validators
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from watch_demo.core.model_mixin import StrFromFieldsMixin, ChoicesEnumMixin
from watch_demo.core.validators import validate_file_less_than_5mb, validate_only_letters

UserModel = get_user_model()


class Genre(ChoicesEnumMixin, Enum):
    action = 'Action'
    adventure = 'Adventure'
    animation = 'Animation'
    comedy = 'Comedy'
    documentary = 'Documentary'
    drama = 'Drama'
    fantasy = 'Fantasy'
    horror = 'Horror'
    sci_fi = 'Sci-Fi'
    thriller = 'Thriller'
    western = 'Western'


class Actor(StrFromFieldsMixin, models.Model):
    str_fields = ('full_name',)
    MAX_NAME = 30

    first_name = models.CharField(
        max_length=MAX_NAME,
        validators=(
            validate_only_letters,
        ),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_NAME,
        validators=(
            validate_only_letters,
        ),
        null=False,
        blank=False,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Movie(StrFromFieldsMixin, models.Model):
    MAX_NAME = 30
    MAX_DESCRIPTION_LENGTH = 300
    MIN_DESCRIPTION_LENGTH = 20
    CURRENT_YEAR = current_year = date.today().year
    MAX_YEAR = CURRENT_YEAR
    MIN_YEAR = 1930

    name = models.CharField(
        max_length=MAX_NAME,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        choices=Genre.choices(),
        max_length=Genre.max_len(),
        null=False,
        blank=False,
    )

    movie_poster = models.ImageField(
        upload_to='movie_posters/',
        validators=(
            validate_file_less_than_5mb,
        ),
        null=False,
        blank=False,
    )

    year_of_release = models.IntegerField(
        validators=(
            validators.MaxValueValidator(MAX_YEAR),
            validators.MinValueValidator(MIN_YEAR),
        ),
        null=False,
        blank=False,
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    tagged_actors = models.ManyToManyField(
        Actor,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')

        return super().save(*args, **kwargs)




