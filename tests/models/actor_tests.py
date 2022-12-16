from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse_lazy

from watch_demo.movies.models import Actor

UserModel = get_user_model()


class ActorAddTests(TestCase):
    VALID_USER_DATA = {
        'username': 'test_user',
        'email': 'user@test.com',
        'password': 'qwer1234ASDF',
    }

    def create_user_and_login(self, user_data):
        user = UserModel.objects.create_user(**user_data)
        self.client.login(**self.VALID_USER_DATA)
        return user

    def test_actor_add_view__with_correct_data_expect_success(self):
        actor = Actor(
            first_name='John',
            last_name='Travolta'
        )

        actor.save()
        full_name = f'{actor.first_name} {actor.last_name}'

        self.assertEqual(full_name, actor.full_name)

    def test_actor_add_view__with_incorrect_data_expect_exception(self):
        user = self.create_user_and_login(self.VALID_USER_DATA)
        actor = Actor(
            first_name='John',
            last_name='Travolta'
        )
        actor.save()
        with self.assertRaises(ValidationError) as context:
            user.full_clean()
            user.save()

        self.assertIsNotNone(context.exception)