from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('enseignanthomepage/', views.HomeEnseignant, name='enseignanthomepage'),
    path("Emplois du Temps/",views.emploi_du_temps_view, name='emploidutemps'),
    path("Home/",views.emploi_du_temps_view, name='Home'),
    path("bibliotheque/", views.bibliotheque, name="bibliotheque"),
]