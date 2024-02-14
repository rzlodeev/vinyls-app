from rest_framework.routers import DefaultRouter
from app_api.views import UserList, DiscList

router = DefaultRouter()
router.register(r'users', UserList, basename='user')
router.register(r'discs', DiscList, basename='disc')
urlpatterns = router.urls
