from enum import Enum

from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models

from watch_demo.core.model_mixin import ChoicesEnumMixin
from watch_demo.core.validators import validate_only_letters


class Gender(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'
    NotShown = 'Not shown'


class AppUser(auth_models.AbstractUser):
    MIN_LENGTH_FIRST_NAME = 3
    MAX_LENGTH_FIRST_NAME = 20
    MIN_LENGTH_LAST_NAME = 3
    MAX_LENGTH_LAST_NAME = 20

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_FIRST_NAME),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_LAST_NAME),
            validate_only_letters,
        )
    )

    email = models.EmailField(
        unique=True,
    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len(),
    )


from django.db import models

# Create your models here.
