from django.test import TestCase
from django.urls import reverse, reverse_lazy


class SignUpViewTests(TestCase):
    VALID_USER_DATA = {
        'username': 'test_user1',
        'email': 'user@test.com',
        'password': 'qwer1234ASDF',
        'password2': 'qwer1234ASDF',
    }

    def test_sign_up__when_data_is_valid__expect_logged_in_user(self):
        response = self.client.post(
            reverse('register user'),
            data=self.VALID_USER_DATA,
        )
        print(response.context['user'])
        self.assertEqual(self.VALID_USER_DATA['username'], response.context['user'].username)
