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
        genre (str): Genre of an artist.
        role (str): Role of an artist.
        created_at (datetime): Date of sign in of the artist in the database.
        band (int): Identifier of a band.
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
    genre = models.CharField(
        max_length=1,
        choices=Genre.choices
    )
    role = models.CharField(max_length=15)
    band = models.ForeignKey('bands.Band', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
