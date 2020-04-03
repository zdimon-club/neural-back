from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path

# custom consumers
from online.consumers import OnlineConsumer
from chat.consumers import ChatConsumer


websocket_urlpatterns = [
    re_path(r'chat/$', ChatConsumer),
    re_path(r'online/$', OnlineConsumer),
]

application = ProtocolTypeRouter({
    
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),    

})