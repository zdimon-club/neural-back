from django.shortcuts import render
from account.models import UserProfile
from account.user_serializer import ShortUserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

class UserlistAllListView(generics.ListAPIView):
    """
    API endpoint for userlist.
    """
    queryset = UserProfile.objects.all().order_by('-id')
    serializer_class = ShortUserSerializer
    permission_classes = (AllowAny,)
    
    def get_queryset(self):
        user = self.request.user.userprofile
        if user.gender == 'male':
            return UserProfile.objects.filter(gender='female')
        else:
            return UserProfile.objects.filter(gender='male')