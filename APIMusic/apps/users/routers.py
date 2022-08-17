from rest_framework.routers import SimpleRouter

from .viewsets import UserViewSet

router = SimpleRouter()

router.register('user', UserViewSet, basename='user')

urlpatterns = router.urls
