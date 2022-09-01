from rest_framework import serializers

from ..models import Song


# -----------------------------------------------------------------
#                             Song
# -----------------------------------------------------------------


class SongSerializer(serializers.ModelSerializer):
    """
    Class to serialize Song class
    """

    
    class Meta:
        
        model = Song
        fields = ('id' ,'song_name', 'duration_in_minutes', 'created_at',
                'band', 'album',)


    def to_representation(self, instance):
        
        return {
            'id': instance.id,
            'song_name': instance.song_name,
            'duration_in_minutes': instance.duration_in_minutes,
            'created_at': instance.created_at,
            'band': instance.band.band_name,
        }
