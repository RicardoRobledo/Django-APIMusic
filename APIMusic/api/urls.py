"""
This module contains URL Configuration about api app
"""


__author__ = "Ricardo Robledo"
__version__ = "0.1"


from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import(
    AlbumViewSet,
    ArtistViewSet,
    BandViewSet,
    SongViewSet
)


# paths
router = SimpleRouter()
router.register('', ArtistViewSet, basename='artist')
router.register('album', AlbumViewSet, basename='album')
router.register('band', BandViewSet, basename='band')
router.register('song', SongViewSet, basename='song')

urlpatterns = router.urls
