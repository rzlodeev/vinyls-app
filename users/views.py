from django.contrib.auth import authenticate, get_user_model
from rest_framework import status, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer

from .serializers import RegisterUserSerializer
from .models import User


class UserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            if new_user:
                refresh = RefreshToken.for_user(new_user)
                refresh.payload.update({
                    'user_id': new_user.id,
                    'email': new_user.email
                })

                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }, status=status.HTTP_201_CREATED)

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


class UserLogout(APIView):

    def post(self, request):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({'error': 'Refresh token is missing'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response({'error': f'{e}'},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response({'success': 'Logout successfully'},
                        status=status.HTTP_200_OK)


class UserList(GenericViewSet,
               mixins.RetrieveModelMixin,
               mixins.ListModelMixin):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

    def get_permissions(self):
        permissions_mapping = {
            'list': [IsAdminUser],
            'retrieve': [AllowAny]
        }
        permission_classes = permissions_mapping.get(self.action, [])
        return [permission() for permission in permission_classes]
