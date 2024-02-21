from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from app.models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileList(GenericViewSet,
                      mixins.RetrieveModelMixin):
    queryset = UserProfile
    serializer_class = UserProfileSerializer


