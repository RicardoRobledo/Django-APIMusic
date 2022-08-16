from rest_framework import viewsets

from .models import Artist
from .serializers import ArtistSerializer


# -----------------------------------------------------------------
#                            Artist
# -----------------------------------------------------------------


class ArtistViewSet(viewsets.ModelViewSet):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
