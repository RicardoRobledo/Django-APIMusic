from rest_framework import serializers
from ..models import Album


__author__ = "Ricardo Robledo"
__version__ = "0.1"


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
