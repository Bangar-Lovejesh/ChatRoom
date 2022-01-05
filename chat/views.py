from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Room, Messages
# Create your views here.

def index(request):
    return render(request,'index.html')

def room(request, room):
    username = request.GET.get('username')
    roomInfo  = Room.objects.get(name=room)
    context = {
        'username' : username,
        'room' :room,
        'roomInfo' : roomInfo
    }
    return render(request,'chatRoom.html',context)

def checkview(request):
    room = request.POST.get('roomName', '')
    username = request.POST.get('username', '')

    if Room.objects.filter(name = room).exists():
        return(redirect('/'+room+'/?username='+username))
    else:
        newRoom = Room.objects.create(name=room)
        newRoom.save()
        return(redirect('/'+room+'/?username='+username))
    
def send(request):
    message = request.POST.get('message','')
    username = request.POST.get('username','')
    roomId = request.POST.get('roomId','')

    newMessage = Messages.objects.create(message = message, user = username, roomName = roomId )

    newMessage.save()

    return HttpResponse('Message sent successfully')


def getMessages(request, room):
    roomDetails = Room.objects.get(name = room)
    messages = Messages.objects.filter(roomName = roomDetails.id)
    return JsonResponse({"messages":list(messages.values())})