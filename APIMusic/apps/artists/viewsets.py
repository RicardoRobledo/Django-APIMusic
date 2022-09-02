from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
import django_filters
from rest_framework.permissions import IsAuthenticated

#from apps.base.permissions import IsOwner
from .models import Artist
from .serializers import ArtistSerializer


# -----------------------------------------------------------------
#                            Artist
# -----------------------------------------------------------------


class ArtistFilter(django_filters.FilterSet):
    
    name = django_filters.CharFilter(field_name='name', lookup_expr='exact')
    middle_name = django_filters.CharFilter(field_name='name', lookup_expr='exact')
    last_name = django_filters.CharFilter(field_name='name', lookup_expr='exact')
    genre = django_filters.CharFilter(field_name='genre', lookup_expr='exact')
    role = django_filters.CharFilter(field_name='role', lookup_expr='exact')
    
    created_at = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='exact')
    created_at_before = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lt')
    created_at_after = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gt')

    class Meta:
        model = Artist
        fields = {
            'name',
            'middle_name',
            'last_name',
            'genre',
            'role',
            'created_at',
        }


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

    permission_classes = (IsAuthenticated,)
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filterset_class = ArtistFilter
