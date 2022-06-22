from django.db import models


__author__ = "Ricardo Robledo"
__version__ = "0.1"


# -----------------------------------------------------------------
#                             Artist
# -----------------------------------------------------------------


class Artist(models.Model):
    """
    This class define our Artist model
    
    Attributes:
        name (str): Name of an artist.
        middle_name (str): Middle name of an artist.
        last_name (str): last_name of an artist.
        age (int):  Age of an artist.
        genre (str): Genre of an artist.
        role (str): Role of an artist.
        created_at (datetime): Date of sign in of the artist in the database.
        band (str): Band of our artist.
    """


    class Genre(models.TextChoices):
        """
        This inner class define our choices for a genre of an artist
    
        Attributes:
            FEMALE tuple(str): Choice for a female artist.
            MALE tuple(str): Choice for a male artist.
        """
        
        FEMALE = ('F', 'Female')
        MALE = ('M', 'Male')


    name = models.CharField(max_length=15)
    middle_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    age = models.IntegerField()
    genre = models.CharField(
        max_length=1,
        choices=[Genre.FEMALE, Genre.MALE,]
    )
    role = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    band = models.CharField(max_length=15)
    
    
    def __str__(self):
        return self.name


# -----------------------------------------------------------------
#                              Band
# -----------------------------------------------------------------


class Band(models.Model):
    """
    This class define our Band model
    
    Attributes:
        band_name tuple(str): Band name.
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
        choices=[Genre.ROCK, Genre.INDIE_FOLK,
                Genre.POP_ROCK, Genre.ELECTRONIC,]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.band_name
    