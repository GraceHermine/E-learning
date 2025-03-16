from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from administration.models import EnseignantB

User = get_user_model()
class Etudiant(User):

    class Meta:
        verbose_name = "Etudiant"
        verbose_name_plural = "Etudiants"

    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    nationalite = models.CharField(max_length=50)
    matricule = models.CharField(max_length=50, unique=True)
    niveau = models.CharField(max_length=50)
    specialite = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
 

    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=False)
    last_updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.matricule 

class Forum(models.Model):

    class Meta:
        verbose_name = "Forum"
        verbose_name_plural = "Forums"

    titre = models.CharField(max_length=255)
    date_creation = models.DateField()

    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=False)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

class Reclamation(models.Model):

    class Meta:
        verbose_name = "Reclamation"
        verbose_name_plural = "Reclamations"


    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    enseignant = models.ForeignKey(EnseignantB, on_delete=models.CASCADE)
    sujet = models.CharField(max_length=255)
    description = models.TextField()
    statut = models.CharField(max_length=50, choices=[("En attente", "En attente"), ("Traité", "Traité")])

    
    created_at = models.DateTimeField(auto_now_add=False)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sujet} - {self.etudiant}"


class Cours(models.Model):
    GROUP_CHOICES = [
        ('Group 1', 'Group 1'),
        ('Group 2', 'Group 2'),
        ('Group 3', 'Group 3'),
        # Ajoutez d'autres groupes si nécessaire
    ]

    class Meta:
        verbose_name = "Cours"
        verbose_name_plural = "Cours"

    group = models.CharField(max_length=50, choices=GROUP_CHOICES)
    heures = models.PositiveIntegerField()  # Nombre d'heures
    titre = models.CharField(max_length=200)  # Titre du cours
    description = models.TextField()  # Description du cours
    credits = models.PositiveIntegerField()  # Nombre de crédits
    video_url = models.URLField(blank=True, null=True)   # Lien YouTube
    contenu = models.TextField()
    enseignant = models.ForeignKey(EnseignantB, on_delete=models.CASCADE)
    
    

    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=False)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre


class Salle(models.Model):
    nom = models.CharField(max_length=100)  # Nom de la salle
    capacite = models.PositiveIntegerField()  # Capacité de la salle
    type_salle = models.CharField(max_length=50)  # Type de la salle

    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=False)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

class Evaluation(models.Model):
    TYPE_EVALUATION_CHOICES = [
        ('Examen', 'Examen'),
        ('Devoir', 'Devoir'),
        ('Projet', 'Projet'),
        # Ajoutez d'autres types d'évaluation si nécessaire
    ]

    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)  # Lien avec le modèle Cours
    type_evaluation = models.CharField(max_length=50, choices=TYPE_EVALUATION_CHOICES)
    date = models.DateField()  # Date de l'évaluation
    duree = models.PositiveIntegerField(default=60)  # Durée de l'évaluation

    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=False)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type_evaluation} - {self.date}"

class Note(models.Model):

    enseignant = models.ForeignKey(EnseignantB, on_delete=models.CASCADE)
    cour = models.ForeignKey(Cours, on_delete=models.CASCADE)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)  # Lien avec le modèle Evaluation
    etudiant = models.CharField(max_length=100)  # Nom de l'étudiant
    
    valeur = models.DecimalField(max_digits=5, decimal_places=2)
    remarque = models.TextField(blank=True, null=True)

    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=False)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.etudiant} - {self.note}"
    


class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.user.username} at {self.created_at}"
    

    