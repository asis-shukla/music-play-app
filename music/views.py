from rest_framework import viewsets
from .models import Album, Song
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AlbumSerializers, SongSerializers

class AlbumList(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializers
    # def get(self, request):
    #     albums = Album.objects.all()
    #     serializer = AlbumSerializers(albums, many=True)
    #     return Response(serializer.data)
        
    
    # def post(self):
    #     pass


class SongList(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializers