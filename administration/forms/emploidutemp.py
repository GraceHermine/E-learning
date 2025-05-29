from django import forms
from administration.models import EmploiDuTemps

class EmploiDuTempsForm(forms.ModelForm):
    class Meta:
        model = EmploiDuTemps
        fields = ['enseignant', 'matiere', 'departement', 'niveau', 'classe', 
                 'jour', 'heure_debut', 'heure_fin']
        widgets = {
            'heure_debut': forms.TimeInput(attrs={'type': 'time'}),
            'heure_fin': forms.TimeInput(attrs={'type': 'time'}),
        }