from django.db.models.expressions import F
from django.http.response import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from music.models import Album, Song
from django.core import serializers
# Create your views here.

def album_index(request):
    all_albums = Album.objects.all()
    print(all_albums)
    html_response = ''
    for album in all_albums:
        url = '/music/' + str(album.id) + "/"
        html_response += '<a href="' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html_response)

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    # try:
    #     album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Album does not exist")
    
    return render(request, 'music/detail.html', {'album': album})

def song_index(request):
    all_songs = Song.objects.all()
    return HttpResponse("This is the list of all songs")


def favourite(request, song_id):
    # postpk = request.POST['song']
    # song = get_object_or_404(Song, pk=postpk)
    # song.is_favourite = True
    # song.save()
    return HttpResponse("This is the details of one song " + str(song_id))
