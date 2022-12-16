from django.test import TestCase
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from tests.utils.utils import create_movie_for_user
from watch_demo.common.models import MovieRating

UserModel = get_user_model()


class TestRatingCalculator(TestCase):
    VALID_USER_DATA = {
        'username': 'test_user',
        'email': 'user@test.com',
        'password': 'qwer1234ASDF',
    }

    def create_user_and_login(self, user_data):
        user = UserModel.objects.create_user(**user_data)
        self.client.login(**self.VALID_USER_DATA)
        return user

    def test_calculate_rating__when_more_than_one_users_rate__expect_average(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)
        movie = create_movie_for_user(user)

        first_user_data = {
        'username': 'test_user1',
        'email': 'user1@test.com',
        'password': 'qwer1234ASDF',
        }
        first_user = UserModel.objects.create_user(**first_user_data)

        second_user_data = {
            'username': 'test_user2',
            'email': 'user2@test.com',
            'password': 'qwer1234ASDF',
        }
        second_user = UserModel.objects.create_user(**second_user_data)

        rate_movie1 = MovieRating(
            movie_id=movie.pk,
            user_id=first_user.pk,
            rating=8.0,
        )
        rate_movie1.save()

        rate_movie2 = MovieRating(
            movie_id=movie.pk,
            user_id=second_user.pk,
            rating=5.0,
        )
        rate_movie2.save()

        expected_result = (8.0 + 5.0) / 2

        response = self.client.get(reverse_lazy('movie details', kwargs={'slug': movie.slug}))

        self.assertEqual(expected_result, float(response.context['rating']))

