from django.contrib.auth import get_user_model
from django.db import models
import uuid

User = get_user_model()

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    users = models.ManyToManyField(User, related_name="rooms",blank=True) #(1)



class Message(models.Model):
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE,blank=True,null=True)

    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


