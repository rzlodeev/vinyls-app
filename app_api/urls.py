from rest_framework.routers import DefaultRouter
from .views import UserProfileList

router = DefaultRouter()
router.register(r'user-profile', UserProfileList, basename='user-profile')
urlpatterns = router.urls
