from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('about/', include('About.urls')),
    path('donation/', include('Donation.urls')),
    path('media/', include('Media.urls')),
    path('contact/', include('Contact.urls')),
    path('control/', include('Control.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
