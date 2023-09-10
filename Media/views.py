from django.shortcuts import render
from .models import Audio_Message, Photo_Gallery, Video_Message
from django.core.paginator import Paginator

def Audio(request):
    audio = Audio_Message.objects.all().order_by('-created_time')

    page_number = request.GET.get('page')
    paginator = Paginator(audio, 10)
    audio = paginator.get_page(page_number)
    return render (request, 'Media/audio.html', {'audio': audio})

def Video(request):
    video = Video_Message.objects.all().order_by('-created_time')

    page_number = request.GET.get('page')
    paginator = Paginator(video, 12)
    video = paginator.get_page(page_number)
    return render (request, 'Media/video.html', {'video': video})

def Gallery(request):
    gallery = Photo_Gallery.objects.all().order_by('-created_time')

    page_number = request.GET.get('page')
    paginator = Paginator(gallery, 10)
    gallery = paginator.get_page(page_number)
    return render (request, 'Media/gallery.html', {'gallery': gallery})

def video_detail(request, pk):
    video = Video_Message.objects.get(id=pk)
    others = Video_Message.objects.all()
    return render (request, 'Media/video_detail.html', {'video': video, 'others' : others})
    

