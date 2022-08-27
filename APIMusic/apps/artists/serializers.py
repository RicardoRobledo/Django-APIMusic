from rest_framework import serializers
from .models import Artist


__author__ = "Ricardo Robledo"
__version__ = "0.1"


# -----------------------------------------------------------------
#                             Artist
# -----------------------------------------------------------------


class ArtistSerializer(serializers.ModelSerializer):
    """
    Class to serialize Artist class
    """

    
    class Meta:
            
        model = Artist
        fields = ('id' ,'name', 'middle_name', 'last_name',
                'genre', 'role', 'band', 'created_at')