from django.contrib import admin
from .models import UserOnline

@admin.register(UserOnline)
class UserOnlineAdmin(admin.ModelAdmin):
    list_display = ['user', 'sid', 'token', 'agent', 'activity']

