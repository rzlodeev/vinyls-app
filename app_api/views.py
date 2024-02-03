from app.models import Disc
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, UsersDiscSerializer


class UserList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        User = get_user_model()
        return User.objects.all()

    def update(self, request, *args, **kwargs):
        pass


class UserDiscList(viewsets.ModelViewSet):
    """
    Viewset of user's discs
    """
    permission_classes = [IsAuthenticated]
    serializer_class = UsersDiscSerializer

    def get_queryset(self):
        # user = get_object_or_404(settings.AUTH_USER_MODEL, pk=user_id)
        return Disc.objects.all()
