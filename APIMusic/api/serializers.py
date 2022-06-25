"""
This module define our serializers
"""


__author__ = "Ricardo Robledo"
__version__ = "0.1"


from rest_framework import serializers
from api.models import Album, Artist, Band, Song


# -----------------------------------------------------------------
#                             Album
# -----------------------------------------------------------------


class AlbumSerializer(serializers.ModelSerializer):
    """
    Class to serialize Album class
    """

    
    class Meta:
        
        model = Album
        fields = ('id', 'album_name', 'created_at',)


# -----------------------------------------------------------------
#                              Band
# -----------------------------------------------------------------


class BandSerializer(serializers.ModelSerializer):
    """
    Class to serialize Band class
    """
    
    
    class Meta:
        
        fields = ('id', 'band_name', 'musical_genre',
                'created_at', 'album',)
        model = Band

