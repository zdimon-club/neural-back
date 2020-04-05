from django.urls import path, include
from .views import *
from rest_framework import routers
from .views import GoogleView

from drf_yasg.utils import swagger_auto_schema

from account.serializers.login_serializer import GoogleAuthRequestSerializer, GoogleAuthResponceSerializer

decorated_google_login_view = \
swagger_auto_schema( \
   method='post', \
   request_body=GoogleAuthRequestSerializer, \
   responses={200: GoogleAuthResponceSerializer} \
   )(GoogleView.as_view())

urlpatterns = [
    path('google', decorated_google_login_view, name="auth-from-google"),
    
]
