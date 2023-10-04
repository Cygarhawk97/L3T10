from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    title = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    description = models.TextField(default='')
    artist = models.CharField(max_length=200, default='Unknown')
    audio_file = models.FileField(upload_to='audio/', default='path/to/default_audio.mp3')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.title
