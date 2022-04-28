from django.core.management.base import BaseCommand

from todoapp.models import Todo


class Command(BaseCommand):
    def handle(self, *args, **options):
        Todo.objects.all().delete()

        Todo.objects.create(
            text="Сверстать хедер", creator_id=3, project_id=1
        )

        Todo.objects.create(
            text="Добавить в админку возможность добавления товара", creator_id=2, project_id=2
        )

        Todo.objects.create(
            text="Написать тесты к приложению productsapp", creator_id=4, project_id=3
        )

        Todo.objects.create(
            text="Развернуть проект на VPS-сервере", creator_id=2, project_id=3
        )

