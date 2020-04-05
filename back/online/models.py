from django.db import models
import time
# Create your models here.
from django.contrib.auth.models import User
import asyncio
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

class UserOnline(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
            uo = UserOnline.objects.get(token=token, sid=sid, agent=agent)
        except:
            t = Token.objects.get(key=token)
            user = t.user
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

            
@receiver(models.signals.post_save, sender=UserOnline)
def set_online(sender, instance, **kwargs):
    user = instance.user
    user.is_online = True
    user.save()


@receiver(models.signals.pre_delete, sender=UserOnline)
def set_offline(sender, instance, **kwargs):
    user = instance.user
    user.is_online = False
    user.save()