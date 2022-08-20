from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

from .models import Band
from .serializers import BandSerializer


# -----------------------------------------------------------------
#                            Band
# -----------------------------------------------------------------


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
