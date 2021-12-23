from django.urls import path
from .views import chatroom, index

urlpatterns = [
    path('',index,name = "index"),
    path('/<str:room_name>',chatroom,name ='chatroom'),
]