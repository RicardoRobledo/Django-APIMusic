from rest_framework import serializers

from .models import Band


# -----------------------------------------------------------------
#                              Band
# -----------------------------------------------------------------


class BandSerializer(serializers.ModelSerializer):
    """
    Class to serialize Band class
    """
    
    
    class Meta:
        
        model = Band
        fields = ('id', 'band_name', 'musical_genre',
                'created_at', 'album',)


    def to_representation(self, instance):
        

        return {
            'id': instance.id,
            'band_name': instance.band_name,
            'musical_genre': instance.musical_genre,
            'created_at': instance.created_at,
        }
