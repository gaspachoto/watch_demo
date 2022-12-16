from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, reverse_lazy

UserModel = get_user_model()


class EditProfileViewTests(TestCase):

    def test__profile_edit_anonymous_user__expect_to_redirect_to_login(self):
        profile_data = {
            'first_name': 'Vladimir',
            'last_name': 'Iliev',
        }

        response = self.client.post(reverse_lazy('edit user', kwargs={'pk': 1}), data=profile_data)

        self.assertEqual(302, response.status_code)
        self.assertEqual(settings.LOGIN_URL + f'?next=/accounts/profile/1/edit/', response.headers.get('Location'))