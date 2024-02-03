from django.db import models
from django.conf import settings


class Disc(models.Model):

    album = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='discs')

    def __str__(self):
        return '%s - %s' % (self.artist, self.album)
