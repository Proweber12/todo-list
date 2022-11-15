# Тесты отрабатывают корректно, при включенной базовой и сессионной аутентификации в settings.py, вместо JWT и Token,
# а также выключить(закомментировать) authentication_classes = [JWTAuthentication] в todoapp/views.py в 2-ух классах

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate

from todoapp.views import TodoModelViewSet
from usersapp.models import User


class TestProjectModelViewSet(APITestCase):
    def setUp(self) -> None:
        self.name = "admin"
        self.password = "admin"
        self.email = "admin@gmail.com"
        self.data_user = {
            "username": "mihail315",
            "first_name": "Mihail",
            "last_name": "Savchenko",
            "email": "msav@gmail.com",
        }
        self.user = User.objects.create(**self.data_user)
        self.data = {"name": "Интернет-магазин", "users": [self.user], "link": "https://shop.com"}
        self.data_put = {"name": "Сайт-визитка", "users": [self.user], "link": "https://vizitka.com"}

        self.url = "/api/projects/"

        self.admin_user = User.objects.create_superuser(username=self.name, email=self.email, password=self.password)

    def test_get_list_unauthorized(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list_authorized(self):
        self.client.login(username=self.name, password=self.password)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self) -> None:
        pass


class TestTodoModelViewSet(TestCase):
    def setUp(self) -> None:
        self.name = "admin"
        self.password = "admin"
        self.email = "admin@gmail.com"

        self.url = "/api/todo/"

        self.data_todo = {"project": 1, "text": "Создать интернет-магазин", "is_active": True, "creator": 1}

        self.admin_user = User.objects.create_superuser(username=self.name, email=self.email, password=self.password)

    def test_get_list_unauthorized(self):
        factory = APIRequestFactory()
        requests = factory.get(self.url)
        view = TodoModelViewSet.as_view({"get": "list"})
        response = view(requests)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list_authorized(self):
        factory = APIRequestFactory()
        requests = factory.get(self.url)
        force_authenticate(requests, self.admin_user)
        view = TodoModelViewSet.as_view({"get": "list"})
        response = view(requests)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_todo(self):
        factory = APIRequestFactory()
        requests = factory.post(self.url, self.data_todo, format="json")
        force_authenticate(requests, self.admin_user)
        view = TodoModelViewSet.as_view({"post": "create"})
        response = view(requests)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def tearDown(self) -> None:
        pass
