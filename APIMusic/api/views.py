from .models import Album, Artist, Band, Song
from rest_framework import viewsets
from .serializers import(
    AlbumSerializer,
    ArtistSerializer,
    BandSerializer,
    SongSerializer
)


# -----------------------------------------------------------------
#                             Album
# -----------------------------------------------------------------


class AlbumViewSet(viewsets.ModelViewSet):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


# -----------------------------------------------------------------
#                            Artist
# -----------------------------------------------------------------


class ArtistViewSet(viewsets.ModelViewSet):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


# -----------------------------------------------------------------
#                            Band
# -----------------------------------------------------------------


class BandViewSet(viewsets.ModelViewSet):

    queryset = Band.objects.all()
    serializer_class = BandSerializer
