from django.shortcuts import render
from .models import Message
from .models import Chat


def index(request):
    if request.method == "POST":
        myChat = Chat.objects.get(id=1)
        Message.objects.create(
            text=request.POST["textmessage"],
            chat=myChat,
            author=request.user,
            receiver=request.user,
        )
        print(request.POST["textmessage"])
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, "chat/index.html", {"messages": chatMessages})
