from django.core.management.base import BaseCommand

from usersapp.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.all().delete()

        User.objects.create_superuser(
            username="admin", first_name="Михаил", last_name="Савченко", email="admin@gmail.com"
        )

        User.objects.create_user(
            username="Petya23", first_name="Пётр", last_name="Иванов", email="petya.ivanov@gmail.com"
        )

        User.objects.create_user(
            username="Alex243", first_name="Алексей", last_name="Петров", email="alex.petrov@gmail.com"
        )

        User.objects.create_user(username="Max69", first_name="Максим", last_name="Копылов", email="max.kop@gmail.com")
