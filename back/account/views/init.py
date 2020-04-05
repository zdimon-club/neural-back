
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from back.settings import LANGUAGES
from account.models import UserProfile
from account.user_serializer import ShortUserSerializer
from account.serializers.init_serializer import InitSerializer
from drf_yasg.utils import swagger_auto_schema
from core.serializers.noauthorized import NoAuthSerializer

class InitApp(APIView):
    '''
    
    Initialization request.

    Runs after initialisation of the Angular app (APP_INITIALIZER) or F5.

    Returns data about authorized user. 


    '''

    permission_classes = (AllowAny,)
    @swagger_auto_schema( 
        operation_description="Returns data about authorized user", \
        responses={200: InitSerializer, 401: NoAuthSerializer} )
    def get(self, request, format=None):
        try:
            token = Token.objects.get(user=request.user)
            if request.user.userprofile.gender=='male':
                uonline = UserProfile.objects.filter(gender='female',is_online=True)
            else:
                uonline = UserProfile.objects.filter(gender='male',is_online=True)
            uo = {}
            for u in uonline:
                uo[u.id] = ShortUserSerializer(u).data
            lng = []
            for l in LANGUAGES:
                lng.append({'id': l[0], 'name': l[1]})
            return Response({
                'status': 0,
                'message': 'Ok',
                'token': token.key,
                'languges': lng,
                'user': ShortUserSerializer(request.user.userprofile).data,
                'users_online': uo,
                'online': len(uo)
                })
        except:
            return Response({'status': 1, 'message': 'no authorized!'})

