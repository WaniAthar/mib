from django.contrib import admin
from django.urls import path, include
from mib_backend import views as home_views
from . import views
from django.conf.urls.static import static 
from django.conf import settings 



urlpatterns = [
    path('', home_views.home, name='home'),
    path('pupa', views.pupa, name='pupa'),
    path('contact', home_views.contact, name='contact'),
]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)