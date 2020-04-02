from rest_framework.views import APIView
from rest_framework.response import Response
from payment.tasks import update_account_service
from account.user_serializer import ShortUserSerializer

class AddCretitsView(APIView):
    """
       Add credits
    """
    def post(self, request, format=None):
        pr = request.user.userprofile
        pr.account = pr.account + int(request.data['credits'])
        pr.save()
        update_account_service(pr)
        return Response(ShortUserSerializer(pr).data)