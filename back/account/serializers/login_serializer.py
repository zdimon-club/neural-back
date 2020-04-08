from rest_framework import serializers
from account.user_serializer import ShortUserSerializer
from drf_yasg import openapi



username = openapi.Parameter('username', openapi.IN_FORM, description="Username", type=openapi.TYPE_STRING)
password = openapi.Parameter('password', openapi.IN_FORM, description="Password", type=openapi.TYPE_STRING)
login_pars = [username, password]


class LogoutRequestSerializer(serializers.Serializer):
    sid = serializers.CharField()

class LogoutResponseSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    message = serializers.CharField()

class LoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    
    

class LoginResponseSerializer(serializers.Serializer):
    username = serializers.CharField()
    status = serializers.IntegerField()
    user = ShortUserSerializer()




class GoogleAuthRequestSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    email = serializers.CharField()
    photoUrl = serializers.CharField()
    firstName = serializers.CharField()
    authToken = serializers.CharField()
    provider = serializers.CharField()
    socket_id = serializers.CharField()


class GoogleAuthResponceSerializer(serializers.Serializer):
    token = serializers.CharField()
    agent = serializers.CharField()
    user = ShortUserSerializer()

'''

token: "1ca5bddacdbb528ae3e6d37ffc899a647ed8f672"
agent: "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
user: {}
'''