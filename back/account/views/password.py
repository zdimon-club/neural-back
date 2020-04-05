import random
from django.utils.translation import ugettext_lazy as _
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema


class PasswordRequestSerializer(serializers.Serializer):
    new_password = serializers.CharField()

class PasswordResponseSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    message = serializers.CharField()


class SaveNewPasswordView(APIView):
    
    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
        operation_description="Change password.", \
        methos='post',\
        request_body=PasswordRequestSerializer, \
        responses={200: PasswordResponseSerializer} )
    def post(self, request, *args, **kwargs):
        new = request.data['new_password']
        request.user.userprofile.set_password(new)
        request.user.userprofile.save()
        return Response({'status': 0, 'message': _('Your password has been changed.')})
