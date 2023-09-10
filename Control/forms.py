from .models import Program
from django import forms
from Media.models import Audio_Message, Photo_Gallery, Video_Message


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ('Church_Name', 'Presents', 'Theme', 'Date', 'Time', 'Venue', 'Enquiry_Lines', 'Ministering', 'Program_Design')


class BulkEmail(forms.Form):
    Subject = forms.CharField(label='Subject', max_length=100)
    Message = forms.CharField(label='Message', max_length=100)

class BulkText(forms.Form):
    Subject = forms.CharField(label='Subject', max_length=100)
    Message = forms.CharField(label='Subject', max_length=100)

class ImageForm(forms.ModelForm):
    class Meta:
        model = Photo_Gallery
        fields = ('Image_File',)


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video_Message
        fields = ('Video_Title', 'embeded_link',)

class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio_Message
        fields = ('Message_Title', 'Preacher_Name', 'Music_file',)