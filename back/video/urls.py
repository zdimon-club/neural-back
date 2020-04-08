from django.urls import path, include
from rest_framework import routers
from video.views import VideoOnView, VideoOffView


urlpatterns = [

    path('on', VideoOnView.as_view()),
    path('off', VideoOffView.as_view()),
 
]
