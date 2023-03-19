from django.shortcuts import render
from rest_framework.views import APIView
from chat.serializers import RoomSerializer, PlayerSerializer
import string, random
from rest_framework.response import Response
from rest_framework import status

class RoomApiView(APIView):
    serializer_class = RoomSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = RoomSerializer(data=request.data['room'])
        
        if serializer.is_valid():
            created_room = serializer.save()
            
            serialized_room = RoomSerializer(created_room)
            
            return Response(serialized_room.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlayerApiView(APIView):
    serializer_class = PlayerSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = PlayerSerializer(data=request.data['player'])
        
        if serializer.is_valid():
            created_player = serializer.save()
            serialized_player = PlayerSerializer(created_player)
            
            return Response(serialized_player.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)