from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from BiYingWallpaper.views import get_bing_wallpaper

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('bing/1920.jpg', get_bing_wallpaper, name='bing'),
]
