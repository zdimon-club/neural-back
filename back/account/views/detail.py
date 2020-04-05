
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from account.models import UserProfile
from account.user_serializer import ShortUserSerializer
from drf_yasg.utils import swagger_auto_schema

class AccountDetailView(APIView):

    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
        operation_description="Returns data about owner profile", \
        responses={200: ShortUserSerializer} )
    def get(self, request, user_id):
        profile = UserProfile.objects.get(pk=user_id)
        return Response(ShortUserSerializer(profile).data)