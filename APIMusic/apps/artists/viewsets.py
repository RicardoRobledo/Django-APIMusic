from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

from .models import Artist
from .serializers import ArtistSerializer


# -----------------------------------------------------------------
#                            Artist
# -----------------------------------------------------------------


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="""
    list our artists
    """
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="""
    get a artist

    :param id: id of our artist.
    """
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="""
    create a artist

    :param name: name of an artist.
    :param middle_name: middle name of an artist.
    :param last_name: last_name of an artist.
    :param genre: genre of our artist
    :param role: role of the artist.
    :param band: band that the artist belongs.
    """
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_description="""
    update a band

    :param band_name: name of a band.
    :param musical_genre: name of our user.
    """
))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    operation_description="""
    update a band

    :param band_name: name of a band.
    :param musical_genre: name of our user.
    """
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_description="""
    eliminate an artist

    :param id: id of an artist.
    """
))
class ArtistViewSet(viewsets.ModelViewSet):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
