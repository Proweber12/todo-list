from django.core.management.base import BaseCommand

from todoapp.models import Project
from usersapp.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user_1 = User.objects.get(pk=1)
        user_2 = User.objects.get(pk=2)
        user_3 = User.objects.get(pk=3)
        user_4 = User.objects.get(pk=4)

        Project.objects.all().delete()

        Project.objects.create(
            name="Сайт-визитка", link="https://www.repos.site-vizitka.com"
        )
        Project.objects.get(pk=1).users.add(user_1, user_3)

        Project.objects.create(
            name="Интернет-магазин", link="https://www.repos.shop.com"
        )
        Project.objects.get(pk=2).users.add(user_2)

        Project.objects.create(
            name="Сайт компании", link="https://www.repos.company.com"
        )
        Project.objects.get(pk=3).users.add(user_2, user_4)
