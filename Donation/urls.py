from django.urls import path
from . import views


urlpatterns = [
    path('offering', views.Offering, name='offering'),
]