from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse_lazy

from tests.utils import create_movie_for_user
from watch_demo.movies.models import Movie

UserModel = get_user_model()


class MovieAddViewTests(TestCase):

    VALID_USER_DATA = {
        'username': 'test_user',
        'email': 'user@test.com',
        'password': 'qwer1234ASDF',
    }

    def create_user_and_login(self, user_data):
        user = UserModel.objects.create_user(**user_data)
        self.client.login(**self.VALID_USER_DATA)
        return user

    def test_add_movie_view__when_data_is_correct__expect_movie_created(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)
        movie = create_movie_for_user(user)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))
        self.assertEqual(1, response.context['movie_count'])
        self.assertEqual(1, len(response.context['movie_list']))

    def test_add_movie_view__when_year_is_incorrect__expect_exception(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)
        movie = Movie(
            name=f'Test_movie',
            genre=f'Horror',
            movie_poster=f'C://movies.com.jpg',
            year_of_release='2030',
            description='descriptiondescriptiondescription',
            user=user
        )
        movie.save()
        with self.assertRaises(ValidationError) as context:
            user.full_clean()
            user.save()
        self.assertIsNotNone(context.exception)

    def test_add_movie_view__when_no_poster__expect_exception(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)
        movie = Movie(
            name=f'Test_movie',
            genre=f'Horror',
            year_of_release='2030',
            description='descriptiondescriptiondescription',
            user=user
        )
        movie.save()
        with self.assertRaises(ValidationError) as context:
            user.full_clean()
            user.save()
        self.assertIsNotNone(context.exception)