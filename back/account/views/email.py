from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers

class EmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

class EmailResponseSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    message = serializers.CharField()

class CheckEmailView(APIView):

    permission_classes = (AllowAny,)

    @swagger_auto_schema( 
        operation_description="Chek if email not exists", \
        methos='get',\
        responses={200: EmailResponseSerializer} )
    def post(self, request, format=None):
        email = request.data.get("email")
        try:
            User.objects.get(email=email)
            return Response({'status': 0, 'message': 'Ok not exist'})
        except:
            return Response({'status': 1, 'message': 'Email esxists!'})
