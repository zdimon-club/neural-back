
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from back.settings import LANGUAGES
from account.models import UserProfile
from account.user_serializer import ShortUserSerializer

class InitApp(APIView):
    '''
    
    Initialization request.

    Runs after initialisation of the Angular app (APP_INITIALIZER) or F5.

    Returns data about authorized user. 
    
    Responce 

    {
        status: 0
        message: "Ok"
        token: "58d52f5c65e705866e266af6897c9458d5a95770"
        languges: [{id: "ru", name: "Russian"}, {id: "en", name: "English"}]
        user: {country_string: "Ukraine", is_subscribed: false, id: 206, username: "", last_name: "",…}
        users_online: {}
        online: 0
    }

    '''

    permission_classes = (AllowAny,)

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

