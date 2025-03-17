from django.db import models
from django.shortcuts import render,redirect
from IIT.models import Cours,Forum,ChatMessage

# Create your views here.
def error(request):

    datas = {

    }

    return render(request, '404.html', datas)

def contacts(request):

    datas = {

    }

    return render(request, 'contact.html', datas)


def index(request):
    courses = Cours.objects.all()  # Si tu veux récupérer tous les cours
   

    datas = {
        'courses': courses,
        
    }
    return render(request, 'index.html', datas)

def cours(request):

    datas = {

    }

    return render(request, 'courses.html', datas)


def about(request):

    datas = {

    }

    return render(request, 'about.html', datas)

def forum_view(request):
    forums = Forum.objects.all()  # Récupérer tous les forums
    return render(request, 'forum.html', {'forums': forums})


def chat_view(request):
    if request.method == "POST":
        message_content = request.POST.get("message")
        if message_content:
            # Créer un nouveau message dans la base de données
            ChatMessage.objects.create(user=request.user, message=message_content)
        return redirect('chat')  # Redirige vers la même page après envoi du message

    messages = ChatMessage.objects.all().order_by('-created_at')
    return render(request, 'chat.html', {'messages': messages})