from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterUserSerializer
from .models import User


class UserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if email is None or password is None:
            return Response({'error': 'Email or password missing'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(email=email, password=password)

        if user is None:
            return Response({'error': 'Wrong credentials'}, status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user)
        refresh.payload.update({
            'user_id': user.id,
            'email': user.email
        })

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        })
