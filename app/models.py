from django.db import models
from django.conf import settings
from users.models import User


class Disc(models.Model):

    album = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='discs')

    def __str__(self):
        return '%s - %s' % (self.artist, self.album)


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    username = models.CharField(max_length=255, blank=True, default='')
    avatar = models.ImageField(upload_to='images')

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.user.email.split('@')[0]
        super().save(*args, **kwargs)

# Create your models here.
