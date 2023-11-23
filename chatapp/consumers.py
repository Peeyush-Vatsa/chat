import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from chatapp.models import Message


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # connection has to be accepted
        self.room_group_name = "chat_room"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        name = text_data_json["name"]

        Message.objects.create(name=name, message=message)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {"type": "chat_message", "message": message, "name": name},
        )

    def chat_message(self, event):
        messsage = event["message"]
        name = event["name"]

        self.send(
            text_data=json.dumps({"type": "chat", "message": messsage, "name": name})
        )
