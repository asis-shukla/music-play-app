from django.urls.conf import path

from music import views


urlpatterns = [
    path('', view=views.index, name="index"),
    path("<int:album_id>/", view=views.detail, name="detail")
]
