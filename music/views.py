from django.http.response import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Album, Song
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AlbumSerializers, SongSerializers
# Create your views here.

class AlbumList(APIView):
    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumSerializers(albums, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass


class SongList(APIView):
    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializers(songs, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass
    

#     elif request.method == 'POST': # user posting data
#         serializer = CountrySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save() # save to db
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)