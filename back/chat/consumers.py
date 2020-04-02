from channels.generic.websocket import WebsocketConsumer
import json
from .models import Channel
from channels.layers import get_channel_layer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from channels.auth import login, get_user
from rest_framework.authtoken.models import Token

def send_to_all_notification(message):
    print('Sendingggg')
    channel_layer = get_channel_layer()
    for c in Channel.objects.all():
        print('sending %s' % c.name)
        # await channel_layer.send(c.name, {
        #     "type": "chat.message",
        #     "text": "Hello there!",
        # })

        #group_name = 'article_{0}'.format(article_id)
        async_to_sync(channel_layer.send)(
            c.name,
            {
                'type': 'send.notification',
                'message': message
            }
        )

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print('Connnect!!!')
        print(self.channel_name)
        Channel.objects.create(name=self.channel_name)
        self.accept()
        self.send(text_data=json.dumps({
            'message': {
                'message': {
                'action': 'set:sid',
                'sid': self.channel_name
                }
            }
        }))

    def disconnect(self, close_code):
        Channel.objects.filter(name=self.channel_name).delete()
        print('DISCONNECT!!!')

    def send_notification(self, action):
        print(action)
        self.send(text_data=json.dumps({
            'message': action
        }))

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(text_data_json)
        if message['action'] == 'ping':
            print('Pinggg!!!')
        if message['action'] == 'broadcast':
            print('broadcasting')
            user = async_to_sync(get_user)(self.scope)
            print(user)
            # send_to_all_notification(message)

        if message['action'] == 'login':
            t = Token.objects.get(key=message['data']['token'])
            user = t.user
            async_to_sync(login)(self.scope, user)
            self.scope["session"].save()