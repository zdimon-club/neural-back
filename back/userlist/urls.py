from django.urls import path, include
from rest_framework import routers
from userlist.views import UserlistAllListView
from userlist.views import UserlistOnlineListView

urlpatterns = [


    path('get', UserlistAllListView.as_view()),
    path('online', UserlistOnlineListView.as_view()),
   

]


