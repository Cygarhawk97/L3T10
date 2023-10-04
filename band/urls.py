from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'band'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('songs/', views.songs, name='songs'),
    path('register/', views.register, name='register'),
    path('submit-song/', views.submit_song, name='submit_song'),
]
