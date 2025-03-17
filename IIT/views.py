from collections import defaultdict
from datetime import date
from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import get_object_or_404, render,redirect
from IIT.models import Cours,Forum,ChatMessage,Evaluation,Note,Reclamation, User
from administration.models import Livre
from activitees.models import Club,Evenement
from django.contrib.auth.decorators import login_required

# Create your views here.
# def error(request):

#     datas = {

#     }

#     return render(request, '404.html', datas)

# def contacts(request):

#     datas = {

#     }

#     return render(request, 'contact.html', datas)


def index(request):

    courses = Cours.objects.all()
    forums = Forum.objects.all()
    evaluations = Evaluation.objects.all()
    messages = ChatMessage.objects.filter(user=request.user)  # Messages de l'utilisateur connecté
    livres = Livre.objects.all()
    # emploi_temps = EmploiDuTemps.objects.all()
    clubs = Club.objects.all()
    evenements = Evenement.objects.all()

    datas = {
        'courses': courses,
        'forums': forums,
        'evaluations': evaluations,
        'messages': messages,
        'livres': livres,
        # 'emploi_temps': emploi_temps,
        'clubs': clubs,
        'evenements': evenements,

    }
    return render(request, 'index.html', datas)

def Studentpage(request):
    return render(request, 'StudentHome.html')

def cours(request):

    courses = Cours.objects.all().order_by('-created_at')
    datas = {
        'courses': courses,
    }
    return render(request, 'courses.html', datas)

def about(request):
    datas = {
        'active_page': 'about'  # Ajoutez cette ligne pour indiquer la page active
    }
    return render(request, 'about.html', datas)



def forum_view(request):

    forums = Forum.objects.all().order_by('-date_creation') # Récupérer tous les forums
    return render(request, 'forum.html', {'forums': forums})





@login_required
def chat_view(request):
    # Récupérer tous les utilisateurs et leur dernier message
    users = User.objects.all()
    user_messages = {
        user: ChatMessage.objects.filter(user=user).order_by('-created_at').first()
        for user in users
    }

    # Compter les messages pour chaque utilisateur
    message_counts = {
        user.id: ChatMessage.objects.filter(user=user).count()
        for user in users
    }

    # Récupérer les messages de l'utilisateur actuel
    messages = ChatMessage.objects.all().order_by('created_at')

    if request.method == "POST":
        message_text = request.POST.get("message")
        if message_text:
            ChatMessage.objects.create(user=request.user, message=message_text)
            return redirect('chat')  # Rediriger pour rafraîchir la page

    return render(request, "chat.html", {
        "messages": messages,
        "user_messages": user_messages,
        "message_counts": message_counts
    })

def evaluations_view(request):
    today = date.today()
    evaluations = Evaluation.objects.all()

    for eval in evaluations:
        if eval.date > today:
            eval.status = "À venir"
        elif eval.date == today:
            eval.status = "En cours"
        else:
            eval.status = "Terminée"

    return render(request, "about.html", {"evaluations": evaluations})


def evaluation_detail(request, eval_id):
    eval = get_object_or_404(Evaluation, id=eval_id)
    today = date.today()

    if eval.date > today:
        status_message = "Cette évaluation n'est pas encore arrivée."
    elif eval.date == today:
        status_message = "Vous pouvez réaliser cette évaluation en ligne."
        if request.method == "POST":
            # Logique pour enregistrer l'évaluation en ligne
            pass
    else:
        status_message = "La date de cette évaluation est passée."

    # Si l'évaluation est terminée, afficher la note et possibilité de réclamation
    if eval.status == "Terminée":
        note = Note.objects.filter(evaluation=eval, etudiant=request.user.username).first()
        if note:
            note_message = f"Votre note est {note.valeur}%"
            reclamation_form = Reclamation.objects.filter(etudiant=request.user, evaluation=eval)
        else:
            note_message = "Vous n'avez pas encore de note pour cette évaluation."

    return render(request, 'evaluation_detail.html', {
        'evaluation': eval,
        'status_message': status_message,
        'note_message': note_message,
        'reclamation_form': reclamation_form,
    })



def cours_view(request):
    cours_list = Cours.objects.all()

    return render(request, "courses.html", {"cours_list": cours_list})


# forummms
def forum(request):
    forums = Forum.objects.all()
    return render(request, 'forum.html', {'forums': forums})

def forum_detail(request, id):
    forum = get_object_or_404(Forum, id=id)

    # Récupérer tous les messages associés à ce forum
    messages = ChatMessage.objects.filter(forum=forum)  # Assurez-vous que la relation existe

    # Si le formulaire est soumis, ajouter un message au forum
    if request.method == "POST":
        new_message = request.POST.get('message')
        if new_message:
            # Créer un nouveau message et l'ajouter
            ChatMessage.objects.create(forum=forum, message=new_message, user=request.user)
    
    # Passer les messages existants et le forum au template
    # datas = {
    #     'forum': forum,
    #     'messages': messages,
    # }

    # return render(request, 'forums_detail.html', datas)


    messages = ChatMessage.objects.all().order_by('-created_at')
# <<<<<<< HEAD
# # <<<<<<< HEAD
# =======
# >>>>>>> f5c70310d4dff241b61767337ce98a2a0f93d3d7
    return render(request, 'chat.html', {'messages': messages})



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

# <<<<<<< HEAD
# def logout_view(request):
#     logout(request)
#     return redirect('index')


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
# =======
#     datas = {
#         'messages': messages,
#         'active_page': 'chat'  # Ajoutez cette ligne pour indiquer la page active
#     }
#     return render(request, 'chat.html', datas)
# >>>>>>> d908e0825373ee22157592428c5789a66a55e449
# =======
# >>>>>>> f5c70310d4dff241b61767337ce98a2a0f93d3d7
