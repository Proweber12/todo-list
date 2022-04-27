from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from graphene_django.views import GraphQLView
from rest_framework import permissions
from rest_framework.routers import SimpleRouter

# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from usersapp.views import UserCustomViewSet
from todoapp.views import ProjectModelViewSet, TodoModelViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="ToDo",
        default_version="0.1",
        description="Documentation about project ToDo-List",
        contact=openapi.Contact(email="admin@gmail.com"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = SimpleRouter()
# router.register('users', UserCustomViewSet)
router.register("projects", ProjectModelViewSet)
router.register("todo", TodoModelViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    path("api-token-auth/", TokenObtainPairView.as_view()),
    path("api-token-auth/refresh/", TokenRefreshView.as_view()),
    path("api/users/0.1/", include("usersapp.urls", namespace="0.1")),
    path("api/users/0.2/", include("usersapp.urls", namespace="0.2")),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0)),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
]
