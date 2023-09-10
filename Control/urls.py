from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.Control.as_view(), name='control'),
    path('pending_testimonies', views.Pending_Testimoniy.as_view(), name='pending_testimonies'),
    path('prayer_list', views.Prayers.as_view(), name='prayer_list'),
    path('add_program', views.Programs.as_view(), name='add_program'),
    path('user_email', views.user_email.as_view(), name='user_email'),
    path('user_number', views.user_number.as_view(), name='user_number'),
    path('program_detail/<int:pk>/', views.program_detail.as_view(), name='program_detail'),
    path('signin/', views.Signin, name='signin'),
    path('signout/', views.Signout, name='signout'),
    path('bulk_email', views.bulk_email.as_view(), name='bulk_email'),
    path('bulk_text', views.bulk_text.as_view(), name='bulk_text'),
    path('add_image', views.add_image.as_view(), name='add_image'),
    path('add_video', views.add_video.as_view(), name='add_video'),
    path('add_audio', views.add_audio.as_view(), name='add_audio'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)