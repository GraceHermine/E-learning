# activitees/urls.py

from django.urls import path
from activitees.views import departement_list,club_list,evenement_list,activite_list

urlpatterns = [
    path('activite/', activite_list, name='activite'), 
    path('departements/', departement_list, name='departement_list'),
    path('clubs/',club_list, name='club_list'),
    path('evenements/', evenement_list, name='evenement_list'),
]
