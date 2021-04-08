from django.db.models import fields
from rest_framework import serializers
from .models import *

class songSerializer(serializers.ModelSerializer):

    class Meta:
        model = SongModel
        fields = '__all__'

class podSerializer(serializers.ModelSerializer):

    class Meta:
        model = PodcastModel
        fields = '__all__'

class audioBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = AudioBookModel
        fields = '__all__'