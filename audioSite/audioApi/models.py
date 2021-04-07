from django.db import models
from django.db.models.base import Model
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime
#validators
def validate_upload_time(date):
    if date.strftime("%d") < datetime.datetime.now().strftime("%d"):
        raise ValidationError("Date cannot be in the past")


# Create your models here.

class SongModel(models.Model):
    id = models.IntegerField(primary_key=True)
    song_name = models.CharField(max_length=100, blank=False, null=False)
    duration = models.PositiveIntegerField(blank=False, null=False,help_text='Enter duration in seconds')
    upload_time = models.DateTimeField(validators=[validate_upload_time],null=True, blank=True, default=None,)

    def __str__(self) -> str:
        return f'{self.song_name} : {self.duration} secs'

class PodcastModel(models.Model):
    id = models.IntegerField(primary_key=True)
    pod_name = models.CharField(max_length=100, blank=False, null=False)
    duration = models.PositiveIntegerField(blank=False, null=False, help_text='Enter duration in seconds')
    upload_time = models.DateTimeField(validators=[validate_upload_time],null=True, blank=True, default=None,)
    host = models.CharField(max_length=100, blank=False, null=False)
    # Participants = models.Li

    def __str__(self) -> str:
        return f'{self.pod_name} : {self.duration} secs'


class AudioBookModel(models.Model):
    id = models.IntegerField(primary_key=True)
    audio_book_name = models.CharField(max_length=100, blank=False, null=False)
    author_title = models.CharField(max_length=100, blank=False, null=False)
    narrator = models.CharField(max_length=100, blank=False, null=False)
    duration = models.PositiveIntegerField(blank=False, null=False, help_text='Enter duration in seconds')
    upload_time = models.DateTimeField(validators=[validate_upload_time],null=True, blank=True, default=None,)
    
    def __str__(self) -> str:
        return f'{self.audio_book_name} : {self.duration} secs'