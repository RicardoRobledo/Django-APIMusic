from .models import Album, Artist, Band, Song
from rest_framework import viewsets
from .serializers import AlbumSerializer


class AlbumViewSet(viewsets.ModelViewSet):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
