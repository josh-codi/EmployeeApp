"""InternProject URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('EmployeeApp.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')) #For the the login
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)