from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

from ..models import Song
from ..serializers.general_serializers import SongSerializer


# -----------------------------------------------------------------
#                            Song
# -----------------------------------------------------------------


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="""
    list our songs
    """
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="""
    get a song

    :param id: id of our song.
    """
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="""
    create a song

    :param song_name: name of a song.
    :param duration_in_minutes: minutes of duration.
    :param band: id of a band.
    :param album: id of a album.
    """
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_description="""
    update a song

    :param id: id of our song.
    :param song_name: name of a song.
    :param duration_in_minutes: minutes of duration.
    :param band: id of a band.
    :param album: id of a album.
    """
))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    operation_description="""
    update a song

    :param id: id of our song.
    :param song_name: name of a song.
    :param duration_in_minutes: minutes of duration.
    :param band: id of a band.
    :param album: id of a album.
    """
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_description="""
    eliminate a song

    :param id: id of a song.
    """
))
class SongViewSet(viewsets.ModelViewSet):

    queryset = Song.objects.all()
    serializer_class = SongSerializer
