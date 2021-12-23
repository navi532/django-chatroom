from django.shortcuts import render

# Create your views here.

def index(response):
    print(response.POST)


    return render(response,'chat/index.html',{})

def chatroom(response,room_name):
    context = {}
    context['room'] = room_name
    
    return render(response,'chat/chatroom.html',context)