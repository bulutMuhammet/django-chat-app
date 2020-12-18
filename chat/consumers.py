# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import get_object_or_404

from .models import Message,User,Room

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        print("connect")
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        print("disconnect")
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        print("receive")
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        yeter = text_data_json['yeter']
        #print(yeter)

        user = self.scope["user"]



        room=Room.objects.get(id=self.room_name)
        auth = get_object_or_404(User, username=user)
        m=Message.objects.create(content=message, user=auth,room=room)
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user':user.username,
                'tarih':m.timestamp.strftime("%H:%M")
            }
        )


    # Receive message from room group
    def chat_message(self, event):
        print("chat_message")
        message = event['message']
        username=event['user']
        tarih=event["tarih"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'username':username,
            'tarih':tarih
        }))