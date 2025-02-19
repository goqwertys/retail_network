from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.permissions import IsOwnerOrReadOnly
from users.serializers import UserSerializer, UserProfileSerializer, UserUpdateSerializer


class UserCreateAPIView(CreateAPIView):
    """ API view for registration """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny, )


class UserProfileViewSet(ModelViewSet):
    """ User CRUD """
    queryset = User.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action in ('update', 'partial_update'):
            return UserUpdateSerializer
        return UserProfileSerializer
