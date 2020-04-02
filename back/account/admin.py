from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group

from account.models import UserProfile, ReplenishmentLog, ResetPasswordToken, UserProfileDoc



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'username', 
        'country', 
        'is_online', 
        'is_camera', 
        'gender', 
        'admin_icon', 
        'age', 
        'zodiac_icon',
        'birthday', 
        'is_verified', 
        'is_blocked']
    list_filter = ['is_online', 'gender']



@admin.register(ReplenishmentLog)
class ReplenishmentAdmin(admin.ModelAdmin):
    list_display = ['user_profile', 'plan', 'creation_date']


@admin.register(ResetPasswordToken)
class ResetPasswordTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', 'created_at', 'ip_address', 'user_agent')



@admin.register(UserProfileDoc)
class UserProfileDocAdmin(admin.ModelAdmin):
    list_display = ('user', 'image1', 'image2')
