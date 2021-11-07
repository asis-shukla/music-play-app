from django.conf.urls import include
from django.urls.conf import path
from rest_framework import routers
from music import views

router = routers.DefaultRouter()
router.register(r'album', views.AlbumList, basename=None)
router.register(r'song', views.SongList, basename=None)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='music-api-auth')),
]
