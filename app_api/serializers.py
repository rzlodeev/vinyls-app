from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from app.models import Disc, UserProfile
from django.conf import settings


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile.objects.all()
        fields = '__all__'
