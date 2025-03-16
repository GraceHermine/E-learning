# activitees/views.py

from django.shortcuts import render
from .models import Departement, Club, Evenement

def departement_list(request):
    departements = Departement.objects.all()
    return render(request, 'Departements.html', {'departements': departements})

def club_list(request):
    clubs = Club.objects.all()
    return render(request, 'clubs.html', {'clubs': clubs})

def evenement_list(request):
    evenements = Evenement.objects.all()
    return render(request, 'evenements.html', {'evenements': evenements})

def activite_list(request):
    departements = Departement.objects.all()
    clubs = Club.objects.all()
    evenements = Evenement.objects.all()
    return render(request, 'activite.html', {
        'departements': departements,
        'clubs': clubs,
        'evenements': evenements
    })
