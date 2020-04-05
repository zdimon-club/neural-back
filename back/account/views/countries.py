from rest_framework.views import APIView
from rest_framework.response import Response
from django_countries.data import COUNTRIES
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers

class CounrtySerializer(serializers.Serializer):
      name = serializers.CharField()
      value = serializers.CharField()

class CountryResponceSerializer(serializers.Serializer):
    countries = CounrtySerializer(many=True)

class CountriesListView(APIView):
    """
      Countries list
    """
    permission_classes = (AllowAny,)
    @swagger_auto_schema( 
        operation_description="Countries list", \
        methos='get',\
        responses={200: CountryResponceSerializer} )
    def get(self, request, format=None):
        out = {'countries': []}
        for k in COUNTRIES:
            out['countries'].append({"name": COUNTRIES[k], "value": k})
        return Response(out)