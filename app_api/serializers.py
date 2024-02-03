from rest_framework import serializers
from django.contrib.auth import get_user_model
from app.models import Disc
from django.conf import settings


class UsersDiscSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disc
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    discs = UsersDiscSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'is_staff', 'discs')

