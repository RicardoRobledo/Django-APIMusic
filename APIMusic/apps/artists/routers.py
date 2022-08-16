from rest_framework.routers import SimpleRouter

from .viewsets import ArtistViewSet


router = SimpleRouter()
router.register('artist', ArtistViewSet, basename='artist')

urlpatterns = router.urls
