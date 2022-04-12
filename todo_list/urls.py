from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from usersapp.views import UserCustomViewSet
from todoapp.views import ProjectModelViewSet, TodoModelViewSet

router = DefaultRouter()
router.register('users', UserCustomViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todo', TodoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth/', TokenObtainPairView.as_view()),
    path('api-token-auth/refresh/', TokenRefreshView.as_view()),
]
