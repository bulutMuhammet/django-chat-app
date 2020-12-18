#Coding by Muhammet Bulut - CEO of Pencil Pie
from django.contrib import admin
from .models import Message,Room
#
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):

    list_display = ["content","timestamp"]


    class Meta:
        model = Message
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = ["id"]


    class Meta:
        model = Room