from channels.generic.websocket import WebsocketConsumer
import json
from .models import Channel
from channels.layers import get_channel_layer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync

def send_to_all_notification():
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
                
            }
        )

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print('Connnect!!!')
        print(self.channel_name)
        Channel.objects.create(name=self.channel_name)
        self.accept()

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
        print(message)
        send_to_all_notification()

        # self.send(text_data=json.dumps({
        #     'message': message
        # }))