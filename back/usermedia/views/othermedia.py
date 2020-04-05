from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from usermedia.models import UserMedia
from account.models import UserProfile
from usermedia.serializers import UserMediaPhotoSerializer, UserMediaVideoSerializer
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from core.serializers.badrequest import BadRequestSerializer
from core.serializers.noauthorized import NoAuthSerializer

class OtherPhotoView(generics.ListAPIView):
    '''
    Othres photo
    '''
    queryset = UserMedia.objects.all().order_by('-id')
    serializer_class = UserMediaPhotoSerializer
    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
        operation_description="Owners photo", \
        methos='get',\
        responses={200: UserMediaPhotoSerializer, 400: BadRequestSerializer, 401: NoAuthSerializer} )
    def get(self, request, user_id):
        return super().get(self, request, user_id)

    def get_queryset(self):
        try:
            pr = UserProfile.objects.get(pk=self.kwargs['user_id'])
        except Exception as e:
            
            print(e)
            raise ValidationError({'message':'User not exists!', 'status': 1})
        return UserMedia.objects.filter(user=pr,type_media='photo').order_by('-id')
    

class OtherVideoView(generics.ListAPIView):
    '''
    Othres video
    '''
    queryset = UserMedia.objects.all().order_by('-id')
    serializer_class = UserMediaVideoSerializer
    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
        operation_description="Owners video", \
        methos='get',\
        responses={200: UserMediaVideoSerializer, 400: BadRequestSerializer, 401: NoAuthSerializer} )
    def get(self, request, user_id):
        return super().get(self, request, user_id)

    def get_queryset(self):
        try:
            pr = UserProfile.objects.get(pk=self.kwargs['user_id'])
        except:
            raise ValidationError({'message':'User not exists!', 'status': 1})
        return UserMedia.objects.filter(user=pr,type_media='video').order_by('-id')

