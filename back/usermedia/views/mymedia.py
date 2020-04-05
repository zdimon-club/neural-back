from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from usermedia.models import UserMedia
from usermedia.serializers import UserMediaPhotoSerializer, UserMediaVideoSerializer
from rest_framework import generics


class MyPhotoView(generics.ListAPIView):
    '''
    Owners photo
    '''
    queryset = UserMedia.objects.all().order_by('-id')
    serializer_class = UserMediaPhotoSerializer
    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
        operation_description="Owners photo", \
        methos='get',\
        responses={200: UserMediaPhotoSerializer} )
    def get_queryset(self):
        pr = self.request.user.userprofile
        return UserMedia.objects.filter(user=pr,type_media='photo').order_by('-id')
    

class MyVideoView(generics.ListAPIView):
    queryset = UserMedia.objects.all().order_by('-id')
    serializer_class = UserMediaVideoSerializer
    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
        operation_description="Owners video", \
        methos='get',\
        responses={200: UserMediaVideoSerializer} )
    def get_queryset(self):
        pr = self.request.user.userprofile
        return UserMedia.objects.filter(user=pr,type_media='video').order_by('-id')

