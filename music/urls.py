from django.urls.conf import path

from music import views

urlpatterns = [
    path('album/', view=views.AlbumList.as_view(), name="index"),
    path("song/", view=views.SongList.as_view(), name="song"),
    # path("album/<int:album_id>/", view=views.DetailView.as_view(), name="detail"),
    # path("song/<int:song_id>/", view=views.favourite, name="favourite")
]
