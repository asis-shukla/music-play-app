from django.http.response import Http404, HttpResponse, JsonResponse
from django.shortcuts import render

from music.models import Album
# Create your views here.

def index(request):
    all_albums = Album.objects.all()
    print(all_albums)
    html_response = ''
    for album in all_albums:
        url = '/music/' + str(album.id) + "/"
        html_response += '<a href="' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html_response)
   

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    
    return render(request, 'music/detail.html', {'album': album})