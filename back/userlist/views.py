from django.shortcuts import render
from account.models import UserProfile
from online.models import UserOnline
from account.user_serializer import ShortUserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny


class UserlistOnlineListView(generics.ListAPIView):
    queryset = UserProfile.objects.filter(is_online=True).order_by('-id')
    serializer_class = ShortUserSerializer
    permission_classes = (AllowAny,)


class UserlistAllListView(generics.ListAPIView):
    """
    API endpoint for userlist.
    """
    queryset = UserProfile.objects.all().order_by('-id')
    serializer_class = ShortUserSerializer
    permission_classes = (AllowAny,)
    
    def get_queryset(self):
        try:
            user = self.request.user.userprofile
            if user.gender == 'male':
                return UserProfile.objects.filter(gender='female').exclude(user=user)
            else: 
                return UserProfile.objects.filter(gender='male').exclude(user=user)
        except:
            return UserProfile.objects.filter(gender='female')
