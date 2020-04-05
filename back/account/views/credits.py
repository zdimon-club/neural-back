from rest_framework.views import APIView
from rest_framework.response import Response
from account.user_serializer import ShortUserSerializer
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from core.serializers.noauthorized import NoAuthSerializer

class AddCreditResponceSerializer(serializers.Serializer):
    credits = serializers.IntegerField()


class AddCretitsView(APIView):
    """
       Add credits
    """
    @swagger_auto_schema( 
        operation_description="Logout", \
        methos='post',\
        request_body=AddCreditResponceSerializer, \
        responses={ 200: ShortUserSerializer, 401: NoAuthSerializer} )
    def post(self, request, format=None):
        pr = request.user.userprofile
        pr.add_account(int(request.data['credits']))
        return Response(ShortUserSerializer(pr).data)