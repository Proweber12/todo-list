from rest_framework.renderers import AdminRenderer, JSONRenderer

from rest_framework.viewsets import ModelViewSet

from .models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer


class ProjectModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class TodoModelViewSet(ModelViewSet):
    renderer_classes = [AdminRenderer]
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer

