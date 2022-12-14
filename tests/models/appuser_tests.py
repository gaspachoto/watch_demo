from django.core.exceptions import ValidationError
from django.test import TestCase

from watch_demo.accounts.models import AppUser


class AppUserModelTests(TestCase):
    # Triple A - Arrange, Act, Assert

    def test_profile_save__with_correct_values__expect_success(self):
        # Arrange
        profile = AppUser(
            username='Vladimir',
            email='vlad@iliev.com',
            password='qwer1234ASDF',
            first_name='Vladimir',
            last_name='Iliev',
            gender='male',
        )

        # Act
        profile.full_clean()  # Call this for validation
        profile.save()

        # Assert
        self.assertIsNotNone(profile.pk)

    def test_profile_save__with_incorrect_name__expect_exception(self):
        # Arrange
        profile = AppUser(
            username='Vladimir',
            email='vlad@iliev.com',
            password='qwer1234ASDF',
            first_name='Vladimir3',
            last_name='Iliev',
            gender='male',
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)