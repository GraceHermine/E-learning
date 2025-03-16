# api/serializers.py

from rest_framework import serializers
from .models import Etudiant, Forum, Reclamation, Cours, Salle, Evaluation, Note

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'
    depth = 1

class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = '__all__'

class ReclamationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reclamation
        fields = '__all__'

class CoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cours
        fields = '__all__'

class SalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = '__all__'

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


from rest_framework import serializers
from .models import Etudiant

class EtudiantCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = ['id','matricule', 'nom','specialite']