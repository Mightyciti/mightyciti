from django.db import models
import datetime

class Testimony(models.Model):
    STATE = [
        ('Abuja', 'Abuja'),
        ('Abia', 'Abia'),
        ('Adamawa', 'Adamawa'),
        ('Akwa Ibom', 'Akwa Ibom'),
        ('Anambra', 'Anambra'),
        ('Bauchi', 'Bauchi'),
        ('Bayelsa', 'Bayelsa'),
        ('Benue', 'Benue'),
        ('Borno', 'Borno'),
        ('Cross River', 'Cross River'),
        ('Delta', 'Delta'),
        ('Ebonyi', 'Ebonyi'),
        ('Edo', 'Edo'),
        ('Ekiti', 'Ekiti'),
        ('Enugu', 'Enugu'),
        ('Gombe', 'Gombe'),
        ('Imo', 'Imo'),
        ('Jigawa', 'Jigawa'),
        ('Kaduna', 'Kaduna'),
        ('Kano', 'Kano'),
        ('Katsina', 'Katsina'),
        ('Kebbi', 'Kebbi'),
        ('Kogi', 'Kogi'),
        ('Kwara', 'Kwara'),
        ('Lagos', 'Lagos'),
        ('Nassarawa', 'Nassarawa'),
        ('Niger', 'Niger'),
        ('Ogun', 'Ogun'),
        ('Ondo', 'Ondo'),
        ('Osun', 'Osun'),
        ('Oyo', 'Oyo'),
        ('Plateau', 'Plateau'),
        ('Rivers', 'Rivers'),
        ('Sokoto', 'Sokoto'),
        ('Taraba', 'Taraba'),
        ('Yobe', 'Yobe'),
        ('Zamfara', 'Zamfara'),
    ]
    Name = models.CharField(max_length=50)
    State = models.CharField(max_length=20, choices=STATE)
    Testimony = models.TextField(null=True)
    Approved = models.BooleanField(default=False, null=True)
    created_time = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return str(self.Name)




class PrayerRequest(models.Model):
    STATE = [
        ('Abuja', 'Abuja'),
        ('Abia', 'Abia'),
        ('Adamawa', 'Adamawa'),
        ('Akwa Ibom', 'Akwa Ibom'),
        ('Anambra', 'Anambra'),
        ('Bauchi', 'Bauchi'),
        ('Bayelsa', 'Bayelsa'),
        ('Benue', 'Benue'),
        ('Borno', 'Borno'),
        ('Cross River', 'Cross River'),
        ('Delta', 'Delta'),
        ('Ebonyi', 'Ebonyi'),
        ('Edo', 'Edo'),
        ('Ekiti', 'Ekiti'),
        ('Enugu', 'Enugu'),
        ('Gombe', 'Gombe'),
        ('Imo', 'Imo'),
        ('Jigawa', 'Jigawa'),
        ('Kaduna', 'Kaduna'),
        ('Kano', 'Kano'),
        ('Katsina', 'Katsina'),
        ('Kebbi', 'Kebbi'),
        ('Kogi', 'Kogi'),
        ('Kwara', 'Kwara'),
        ('Lagos', 'Lagos'),
        ('Nassarawa', 'Nassarawa'),
        ('Niger', 'Niger'),
        ('Ogun', 'Ogun'),
        ('Ondo', 'Ondo'),
        ('Osun', 'Osun'),
        ('Oyo', 'Oyo'),
        ('Plateau', 'Plateau'),
        ('Rivers', 'Rivers'),
        ('Sokoto', 'Sokoto'),
        ('Taraba', 'Taraba'),
        ('Yobe', 'Yobe'),
        ('Zamfara', 'Zamfara'),
    ]
    Name = models.CharField(max_length=50)
    State = models.CharField(max_length=20, choices=STATE)
    Prayer_Request = models.TextField(null=True)
    created_time = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return str(self.Name)