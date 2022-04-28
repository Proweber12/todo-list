from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .filters import ProjectFilter, TodoFilter
from .models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer


class ProjectLimitOffsetPagination(PageNumberPagination):
    page_size = 10


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter
    authentication_classes = [JWTAuthentication]


class TodoLimitOffsetPagination(PageNumberPagination):
    page_size = 20


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    pagination_class = TodoLimitOffsetPagination
    filterset_class = TodoFilter
    authentication_classes = [JWTAuthentication]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
