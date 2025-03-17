# activitees/urls.py

from django.urls import path
from .views import departement_list, club_list, evenement_list, activite_list, departement_detail, club_detail, evenement_detail

urlpatterns = [
    path('departements/', departement_list, name='departement_list'),
    path('clubs/', club_list, name='club_list'),
    path('evenements/', evenement_list, name='evenement_list'),
    path('activite/', activite_list, name='activite'),
    path('departement/<int:departement_id>/', departement_detail, name='departement_detail'),
    path('club/<int:club_id>/', club_detail, name='club_detail'),
    path('evenement/<int:evenement_id>/', evenement_detail, name='evenement_detail'),
]
