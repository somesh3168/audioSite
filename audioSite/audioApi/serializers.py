from django.db.models import fields
from rest_framework import serializers
from .models import *

class songSerializer(serializers.ModelSerializer):

    class Meta:
        model = SongModel
        fields = '__all__'