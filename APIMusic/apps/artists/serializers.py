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


    def to_representation(self, instance):
        
        return {
            'id': instance.id,
            'name': instance.name,
            'middle_name': instance.middle_name,
            'last_name': instance.last_name,
            'genre': instance.genre,
            'role': instance.role,
            'band': instance.band.band_name,
            'created_at': instance.created_at,
        }
