from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from core.serializers.common import CommonSerializer
from core.serializers.noauthorized import NoAuthSerializer

class VideoOnView(APIView):
    '''
    LogouTurn the video on.
    '''
    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
        methos='get', \
        responses={200: CommonSerializer, 401: NoAuthSerializer} )
    def get(self, request):
        return Response({'status': 0, 'message': 'Ok'})


class VideoOffView(APIView):
    '''
    LogouTurn the video on.
    '''
    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
        methos='get', \
        responses={200: CommonSerializer, 401: NoAuthSerializer} )
    def get(self, request):
        return Response({'status': 0, 'message': 'Ok'})
