from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


User = get_user_model()


# Modèle Enseignant lié à User via OneToOneField
class Enseignant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(verbose_name="Nom", max_length=255)
    matricule = models.CharField(max_length=255, unique=True)
    departement = models.CharField(verbose_name="Département", max_length=255)
    specialite = models.CharField(verbose_name="Spécialité", max_length=255)
    statut = models.BooleanField(default=True)  
    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name = "Enseignant"
        verbose_name_plural = "Enseignants"

    def __str__(self):
        return self.nom

# Modèle Emploi du Temps
class EmploiDuTemps(models.Model):
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name='emplois_du_temps')
    jour = models.CharField(verbose_name="Jour", max_length=50)
    heure_debut = models.TimeField(verbose_name="Heure de début")
    heure_fin = models.TimeField(verbose_name="Heure de fin")
    statut = models.BooleanField(default=True)  
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.enseignant.nom} - {self.jour} de {self.heure_debut} à {self.heure_fin}"

# Modèle Bibliothécaire lié à User
class Bibliotheque(models.Model):
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    adresse = models.CharField(max_length=255)
    
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Bibliothécaire"
        verbose_name_plural = "Bibliothécaires"

    def __str__(self):
        return self.user.username if self.user else "Bibliothécaire sans compte"

# Modèle Livre
class Livre(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    titre = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255)
    edition = models.CharField(max_length=255)
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    bibliothecaire = models.ForeignKey(Bibliotheque, on_delete=models.CASCADE, related_name='livres')

    class Meta:
        verbose_name = "Livre"
        verbose_name_plural = "Livres"

    def __str__(self):
        return self.titre

# Modèle Réservation
class Reservation(models.Model):
    date_reservation = models.DateField()
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, related_name='reservations')
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Réservation"
        verbose_name_plural = "Réservations"

    def __str__(self):
        return f"Réservation de {self.utilisateur.username} pour {self.livre.titre} le {self.date_reservation}"

# Modèle Inscription
class Inscription(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('validée', 'Validée'),
        ('refusée', 'Refusée'),
    ]

    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_inscription = models.DateField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Inscription"
        verbose_name_plural = "Inscriptions"

    def __str__(self):
        return f"{self.utilisateur.username} - {self.get_statut_display()}"

# Modèle Administrateur
class Administrateur(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, default="Administrateur")
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Administrateur"
        verbose_name_plural = "Administrateurs"

    def __str__(self):
        return f"{self.utilisateur.username} - {self.role}"
