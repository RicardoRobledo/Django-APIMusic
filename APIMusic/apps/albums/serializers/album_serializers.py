from rest_framework import serializers

from ..models import Album, Song


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


    def to_representation(self, instance):
        
        songs = [song.song_name for song in Song.objects.filter(album=instance.id)]
        
        return {
            'id': instance.id,
            'album_name': instance.album_name,
            'created_at': instance.created_at,
            'songs': songs,
        }
