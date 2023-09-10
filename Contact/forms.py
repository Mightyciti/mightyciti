from .models import PrayerRequest, Testimony
from django import forms


class PrayerRequestForm(forms.ModelForm):
    class Meta:
        model = PrayerRequest
        fields = ('Name', 'Prayer_Request', 'State')


class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = ('Name', 'Testimony', 'State', )