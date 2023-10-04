from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from band import views as band_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('band/', include('band.urls', namespace='band')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('about/', band_views.about, name='about'),
    path('songs/', band_views.songs, name='songs'),
    path('register/', band_views.register, name='register'),
    path('', band_views.home, name='home'),  # Keep this as the last pattern
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
