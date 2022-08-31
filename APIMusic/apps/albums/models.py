from django.db import models


__author__ = "Ricardo Robledo"
__version__ = "0.1"


# -----------------------------------------------------------------
#                             Album
# -----------------------------------------------------------------


class Album(models.Model):
    """
    This class define our Album model
    
    Attributes:
        album_name (str): Album name.
        created_at (datetime): Date of sign in of the album in the database.
    """

    
    album_name = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.album_name


# -----------------------------------------------------------------
#                             Song
# -----------------------------------------------------------------


class Song(models.Model):
    """
    This class define our Song model
    
    Attributes:
        song_name (str): Song name.
        duration_in_minutes (str): Duration of the song in minutes.
        created_at (datetime): Date of sign in of the album in the database.
        band (int): Identifier of a band.
        album (int): Identifier of an album.
    """

    
    song_name = models.CharField(max_length=15)
    duration_in_minutes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    band = models.ForeignKey('bands.Band', related_name='songs', on_delete=models.CASCADE)
    album = models.ForeignKey('albums.Album', related_name='songs', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.song_name
