from django.urls import include, path
from rest_framework.routers import SimpleRouter

from usersapp.views import UserCustomViewSet

app_name = "usersapp"

router = SimpleRouter()
router.register("", UserCustomViewSet)

urlpatterns = [
    path("", include((router.urls, "usersapp"))),
]
