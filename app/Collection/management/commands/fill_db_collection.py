import random
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from CatApp import settings
from Collection.models import Collection
from Link.models import Link

TEST_DATA_SET = settings.TEST_DATA_SET


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        all_users = User.objects.all()
        for user in all_users:
            rand = random.randint(2, 5)
            for i in range(1, rand):
                name = f'Collection {i} for {user.username}'
                description = f'Test collection {i} for {user.username}'
                collection = Collection.objects.create(
                    user=user,
                    name=name,
                    description=description
                )

                # Create links for the collection
                rand_link = random.randint(2, 6)
                for j in range(1, rand_link):
                    title = f'Link {j} in {name}'
                    description = f'Test link {j} in {name}'
                    url = f'https://example.com/link{i}_{j}'
                    image = f'https://example.com/image{i}_{j}.jpg'
                    link_type = random.randint(1, 5)
                    link = Link.objects.create(
                        user=user,
                        title=title,
                        description=description,
                        url=url,
                        image=image,
                        link_type=link_type
                    )
                    link.collections.add(collection)

        self.stdout.write("Success: Collections and Links were added to DB!")
