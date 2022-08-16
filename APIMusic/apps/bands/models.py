from django.db import models


__author__ = "Ricardo Robledo"
__version__ = "0.1"


# -----------------------------------------------------------------
#                              Band
# -----------------------------------------------------------------


class Band(models.Model):
    """
    This class define our Band model
    
    Attributes:
        band_name (str): Band name.
        musical_genre tuple(str): Musical genre that the band plays.
        created_at (datetime): Date of sign in of the band in the database.
    """
    
    
    class Genre(models.TextChoices):
        """
        This inner class define our choices for musical genres
    
        Attributes:
            ROCK tuple(str): Choice for rock genre.
            INDIE_FOLK tuple(str): Choice for indie folk genre.
            POP_ROCK tuple(str): Choice for pop rock genre.
            ELECTRONIC tuple(str): Choice for electronic genre.
        """
        
        ROCK = ('ROCK', 'Rock')
        INDIE_FOLK = ('INDIE_FOLK', 'Indie folk')
        POP_ROCK = ('POP_ROCK', 'Pock rock')
        ELECTRONIC = ('ELECTRONIC', 'Electronic')
    
    
    band_name = models.CharField(max_length=15)
    musical_genre = models.CharField(
        max_length=15,
        choices=Genre.choices
    )
    created_at = models.DateTimeField(auto_now_add=True)
    album = models.ManyToManyField('albums.Album', through='albums.Song')
    
    
    def __str__(self):
        return self.band_name
