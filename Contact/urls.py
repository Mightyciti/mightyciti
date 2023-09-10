from django.urls import path
from . import views


urlpatterns = [
    path('prayer_request', views.Prayer_Request.as_view(), name='prayer_request'),
    path('testimony', views.Testimony_View.as_view(), name='testimony'),
    path('testimony_accept/<int:pk>/', views.testimony_accepted, name='testimony_accept'),
    path('testimony_reject/<int:pk>/', views.testimony_rejected, name='testimony_reject'),
]