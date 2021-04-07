from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(SongModel)
admin.site.register(PodcastModel)
admin.site.register(AudioBookModel)