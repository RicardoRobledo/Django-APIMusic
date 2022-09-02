from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
import django_filters
from rest_framework.permissions import BasePermission

from ..models import Song
from ..serializers.general_serializers import SongSerializer


# -----------------------------------------------------------------
#                            Song
# -----------------------------------------------------------------

class SongFilter(django_filters.FilterSet):
    
    song_name = django_filters.CharFilter(field_name='song_name', lookup_expr='exact')
    duration_in_minutes = django_filters.NumberFilter(field_name='duration_in_minutes', lookup_expr='exact')
    band = django_filters.NumberFilter(field_name='band', lookup_expr='exact')
    album = django_filters.NumberFilter(field_name='album', lookup_expr='exact')
    
    created_at = django_filters.NumberFilter(field_name='album', lookup_expr='exact')
    created_at_before = django_filters.NumberFilter(field_name='album', lookup_expr='lt')
    created_at_created_atfter = django_filters.NumberFilter(field_name='album', lookup_expr='gt')
    
    class Meta:
        model = Song
        fields = {
            'song_name',
            'duration_in_minutes',
            'created_at',
            'band',
            'album',
        }


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

    permission_classes = (BasePermission,)
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filterset_class = SongFilter
