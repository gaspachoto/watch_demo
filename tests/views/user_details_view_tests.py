from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from tests.utils.utils import create_movies_for_user
from watch_demo.movies.models import Movie

UserModel = get_user_model()


class UserDetailsViewTests(TestCase):
    VALID_USER_DATA = {
        'username': 'test_user',
        'email': 'user@test.com',
        'password': 'qwer1234ASDF',
    }

    def create_user_and_login(self, user_data):
        user = UserModel.objects.create_user(**user_data)
        self.client.login(**self.VALID_USER_DATA)
        return user

    def test_user_details__when_owner__expect_is_owner_true(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))
        self.assertTrue(response.context['is_owner'])

    def test_user_details__when_not_owner__expect_is_owner_false(self):
        profile_user = self.create_user_and_login({
            'username': self.VALID_USER_DATA['username'] + '1',
            'email': self.VALID_USER_DATA['email'] + '1',
            'password': self.VALID_USER_DATA['password'],
        })

        self.create_user_and_login(self.VALID_USER_DATA)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': profile_user.pk}))

        self.assertFalse(response.context['is_owner'])

    def test_user_details__when_movies_expect_count_of_suggestions(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)
        create_movies_for_user(user)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(5, response.context['movie_count'])
        self.assertEqual(5, len(response.context['movie_list']))

    def test_user_details__when_no_movies_expect_0_suggestions(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(0, response.context['movie_count'])
        self.assertEqual([], list(response.context['user_movies']))