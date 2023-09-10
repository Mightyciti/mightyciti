from django.urls import path
from . import views


urlpatterns = [
    path('audio', views.Audio, name='audio'),
    path('video', views.Video, name='video'),
    path('photo-gallery', views.Gallery, name='photo'),
    path('video_detail/<int:pk>/', views.video_detail, name='video_detail'),
]