from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
import django_filters

from .models import Band
from .serializers import BandSerializer


# -----------------------------------------------------------------
#                            Band
# -----------------------------------------------------------------

class BandFilter(django_filters.FilterSet):
    
    band_name = django_filters.CharFilter(field_name='band_name', lookup_expr='exact')
    musical_genre = django_filters.CharFilter(field_name='musical_genre', lookup_expr='exact')
    
    created_at = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='exact')
    created_at_before = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lt')
    created_at_after = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gt')
    
    class Meta:
        model = Band
        fields = {
            'band_name',
            'musical_genre',
            'created_at',
        }


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="""
    list our bands
    """
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="""
    get a band

    :param id: id of our band.
    """
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="""
    create a band

    :param band_name: name of a band.
    :param musical_genre: name of our user.
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
    eliminate a ba

    :param id: id of a band.
    """
))
class BandViewSet(viewsets.ModelViewSet):

    queryset = Band.objects.all()
    serializer_class = BandSerializer
    filterset_class = BandFilter
