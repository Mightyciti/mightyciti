from django.db import models
import datetime

class Program (models.Model):
    Church_Name = models.CharField(max_length=100, null=True)
    Presents = models.CharField(max_length=50, null=True)
    Theme = models.CharField(max_length=800, null=True)
    Date = models.CharField(max_length=70, null=True)
    Time = models.CharField(max_length=70, null=True)
    Venue = models.CharField(max_length=150, null=True)
    Enquiry_Lines = models.CharField(max_length=100, null=True)
    Ministering = models.CharField(max_length=200, null=True)
    Program_Design = models.ImageField(upload_to='task_upload', null=True, blank=True)
    created_time = models.DateTimeField(default=datetime.datetime.now())

