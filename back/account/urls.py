from django.urls import path, include
from rest_framework import routers
from account.views.init import InitApp
from account.views.auth import LogoutView, CustomAuthToken

urlpatterns = [

    path('init', InitApp.as_view()),
    path('login', CustomAuthToken.as_view()),
    path('logout', LogoutView.as_view()),
  
]
