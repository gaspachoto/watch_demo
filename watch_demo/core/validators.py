from datetime import date

from django.core import exceptions
from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Only letters are allowed')


def validate_file_less_than_5mb(fileobj):
    filesize = fileobj.file.size
    megabyte_limit = 5.0
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError(f'Max file size is {megabyte_limit}MB')


def validate_year(value):
    current_year = current_year = date.today().year
    min_year = 1930
    if value < min_year or value > current_year:
        raise exceptions.ValidationError(f'Year must be between {min_year} and {current_year}')