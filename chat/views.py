from functools import reduce

from autobahn.wamp import subscribe
from django.shortcuts import render,redirect
from .models import Message,Room
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models import Count
from django.contrib.auth import authenticate, login,logout
# Create your views here.
def index(request):
    if request.method=="POST":
        data = request.POST.get("just")
        who = request.POST.get("justwho")
        print("data",data)
        print("who",who)
        """
        if request.user.is_authenticated:
            logout(request.user)
        if not request.user.is_authenticated:
            if User.objects.filter(username=data).exists():
                user = User.objects.get(username=data)

                login(request, user)
            else:
                user = User.objects.create_user(username=data, password=data)
                login(request, user)
        """

        who=User.objects.get(username=who)

        c = [who,request.user]
        room = reduce(lambda qs, pk: qs.filter(users=pk), c, Room.objects.all()).first()

        if not room:
            room=Room()
            room.save()
            room.users.add(request.user,who)

        return redirect("room", room_name="{}".format(room.id))

    else:
        return render(request,"chat/index.html")

def room(request, room_name):
    room=Room.objects.get(id=room_name)

    messages=Message.objects.filter(room=room)
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'kimle_kim_arasinda':list(room.users.all()),
        'messagesfromdb':messages
    })


def testin(request):
    if request.method=="POST":
        print("hello")
        return render(request, "chat/test.html")
    return render(request,"chat/test.html")