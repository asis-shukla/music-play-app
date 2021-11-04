from django.conf.urls import include
from django.urls.conf import path
from rest_framework import routers
from music import views

router = routers.DefaultRouter()
router.register(r'album', views.AlbumList, basename=None)

urlpatterns = [
    path('', include(router.urls)),
    path("song/", view=views.SongList.as_view(), name="song"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path("album/<int:album_id>/", view=views.DetailView.as_view(), name="detail"),
    # path("song/<int:song_id>/", view=views.favourite, name="favourite")
]
