from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from itertools import chain
from django.http import Http404
from rest_framework import status
from rest_framework.exceptions import NotFound

# Create your views here.


def home(request):
    return render(request, "home.html", {})


# audiofiletype = {"song": SongModel, "audiobook": AudioBookModel, "podcast": PodcastModel}


class listAPI(APIView):
    def get(self, request, audioFileType, audioFileID=None):

        if audioFileType == "song":
            if audioFileID is not None:
                Song = SongModel.objects.filter(id=audioFileID)
            elif audioFileID == None:
                Song = SongModel.objects.all()
            elif SongModel.DoesNotExist:
                serializer = {"404": "not found"}
            serializer = songSerializer(Song, many=True)

        elif audioFileType == "podcast":
            if audioFileID is not None:
                Pod = PodcastModel.objects.filter(id=audioFileID)
            elif audioFileID == None:
                Pod = PodcastModel.objects.all()
            serializer = podSerializer(Pod, many=True)
        elif audioFileType == "audiobook":
            if audioFileID is not None:
                Abook = AudioBookModel.objects.filter(id=audioFileID)
            elif audioFileID == None:
                Abook = AudioBookModel.objects.all()
            serializer = audioBookSerializer(Abook, many=True)
        return Response(serializer.data)

    def post(self, request, audioFileType, audioFileID=None):
        if audioFileType == "song":
            serializer = songSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        elif audioFileType == "podcast":
            serializer = podSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        elif audioFileType == "audiobook":
            serializer = audioBookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DelUpdateAPI(APIView):
    def get_object(self, audioFileType=None, audioFileID=None):
        MODEL = None
        try:
            if audioFileType == "song":
                MODEL = SongModel
                return SongModel.objects.get(id=audioFileID)
            elif audioFileType == "podcast":
                MODEL = PodcastModel
                return PodcastModel.objects.get(pk=audioFileID)
            elif audioFileType == "audiobook":
                MODEL = AudioBookModel
                return AudioBookModel.objects.get(pk=audioFileID)

        except Exception as e:
            print(e)
            raise Http404

    def put(self, request, audioFileType=None, audioFileID=None, format=None):
        if audioFileType == "song":
            Song = self.get_object(audioFileID)
            serializer = songSerializer(Song, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

        elif audioFileType == "podcast":

            serializer = podSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

        elif audioFileType == "audiobook":
            serializer = audioBookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, audioFileType=None, audioFileID=None, format=None):

        if audioFileType == "song":
            Song = self.get_object(audioFileID)
            Song.delete()
        elif audioFileType == "podcast":
            Pod = self.get_object(audioFileID)
            Pod.delete()
        elif audioFileType == "audiobook":
            AudioBook = self.get_object(audioFileID)
            print(AudioBook)
            AudioBook.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)