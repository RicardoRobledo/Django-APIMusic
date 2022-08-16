from rest_framework.routers import SimpleRouter
from .views.album_viewsets import AlbumViewSet
from .views.general_viewsets import SongViewSet


__author__ = "Ricardo Robledo"
__version__ = "0.1"


# paths
router = SimpleRouter()
router.register('album', AlbumViewSet, basename='album')
router.register('song', SongViewSet, basename='song')

urlpatterns = router.urls
