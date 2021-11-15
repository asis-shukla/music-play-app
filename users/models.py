from django.db import models
from music.models import Album, Song
# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    favSongs = models.ManyToManyField(Song)
    favAlbums = models.ManyToManyField(Album)
    email = models.EmailField()
    birthDate = models.DateField()
    profilePicture = models.FileField()
    
    def __str__(self) -> str:
        return self.firstName