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

def Studentpage(request):
    return render(request, 'StudentHome.html')

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


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         matricule = request.POST['matricule']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # return redirect('index')
#             if user.matricule.startswith('EtuIIT-'):
#                 return redirect('StudentHome')
#             elif user.matricule.startswith('EnsIIT-'):
#                 return redirect('enseignanthomepage')
#             else:
#                 return redirect('index')
#         else:
#             messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
#     return render(request, 'login.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from administration.models import EnseignantB
from .models import Etudiant

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                etudiant = Etudiant.objects.get(user=user)
                if etudiant.matricule.startswith('EtuIIT-'):
                    return redirect('StudentHome')
            except Etudiant.DoesNotExist:
                pass

            try:
                enseignant = EnseignantB.objects.get(user=user)
                if enseignant.matricule.startswith('EnsIIT-'):
                    return redirect('enseignanthomepage')
            except EnseignantB.DoesNotExist:
                pass

            return redirect('index')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def logout_view(request):
    logout(request)
    return redirect('index')


#  if user is not None:
#             login(request, user)
#             if user.username.startswith('EtuIIT-'):
#                 return redirect('StudentHome')
#             elif user.username.startswith('EnsIIT-'):
#                 return redirect('ProfessorHome')
#             else:
#                 return redirect('index')
#         else:
#             messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')