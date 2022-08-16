from rest_framework import viewsets

from .models import Band
from .serializers import BandSerializer


# -----------------------------------------------------------------
#                            Band
# -----------------------------------------------------------------


class BandViewSet(viewsets.ModelViewSet):

    queryset = Band.objects.all()
    serializer_class = BandSerializer
