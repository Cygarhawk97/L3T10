# band_website/band/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Song  # Import the Song model
from .forms import SongSubmissionForm  # Import the SongSubmissionForm form

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def songs(request):
    print("Songs view executed")
    songs = Song.objects.all()  # Query the Song model
    return render(request, 'songs.html', {'songs': songs})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def submit_song(request):
    if request.method == 'POST':
        form = SongSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.uploaded_by = request.user
            song.save()
            return redirect('songs')
    else:
        form = SongSubmissionForm()
    return render(request, 'submit_song.html', {'form': form})
