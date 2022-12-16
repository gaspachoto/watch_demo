from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, reverse_lazy

UserModel = get_user_model()


class SignUpViewTests(TestCase):
    VALID_USER_DATA = {
        'username': 'test_user',
        'email': 'user@test.com',
        'password': 'qwer1234ASDF',
    }

    def create_user_and_login(self, user_data):
        user = UserModel.objects.create_user(**user_data)
        self.client.login(**self.VALID_USER_DATA)
        return user

    def test_sign_up__when_data_is_valid__expect_logged_in_user(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('register user'))
        self.client.login(**self.VALID_USER_DATA)
        print(response.context['user'])
        self.assertEqual(self.VALID_USER_DATA['username'], response.context['user'].username)
