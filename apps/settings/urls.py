from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('about', about, name="about"),
    path('contact/', contact, name="contact"),
    path('send_data/', send_data, name="send_data"),
]