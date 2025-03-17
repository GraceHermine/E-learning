from django.shortcuts import render
from .models import EmploiDuTemps
from django.shortcuts import render
# redirect, get_object_or_404
# from django.contrib import messages
# from administration.forms.emploidutemp import EmploiDuTempsForm
# from django.contrib.auth.decorators import login_required

# Create your views here.

def HomeEnseignant(request):
    return render(request, 'Home.html')




# def emploi_du_temps_view(request):
#     emplois_du_temps = EmploiDuTemps.objects.select_related('enseignant').all()
#     # emplois_du_temps = EmploiDuTemps.objects.all()
#     jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']
#     heures = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00']
    
#     context = {
#         'jours': jours,
#         'heures': heures,
#         'emplois_du_temps': emplois_du_temps,
#     }
    
#     return render(request, 'index2.html', context)


def emploi_du_temps_view(request):
    # Get all timetables from database
    emplois = EmploiDuTemps.objects.select_related('enseignant').filter(statut=True)
    
    # Get unique values for filters
    niveaux = EmploiDuTemps.NIVEAU_CHOICES
    classes = EmploiDuTemps.CLASSE_CHOICES
    jours = EmploiDuTemps.JOURS_CHOICES
    
    # Get filter values from request
    niveau_filter = request.GET.get('niveau')
    classe_filter = request.GET.get('classe')
    jour_filter = request.GET.get('jour')
    
    # Apply filters if they exist
    if niveau_filter:
        emplois = emplois.filter(niveau=niveau_filter)
    if classe_filter:
        emplois = emplois.filter(classe=classe_filter)
    if jour_filter:
        emplois = emplois.filter(jour=jour_filter)
    
    context = {
        'emplois': emplois,
        'niveaux': niveaux,
        'classes': classes,
        'jours': jours,
        'niveau_actif': niveau_filter,
        'classe_active': classe_filter,
        'jour_actif': jour_filter,
    }
    
    # return render(request, 'administration/emploi_du_temps.html', context)
    return render(request, 'index2.html', context)

