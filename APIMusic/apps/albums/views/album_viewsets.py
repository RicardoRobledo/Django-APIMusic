from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

from ..models import Album
from ..serializers.album_serializers import AlbumSerializer


# -----------------------------------------------------------------
#                             Album
# -----------------------------------------------------------------


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="""
    list our album
    """
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="""
    get an album

    :param id: id of our album.
    """
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="""
    create an album

    :param album_name: name of the album.
    """
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_description="""
    update an album

    :param id: id of our album.
    :param album_name: name of the album.
    """
))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    operation_description="""
    update an album

    :param id: id of our album.
    :param album_name: name of the album.
    """
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_description="""
    eliminate an album

    :param id: id of an album.
    """
))
class AlbumViewSet(viewsets.ModelViewSet):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
