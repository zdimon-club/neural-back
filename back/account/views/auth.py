from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
#from online.utils import set_user_offline, set_user_online
from django.utils.translation import ugettext_lazy as _
from logsys.mixins.db_log import DatabaseLogMixin
from logsys.mixins.ip_tracking_log import IpTrackingLog
from account.user_serializer import ShortUserSerializer
from rest_framework import serializers


class LogoutView(DatabaseLogMixin, APIView):
    '''
    Logout.
    '''
    permission_classes = (AllowAny,)
    log_type = 'logout'

    def get(self, request):
        if request.user.is_authenticated:
            token, created = Token.objects.get_or_create(user=request.user)
            set_user_offline({'token': token, 'user': request.user.userprofile})
        else:
            print("User is not authenticated!")
        return Response({'status': 0, 'message': 'Ok'})

# , ObtainAuthToken
class CustomAuthToken(ObtainAuthToken):
    '''
        Login endpoint.

        POST (body json)

        @param: username:str

        @param: password:str

        Checking out login and password and setting user online.
    '''
    log_type = 'login'

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        profile = user.userprofile
        # is blocked
        if profile.is_blocked:
            return Response({
                'status': 1, 
                'user': ShortUserSerializer(profile).data,
                'message': _('Your account is blocked!')   
            })        
        profile.set_online()
        # import pdb; pdb.set_trace()
        token, created = Token.objects.get_or_create(user=user)
        groups = []
        for g in profile.groups.all():
            groups.append(g.name)
        data = {
            'token': token.key,
            'language': profile.language,
            'agent': request.META['HTTP_USER_AGENT'],
            'user': ShortUserSerializer(profile).data,
            'groups': groups
        }
        
        return Response(data)
