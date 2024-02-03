from rest_framework.routers import DefaultRouter
from app_api.views import UserList

router = DefaultRouter()
router.register(r'users', UserList, basename='user')
urlpatterns = router.urls
