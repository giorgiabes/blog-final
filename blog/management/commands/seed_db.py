from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from blog.models import Post


class Command(BaseCommand):

    def handle(self, *args, **options):
        faker = Faker()

        for _ in range(102):
            Post.objects.create(
                title=faker.text(max_nb_chars=20),
                author=User.objects.get(id=1),
                body=faker.text(),
            )
