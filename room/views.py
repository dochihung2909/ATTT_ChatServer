from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room, Message

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    for message in messages:
        from cipher.scrypto import vigenere_decrypt
        from djangochat import settings
        message.content = vigenere_decrypt(message.content, settings.DB_CHAT_SECRET_KEY)

    return render(request, 'room/room.html', {'room': room, 'messages': messages})