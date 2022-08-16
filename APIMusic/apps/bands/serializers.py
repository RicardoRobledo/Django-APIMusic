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
