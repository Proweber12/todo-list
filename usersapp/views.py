from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import User
from .serializers import UserModelSerializer, UserBaseModelSerializer


class UserCustomViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    authentication_classes = [JWTAuthentication]

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return UserModelSerializer
        return UserBaseModelSerializer
