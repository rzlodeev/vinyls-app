from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from .models import User


class RegisterUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'is_staff')
