from django.urls import path
from . import views


urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('about-omo-woli', views.About_Omowoli, name='about_omowoli'),
    path('about-prophet-moses-aladeolu', views.About_Baba_Aladeolu, name='about_babaaladeolu'),
    path('about-ori-oke-aanu', views.About_Orioke_Aanu, name='about_orioke_aanu'),
]