from django.urls import path
from .views import UserCreate, UserLogin, UserLogout

urlpatterns = [
    path('signup/', UserCreate.as_view(), name='create-user'),
    path('login/', UserLogin.as_view(), name='login-user'),
    path('logout/', UserLogout.as_view(), name='logout-user'),
]