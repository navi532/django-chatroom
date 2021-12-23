from django.shortcuts import redirect, render
from django.urls import reverse
# Create your views here.

def index(response):
    
    if response.POST :
        print(response.POST['room'])
        return redirect(reverse('chatroom',kwargs = {'room_name': str(response.POST['room'])}))

    return render(response,'chat/index.html',{})

def chatroom(response,room_name):
    context = {}
    context['room'] = room_name
    
    return render(response,'chat/chatroom.html',context)