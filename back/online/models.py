from django.db import models
import time
# Create your models here.
from django.contrib.auth.models import User
import asyncio
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
import json
from account.models import UserProfile


class UserOnline(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    username = models.CharField(max_length=250, db_index=True)
    sid = models.CharField(max_length=250, db_index=True)
    token = models.CharField(max_length=250, db_index=True, null=True)
    agent = models.CharField(max_length=250, db_index=True)
    gender = models.CharField(max_length=6, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    activity = models.IntegerField(default=0)

    @staticmethod
    def get_sids_by_user(user):
        sids = []
        for user in UserOnline.objects.filter(user=user):
            sids.append(user.sid)
        return sids
    
    @staticmethod
    def set_online(token,sid,agent):
        
        try:
            uo = UserOnline.objects.get(token=token, sid=sid)
        except:
            t = Token.objects.get(key=token)
            user = t.user.userprofile
            uo = UserOnline()
            uo.username = user.username
            uo.user = user
            uo.sid = sid
            uo.token = token
            uo.agent = agent 
            uo.gender = user.userprofile.gender
        uo.save() 

    def save(self, *args, **kwargs):
        self.activity = time.time()
        super(UserOnline, self).save(*args, **kwargs)

from account.user_serializer import ShortUserSerializer    
from channels.layers import get_channel_layer 
from asgiref.sync import async_to_sync        
channel_layer = get_channel_layer()

@receiver(models.signals.pre_save, sender=UserOnline)
def set_online(sender, instance, **kwargs):

    if not instance.pk:
        print('Creating UserOnline!')
        profile = instance.user
        profile.set_online()
        if profile.gender == 'male':
            group = 'online_male'
        else:
            group = 'online_female'
        async_to_sync(channel_layer.group_send)(group, { \
            "type": "online.on", \
            "message": json.dumps( {
                "type": "online:online.on", \
                "payload": ShortUserSerializer(profile).data
            }) \
        })
        # async_to_sync(channel_layer.group_send)("admin", { \
        #     "type": "online.on", \
        #     "message": json.dumps( {
        #         "type": "admin:online.on", \
        #         "payload": ShortUserSerializer(instance.user.userprofile).data
        #     }) \
        # })

    user = instance.user
    user.is_online = True
    user.save()


@receiver(models.signals.pre_delete, sender=UserOnline)
def set_offline(sender, instance, **kwargs):
    print('Deleting UserOnline!')
    profile = instance.user
    profile.set_offline()
    if profile.gender == 'male':
        group = 'online_male'
    else:
        group = 'online_female'
    async_to_sync(channel_layer.group_send)(group, { \
        "type": "online.off", \
        "message": json.dumps( {
            "type": "online:online.off", \
            "payload": ShortUserSerializer(instance.user.userprofile).data
        }) \
    })
    user = instance.user
    user.is_online = False
    user.save()