from django.urls.conf import path

from music import views

urlpatterns = [
    path('album/', view=views.album_index, name="index"),
    path("album/<int:album_id>/", view=views.detail, name="detail"),
    path("song/", view=views.song_index, name="song"),
    path("song/<int:song_id>/", view=views.favourite, name="favourite")
]
