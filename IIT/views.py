from datetime import date
from django.db import models
from django.shortcuts import get_object_or_404, render,redirect
from IIT.models import Cours,Forum,ChatMessage,Evaluation,Note,Reclamation

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
    courses = Cours.objects.all()
    forums = Forum.objects.all()
    evaluations = Evaluation.objects.all()
    messages = ChatMessage.objects.filter(user=request.user)  # Messages de l'utilisateur connecté

    datas = {
        'courses': courses,
        'forums': forums,
        'evaluations': evaluations,
        'messages': messages,
    }
    return render(request, 'index.html', datas)

def cours(request):
    courses = Cours.objects.all().order_by('-created_at')
    datas = {
        'courses': courses,
    }

    return render(request, 'courses.html', datas)


def about(request):

    datas = {

    }

    return render(request, 'about.html', datas)

def forum_view(request):
    forums = Forum.objects.all().order_by('-date_creation') # Récupérer tous les forums
    return render(request, 'forum.html', {'forums': forums})


def chat_view(request):
    if request.method == "POST":
        message_content = request.POST.get("message")
        if message_content:
            ChatMessage.objects.create(user=request.user, message=message_content)
        return redirect('chat')

    messages = ChatMessage.objects.all().order_by('-created_at')
    return render(request, 'chat.html', {'messages': messages})

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
