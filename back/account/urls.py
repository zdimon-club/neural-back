from django.urls import path, include
from rest_framework import routers
from account.views.init import InitApp
from account.views.auth import LogoutView, CustomAuthToken
from account.views.myprofile import MyProfileView
from account.views.detail import AccountDetailView
from account.views.credits import AddCretitsView
from account.views.countries import CountriesListView
from account.views.password import SaveNewPasswordView
from account.views.email import CheckEmailView

urlpatterns = [

    path('init', InitApp.as_view()),
    path('login', CustomAuthToken.as_view()),
    path('logout', LogoutView.as_view()),
    path('myprofile', MyProfileView.as_view()),
    path('detail/<int:user_id>', AccountDetailView.as_view()),
    path('add/credits', AddCretitsView.as_view()),
    path('country', CountriesListView.as_view()),
    path('new/password', SaveNewPasswordView.as_view()),
    path('check/email', CheckEmailView.as_view()),

]
