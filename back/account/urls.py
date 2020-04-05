from django.urls import path, include
from rest_framework import routers
from account.views.init import InitApp
from account.views.auth import LogoutView, CustomAuthToken
from account.views.myprofile import MyProfileView
from account.views.detail import AccountDetailView

urlpatterns = [

    path('init', InitApp.as_view()),
    path('login', CustomAuthToken.as_view()),
    path('logout', LogoutView.as_view()),
    path('myprofile', MyProfileView.as_view()),
    path('detail/<int:user_id>', AccountDetailView.as_view()),
  
]
