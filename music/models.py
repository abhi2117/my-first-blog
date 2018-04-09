from django.db import models
from django.utils import timezone

# Create your models here.


class Album(models.Model):
	album_title = models.CharField(max_length=200)
	album_logo = models.CharField(max_length=500)
	artist = models.CharField(max_length=200)
	launch = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.album_title + ' - ' + self.artist

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	file_type = models.CharField(max_length=10)
	song_title = models.CharField(max_length=250)
	length = models.CharField(max_length=100)
	is_favorite = models.BooleanField(default=False)

	def __str__(self):
		return self.song_title + ' - ' + self.length