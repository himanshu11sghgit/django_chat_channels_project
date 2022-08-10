from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from .models import Room, Message

# Create your views here.



@login_required
def rooms(request):
    rooms = Room.objects.all()
    context ={
        'rooms': rooms
    }

    return render(request, 'room/rooms.html', context)


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)
    context ={
        'room': room,
        'messages': messages,
    }

    return render(request, 'room/room.html', context)

