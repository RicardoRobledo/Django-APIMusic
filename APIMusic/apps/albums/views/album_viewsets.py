from rest_framework import viewsets
from ..models import Album
from ..serializers.album_serializers import AlbumSerializer


# -----------------------------------------------------------------
#                             Album
# -----------------------------------------------------------------


class AlbumViewSet(viewsets.ModelViewSet):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
