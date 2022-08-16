from rest_framework.routers import SimpleRouter

from .viewsets import BandViewSet


__author__ = "Ricardo Robledo"
__version__ = "0.1"


# paths
router = SimpleRouter()
router.register('band', BandViewSet, basename='band')

urlpatterns = router.urls
