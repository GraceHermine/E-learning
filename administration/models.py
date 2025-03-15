from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Enseignant(User):

    class Meta:
        verbose_name = "Enseignant"
        verbose_name_plural = "Enseignants"

    nom = models.CharField(verbose_name="Nom", max_length=255)
    matricule = models.CharField(max_length=255)
    departement = models.CharField(verbose_name="Département", max_length=255)
    specialite = models.CharField(verbose_name="Spécialité", max_length=255)

    
    statut = models.BooleanField(default=True)  # Ajouté
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.nom

class EmploiDuTemps(models.Model):
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name='emplois_du_temps')
    jour = models.CharField(verbose_name="Jour", max_length=50)
    heure_debut = models.TimeField(verbose_name="Heure de début")
    heure_fin = models.TimeField(verbose_name="Heure de fin")

    statut = models.BooleanField(default=True)  # Ajouté
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.enseignant.nom} - {self.jour} de {self.heure_debut} à {self.heure_fin}"



class Bibliotheque(User):

    class Meta:
        verbose_name = "Bibliothécaire"
        verbose_name_plural = "Bibliothécaires"

    adresse = models.CharField(max_length=255)

    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Livre(models.Model):

    class Meta:
        verbose_name = "Livre"
        verbose_name_plural = "Livres"

    isbn = models.CharField(max_length=13, unique=True)
    titre = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255)
    edition = models.CharField(max_length=255)

    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    bibliothecaire = models.ForeignKey(Bibliotheque, on_delete=models.CASCADE, related_name='livres')

    def __str__(self):
        return self.titre
    

class Reservation(models.Model):

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"

    date_reservation = models.DateField()

    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, related_name='reservations')
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
  

    def __str__(self):
        return f"Réservation de {self.utilisateur.username} pour {self.livre.titre} le {self.date_reservation}"
    
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    

class Inscription(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('validée', 'Validée'),
        ('refusée', 'Refusée'),
    ]

    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_inscription = models.DateField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')

    def __str__(self):
        return f"{self.utilisateur.username} - {self.get_statut_display()}"
    
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
# Administrateur
class Administrateur(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, default="Administrateur")

    def __str__(self):
        return f"{self.utilisateur.username} - {self.role}"
    
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

# Étudiant


