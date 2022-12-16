from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse_lazy

from tests.utils.utils import create_movie_for_user
from watch_demo.common.models import MovieRating, MovieComment
from watch_demo.common.views import rate_movie
from watch_demo.movies.models import Movie

UserModel = get_user_model()


class MovieDetailsViewTests(TestCase):
    VALID_USER_DATA = {
        'username': 'test_user',
        'email': 'user@test.com',
        'password': 'qwer1234ASDF',
    }

    def create_user_and_login(self, user_data):
        user = UserModel.objects.create_user(**user_data)
        self.client.login(**self.VALID_USER_DATA)
        return user

    def test_movie_details_view__when_no_rating_and_no_comments__expect_0(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)
        movie = create_movie_for_user(user)
        response = self.client.get(reverse_lazy('movie details', kwargs={'slug': movie.slug}))

        self.assertEqual('Not rated yet!', response.context['rating'])
        self.assertEqual(None, response.context['comments'])

    def test_movie_details_view__whit_rating_and_comments__expect_not_empty(self):

        user = self.create_user_and_login(self.VALID_USER_DATA)
        movie = create_movie_for_user(user)
        not_owner_data = {
        'username': 'test_user1',
        'email': 'user1@test.com',
        'password': 'qwer1234ASDF',
        }
        movie_rating = 7.0
        not_owner = UserModel.objects.create_user(**not_owner_data)
        rate_movie = MovieRating(
            movie_id=movie.pk,
            user_id=not_owner.pk,
            rating=movie_rating,
        )
        rate_movie.save()
        movie_comment = 'Great movie!'
        comment_movie = MovieComment(
            movie_id=movie.pk,
            user_id=not_owner.pk,
            text=movie_comment
        )
        comment_movie.save()
        response = self.client.get(reverse_lazy('movie details', kwargs={'slug': movie.slug}))

        self.assertEqual(movie_rating, float(response.context['rating']))
        self.assertEqual(1, len(response.context['comments'].values_list('text')))