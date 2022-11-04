# Тесты отрабатывают корректно, при включенной базовой и сессионной аутентификации в settings.py, вместо JWT и Token,
# а также выключить(закомментировать) authentication_classes = [JWTAuthentication] в usersapp/views.py в 1-ом классе

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase, RequestsClient, APIRequestFactory, force_authenticate
from mixer.backend.django import mixer

from usersapp.views import UserCustomViewSet
from usersapp.models import User


class TestUserCustomViewSet(TestCase):

    def setUp(self) -> None:
        self.name = 'admin'
        self.password = 'admin'
        self.email = 'admin@gmail.com'

        self.url = '/api/users/'

        self.data = {'username': 'roma135', 'first_name': 'Roman', 'last_name': 'Semenov', 'email': 'roman@gmail.com'}
        self.data_put = {'username': 'mihail315', 'first_name': 'Mihail', 'last_name': 'Savchenko', 'email': 'msav@gmail.com'}

        self.admin_user = User.objects.create_superuser(
            username=self.name, email=self.email, password=self.password
        )

    def test_get_list_unauthorized(self):
        factory = APIRequestFactory()
        requests = factory.get(self.url)
        view = UserCustomViewSet.as_view({'get': 'list'})
        response = view(requests)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list_authorized(self):
        factory = APIRequestFactory()
        requests = factory.get(self.url)
        force_authenticate(requests, self.admin_user)
        view = UserCustomViewSet.as_view({'get': 'list'})
        response = view(requests)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_detail(self):
        client = APIClient()
        user = User.objects.create(**self.data)
        response = client.get(f'{self.url}{user.id}/')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_user_admin(self):
        client = APIClient()
        user = User.objects.create(**self.data)
        client.login(username=self.name, password=self.password)
        response = client.put(f'{self.url}{user.id}/', self.data_put)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user_data = User.objects.get(id=user.id)
        self.assertEqual(user_data.username, 'mihail315')
        self.assertEqual(user_data.first_name, 'Mihail')
        self.assertEqual(user_data.last_name, 'Savchenko')
        self.assertEqual(user_data.email, 'msav@gmail.com')
        client.logout()

    def tearDown(self) -> None:
        pass


class APITestUserCustomViewSet(APITestCase):

    def setUp(self) -> None:
        self.name = 'admin'
        self.password = 'admin'
        self.email = 'admin@gmail.com'

        self.url = '/api/users/'

        self.data_put = {'username': 'mihail315', 'first_name': 'Mihail', 'last_name': 'Savchenko', 'email': 'msav@gmail.com'}

        self.admin_user = User.objects.create_superuser(
            username=self.name, email=self.email, password=self.password
        )

    def test_put_mixer(self):
        user = mixer.blend(User)
        self.client.login(username=self.name, password=self.password)
        response = self.client.put(f'{self.url}{user.id}/', self.data_put)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user_data = User.objects.get(id=user.id)
        self.assertEqual(user_data.username, 'mihail315')
        self.assertEqual(user_data.first_name, 'Mihail')
        self.assertEqual(user_data.last_name, 'Savchenko')
        self.assertEqual(user_data.email, 'msav@gmail.com')
        self.client.logout()

    def tearDown(self) -> None:
        pass


class LiveTestUserCustomViewSet(RequestsClient):

    def setUp(self) -> None:
        pass

    def test_auth(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self) -> None:
        pass
