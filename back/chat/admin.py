from django.contrib import admin
from .models import Chat, Channel
# Register your models here.

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'message']


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'name']