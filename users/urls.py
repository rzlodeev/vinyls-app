from django.urls import path
from .views import UserCreate, UserLogin, UserLogout, UserList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserList, basename='users')

urlpatterns = [
    path('signup/', UserCreate.as_view(), name='create-user'),
    path('login/', UserLogin.as_view(), name='login-user'),
    path('logout/', UserLogout.as_view(), name='logout-user'),
]

urlpatterns += router.urls
