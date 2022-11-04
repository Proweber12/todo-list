from django.urls import path, include
from rest_framework.routers import DefaultRouter

from usersapp.views import UserCustomViewSet

app_name = 'usersapp'

router = DefaultRouter()
router.register('', UserCustomViewSet)

urlpatterns = [
    path('', include((router.urls, 'usersapp'))),
]
