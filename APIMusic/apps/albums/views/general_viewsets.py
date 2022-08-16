from rest_framework import viewsets

from ..models import Song
from ..serializers.general_serializers import SongSerializer


# -----------------------------------------------------------------
#                            Song
# -----------------------------------------------------------------


class SongViewSet(viewsets.ModelViewSet):

    queryset = Song.objects.all()
    serializer_class = SongSerializer
