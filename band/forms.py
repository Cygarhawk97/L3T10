# band/forms.py
from django import forms
from .models import Song

class SongSubmissionForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'album', 'release_date', 'genre', 'description', 'artist', 'audio_file']
