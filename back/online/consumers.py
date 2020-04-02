from channels.generic.websocket import WebsocketConsumer
import json
from .models import UserOnline
from channels.layers import get_channel_layer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from online.models import UserOnline
from channels.auth import login
from rest_framework.authtoken.models import Token
from asgiref.sync import async_to_sync

def send_to_all_notification(message):
    print('Sendingggg')
    channel_layer = get_channel_layer()
    for c in Channel.objects.all():
        print('sending %s' % c.name)
        # await channel_layer.send(c.name, {
        #     "type": "chat.message",
        #     "text": "Hello there!",
        # })

        async_to_sync(channel_layer.send)(
            c.name,
            {
                'type': 'send.notification',
                'message': message
            }
        )

class OnlineConsumer(WebsocketConsumer):

    sid = None
    token = None
    agent = None

    def check_online(self, token, sid, agent):
        print(self.sid)
        print('check online')
        print(self.scope["user"])
        UserOnline.set_online(token,sid,agent)
        #o.save()

    def connect(self):
        print('Connnect!!! ONLINE')
        print(self.channel_name)
        self.accept()
        # UserOnline.objects.create(
        #     name=self.channel_name
        # )
        # self.accept()
        self.sid = self.channel_name
        self.send(text_data=json.dumps({
            'message': {
                'message': {
                'action': 'set:sid',
                'sid': self.channel_name
                }
            }
        }))

    def disconnect(self, close_code):
        # Channel.objects.filter(name=self.channel_name).delete()
        print('DISCONNECT!!! ONLINE')
        try:
            uo = UserOnline.objects.get(
                token=self.token, 
                sid=self.sid, 
                agent=self.agent
                )
            uo.delete()
        except:
            pass

    # def send_notification(self, action):
    #     print(action)
    #     self.send(text_data=json.dumps({
    #         'message': action
    #     }))

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        #print(text_data_json)
        if message['action'] == 'ping':
            print(message)
            self.check_online(
                message['data']['token'],
                message['data']['sid'],
                message['data']['userAgent']
                )
        if message['action'] == 'login':
            self.token = message['data']['token']
            self.agent = message['data']['userAgent']
            t = Token.objects.get(key=message['data']['token'])
            user = t.user
            async_to_sync(login)(self.scope, user)
            self.scope["session"].save()
            self.check_online(
                self.token,
                self.sid,
                self.agent
                )
           