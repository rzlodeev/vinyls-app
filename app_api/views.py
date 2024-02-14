from app.models import Disc
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .serializers import UserSerializer, UsersDiscSerializer


class UserList(viewsets.GenericViewSet,
               mixins.RetrieveModelMixin,
               mixins.ListModelMixin):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


class UserDiscList(viewsets.ModelViewSet):
    """
    Viewset of user's discs
    """
    permission_classes = [IsAuthenticated]
    serializer_class = UsersDiscSerializer

    def get_queryset(self):
        # user = get_object_or_404(settings.AUTH_USER_MODEL, pk=user_id)
        return Disc.objects.all()


class DiscList(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = UsersDiscSerializer

    def get_queryset(self):
        return Disc.objects.all()
