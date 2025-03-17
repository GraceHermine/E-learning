from django.shortcuts import render, redirect, get_object_or_404
from .models import Livre, Reservation
from django.contrib.auth.decorators import login_required

# Vue pour afficher la bibliothèque
def bibliotheque(request):
    livres = Livre.objects.all()  # Récupère tous les livres dans la bibliothèque
    return render(request, 'bibliotheque.html', {'livres': livres})

# Vue pour afficher les détails d'un livre
def livre(request, livre_id):
    livre = get_object_or_404(Livre, id=livre_id)  # Récupère un livre spécifique
    return render(request, 'livre.html', {'livre': livre})

# Vue pour la réservation d'un livre
@login_required
def reserver(request, livre_id):
    livre = get_object_or_404(Livre, id=livre_id)  # Récupère le livre par son ID
    reservation, created = Reservation.objects.get_or_create(user=request.user, livre=livre)
    if created:
        reservation.statut = "En attente"  # Définit le statut de la réservation à "En attente"
        reservation.save()
        return render(request, 'reservation.html', {'reservation': reservation})
    else:
        # Si la réservation existe déjà, afficher une confirmation
        return render(request, 'reservation.html', {'reservation': reservation})

# Vue pour afficher les réservations de l'utilisateur
@login_required
def mes_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)  # Récupère les réservations de l'utilisateur connecté
    return render(request, 'reservation.html', {'reservations': reservations})
