from django.db import models
# Create your models here.

class Album(models.Model):
    album_title = models.CharField(max_length=500)
    artist = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    album_logo = models.FileField()

    def __str__(self):
        return self.album_title

class Song(models.Model):
    song_title = models.CharField(max_length=250)
    songFile = models.CharField(max_length=10)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.song_title
