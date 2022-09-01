from rest_framework import serializers

from .models import Band
from apps.albums.models import Song


# -----------------------------------------------------------------
#                              Band
# -----------------------------------------------------------------


class BandSerializer(serializers.ModelSerializer):
    """
    Class to serialize Band class
    """
    
    
    class Meta:
        
        model = Band
        fields = ('id', 'band_name', 'musical_genre', 'created_at',)


    def to_representation(self, instance):

        songs = [
            song.song_name
            for song in Song.objects.select_related('album').filter(band=instance.id)
        ]
        
        return {
            'id': instance.id,
            'band_name': instance.band_name,
            'musical_genre': instance.musical_genre,
            'songs': songs,
            'created_at': instance.created_at,
        }
