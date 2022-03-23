from rest_framework.serializers import ModelSerializer

from usersapp.serializers import UserModelSerializer
from .models import Project, Todo


class ProjectModelSerializer(ModelSerializer):
    users = UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(ModelSerializer):
    creator = UserModelSerializer()

    class Meta:
        model = Todo
        fields = '__all__'