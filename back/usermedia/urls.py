from django.urls import path, include
from rest_framework import routers
from usermedia.views.mymedia import MyPhotoView, MyVideoView
from usermedia.views.othermedia import OtherPhotoView, OtherVideoView


urlpatterns = [

    path('my/photo', MyPhotoView.as_view()),
    path('my/video', MyVideoView.as_view()),
    path('other/photo/<int:user_id>', OtherPhotoView.as_view()),
    path('other/video/<int:user_id>', OtherVideoView.as_view()),

]
