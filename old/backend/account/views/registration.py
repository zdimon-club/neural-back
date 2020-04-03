from email_validator import EmailNotValidError, validate_email
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from moderation.utils.woman import add_woman_profile
from moderation.utils.agency import add_agency_profile
import random
from settings.models import MailTemplates
from account.models import UserProfile
from account.utils import send_email
from rest_framework.authtoken.models import Token
from account.user_serializer import ShortUserSerializer


class RegisterWoman(APIView):
    """
    Woman registration.

    Creating a new record with the json was taken in the Moderation model.

    moderation.utils.woman.add_woman_profile(json)

    """
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        m = add_woman_profile(request.data)
        return Response({'status': 0, 'message': 'Ok', 'id': m.id})


class RegisterAgencyView(APIView):
    """
    Agency registration.

    Creating a new record with the json was taken in the Moderation model.

    moderation.utils.agency.add_agency_profile(json)

    """
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        m = add_agency_profile(request.data)
        return Response({'status': 0, 'message': 'Ok', 'id': m.id})


class RegisterMan(APIView):
    """
    Man registration.

    Genetating random password.

    Creating record in DB (account.models.UserProfile).

    Sending email using template (MailTemplates.objects.get(alias='man-registration')).

    """
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        password = random.randint(1111, 9999)
        email = request.data.get("email")

        # Change email_template
        tpl = MailTemplates.objects.get(alias='man-registration')
        data = [
            {'name': '{password}', 'value': str(password)},
            {'name': '{username}', 'value': email}
        ]
        tpl.parse(data)
        #
        send_email(email, tpl)
        u = UserProfile()
        u.username = email
        u.email = email
        u.is_active = True
        u.set_password(password)
        u.save()
        u.publicname = 'user'+str(u.id)
        u.save()
        token, key = Token.objects.get_or_create(user=u)

        return Response({
            'status': 0, 
            'message': 'Ok', 
            'token': token.key, 
            'language': 'en', 
            'user': ShortUserSerializer(u).data})


class CheckValidEmail(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        try:
            validate_email(email)
            return Response({
                'status': 0,
                'message': 'Valid email'
            })
        except EmailNotValidError as e:
            print(str(e))
        except Exception as e:
            print(str(e))

        return Response({
            'status': 1,
            'message': 'Not valid email'
        })
