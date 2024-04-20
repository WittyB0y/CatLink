from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from CatApp import settings

TEST_DATA_SET = settings.TEST_DATA_SET


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for _ in range(0, TEST_DATA_SET):
            email = f'user{_}@example.com'
            User.objects.create_user(
                username=email,
                password='userTest123',
                email=email,
            )
        User.objects.create_user(
            username='spammerbyother@gmail.com',
            password='userTest123',
            email='spammerbyother@gmail.com',
            is_superuser=True,
            is_staff=True,
        )

        self.stdout.write("Success: Users were added to DB!")
