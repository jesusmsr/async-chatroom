from channels.generic.websocket import AsyncWebsocketConsumer
import json
import asyncio
from asgiref.sync import sync_to_async, async_to_sync
from . import models
from channels.db import database_sync_to_async
from .classes import Player, PlayerEncoder


class ChatRoomConsumer(AsyncWebsocketConsumer):
    room_players = {}
    
    async def connect(self):
        await self.accept()
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        
        if text_data_json['joinRoom']:
            print('JOIN')
            data = text_data_json['joinRoom']
            
            room_code = data['room_code']
            
            if data['room_code'] not in self.room_players:
                self.room_players[room_code] = set()
            
            player = Player(nickname=data['nickname'])
            self.room_players[room_code].add(player)
            print('TEST')
            
            await self.channel_layer.group_add(
                data['room_code'],
                self.channel_name
            )
            
            await self.channel_layer.group_send(
                data['room_code'],
                {
                    'type': 'user_joined',
                    'user_id': data['user_id'],
                    'nickname': data['nickname'],
                    'room_code': room_code
                }
            )
        elif text_data_json['joinRoom'] == 'leaveRoom':
            # Remove the user from the specific room group
            await self.channel_layer.group_discard(
                data['room_code'],
                self.channel_name
            )
            # Send a message to the group that the user has left
            await self.channel_layer.group_send(
                data['room_code'],
                {
                    'type': 'user.left',
                    'user_id': data['user_id'],
                    'nickname': data['nickname']
                }
            )
    
    async def user_joined(self, event):
        user_id = event['user_id']
        nickname = event['nickname']
        
        room_code = event['room_code']
        room_players_list = [player.__dict__ for player in self.room_players[room_code]]
        
        await self.send(text_data=json.dumps({
            'type': 'room_entry',
            'room_name': nickname+"'s room",
            'user_id': user_id,
            'nickname': nickname,
            'players': json.dumps(room_players_list)
        }))
    
    async def user_left(self, event):
        user_id = event['user_id']
        nickname = event['nickname']
        await self.send(text_data=json.dumps({
            'type': 'room_exit',
            'user_id': user_id,
            'nickname': nickname
        }))
    
    pass
