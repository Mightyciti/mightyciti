from django.db import models
import datetime

class UserUpdate (models.Model):
    Name = models.CharField(max_length=50, null=True)
    Mobile_Number = models.IntegerField(null=True, blank=True)
    Mail_Address = models.EmailField(max_length=30, null=True)
    created_time = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return str(self.Mail_Address)