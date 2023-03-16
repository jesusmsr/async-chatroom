from django.urls import re_path
from . import consumers
from django.urls import path
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter


websocket_urlpatterns = [
    path('ws/room/<str:room_name>/', consumers.ChatRoomConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})