from django.shortcuts import render
# from .models import EmploiDuTemps

# Create your views here.
def index(request):
    return render(request, 'index2.html')



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
