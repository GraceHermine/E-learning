from django.urls import path
from . import views

urlpatterns = [
    path("bibliotheque/", views.bibliotheque, name="bibliotheque"),
    path('livre/', views.livre, name='livre'),  # Afficher les détails d'un livre
    path('reservation/', views.reserver, name='reserver'),  # Réserver un livre
    path('mes_reservations/', views.mes_reservations, name='mes_reservations'),  # Voir mes réservations
]
