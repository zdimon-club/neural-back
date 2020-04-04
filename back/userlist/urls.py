from django.urls import path, include
from rest_framework import routers
from userlist.views import UserlistAllListView

urlpatterns = [


    path('get', UserlistAllListView.as_view(),name='media-change-role'),
   

]


