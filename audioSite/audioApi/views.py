from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .models import *
from .serializers import *
from itertools import chain

# Create your views here.

def home(request):
    return render (request, "home.html",{}) 

audiofiletype = {"song": SongModel, "audiobook": AudioBookModel, "podcast": PodcastModel}

class listAPI(ListAPIView):

    # result_list = list(chain(SongModel.objects.all(), AudioBookModel.objects.all(), PodcastModel.objects.all()))
    # print(x for x in result_list)
    queryset = SongModel.objects.all() #| AudioBookModel.objects.all()
    # queryset = result_list
    serializer_class = songSerializer


class CreateAPI(CreateAPIView):
    queryset = SongModel.objects.all()
    serializer_class = songSerializer


class UpdateAPI(UpdateAPIView):
    queryset = SongModel.objects.all()
    serializer_class = songSerializer

class DeleteAPI(DestroyAPIView):
    queryset = SongModel.objects.all()
    serializer_class = songSerializer
