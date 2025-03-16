# activitees/views.py

from django.shortcuts import render, get_object_or_404
from .models import Departement, Club, Evenement

def departement_list(request):
    departements = Departement.objects.all()
    return render(request, 'activite.html', {'departements': departements})

def club_list(request):
    clubs = Club.objects.all()
    return render(request, 'activite.html', {'clubs': clubs})

def evenement_list(request):
    evenements = Evenement.objects.all()
    return render(request, 'activite.html', {'evenements': evenements})

def activite_list(request):
    departements = Departement.objects.all()
    clubs = Club.objects.all()
    evenements = Evenement.objects.all()
    return render(request, 'activite.html', {
        'departements': departements,
        'clubs': clubs,
        'evenements': evenements
    })

def departement_detail(request, departement_id):
    departement = get_object_or_404(Departement, id=departement_id)
    return render(request, 'departement_detail.html', {'departement': departement})

def club_detail(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    return render(request, 'club_detail.html', {'club': club})

def evenement_detail(request, evenement_id):
    evenement = get_object_or_404(Evenement, id=evenement_id)
    return render(request, 'evenement_detail.html', {'evenement': evenement})
