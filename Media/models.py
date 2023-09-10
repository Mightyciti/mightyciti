from django.db import models
import datetime

class Audio_Message(models.Model):
    Message_Title = models.CharField(max_length=150, null=True)
    Preacher_Name = models.CharField(max_length=150, null=True)
    Music_file = models.FileField(upload_to='audio_messages/')
    created_time = models.DateTimeField(default=datetime.datetime.now())


class Photo_Gallery(models.Model):
    Image_File = models.ImageField(upload_to='photo_gallery', null=True)
    created_time = models.DateTimeField(default=datetime.datetime.now())


class Video_Message(models.Model):
    Video_Title = models.CharField(max_length=150, null=True)
    embeded_link = models.CharField(max_length=200, null=True)
    created_time = models.DateTimeField(default=datetime.datetime.now())