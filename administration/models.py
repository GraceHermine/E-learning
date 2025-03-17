from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


User = get_user_model()


# Modèle Enseignant lié à User via OneToOneField
# class Enseignant(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     nom = models.CharField(verbose_name="Nom", max_length=255)
#     matricule = models.CharField(max_length=255, unique=True)
#     departement = models.CharField(verbose_name="Département", max_length=255)
#     SPECIALITE_CHOICES = [
#         ('genie_logiciel', 'Génie Logiciel'),
#         ('reseaux_telecom', 'Réseaux Télécom'),
#         ('genie_civil', 'Génie Civil'),
#         ('ingenierie_batiment', 'Ingénierie Bâtiment'),
#         # Ajoutez d'autres spécialités ici
#     ]
#     specialite = models.CharField(max_length=50, choices=SPECIALITE_CHOICES)
#     statut = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name = "Enseignant"
#         verbose_name_plural = "Enseignants"

#     def __str__(self):
#         return self.nom

class EnseignantB(models.Model):

    class Meta:
         verbose_name = "Enseignant"
         verbose_name_plural = "Enseignants"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricule = models.CharField(max_length=255, unique=True, default='IIT-')
    nom = models.CharField(verbose_name="Nom", max_length=255)
    prenom = models.CharField(verbose_name="Prénom", max_length=255)
    email = models.EmailField(verbose_name="Email", max_length=255, default="example@email.com")
    telephone = models.CharField(verbose_name="Téléphone", max_length=255)
    GRADE_CHOICES = [
        ('assistant', 'Assistant'),
        ('maitre_assistant', 'Maître Assistant'),
        ('maitre_conference', 'Maître de Conférence'),
        ('professeur_docteur', 'Docteur'),
        ('professeur', 'Professeur'),
    ]
    grade = models.CharField(max_length=50, choices=GRADE_CHOICES)
    SPECIALITE_CHOICES = [
        ('genie_logiciel', 'Génie Logiciel'),
        ('reseaux_telecom', 'Réseaux Télécom'),
        ('genie_civil', 'Génie Civil'),
        ('ingenierie_batiment', 'Ingénierie Bâtiment'),
        # Ajoutez d'autres spécialités ici
    ]
    departement = models.CharField(max_length=50, choices=SPECIALITE_CHOICES)
#  
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.user:
            self.user = kwargs.get('request').user  # Assign the currently logged-in user
        super().save(*args, **kwargs)

    def __str__(self):
          return self.nom


# Modèle Emploi du Temps
# class EmploiDuTemps(models.Model):
#     NIVEAU_CHOICES = [
#         ('L1', 'Licence 1'),
#         ('L2', 'Licence 2'),
#         ('L3', 'Licence 3'),
#         ('M1', 'Master 1'),
#         ('M2', 'Master 2'),
#         # Ajoutez d'autres niveaux ici
#     ]

#     CLASSE_CHOICES = [
#         ('classe_a', 'Classe A'),
#         ('classe_b', 'Classe B'),
#         # Ajoutez d'autres classes ici
#     ]

#     enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name='emplois_du_temps')
#     specialite = models.CharField(max_length=50, choices=Enseignant.SPECIALITE_CHOICES)
#     niveau = models.CharField(verbose_name="Niveau", max_length=10, choices=NIVEAU_CHOICES)
#     classe = models.CharField(verbose_name="Classe", max_length=10, choices=CLASSE_CHOICES)
#     jour = models.CharField(verbose_name="Jour", max_length=50)
#     matiere = models.CharField(verbose_name="Matière", max_length=255)
#     heure_debut = models.TimeField(verbose_name="Heure de début")
#     heure_fin = models.TimeField(verbose_name="Heure de fin")
#     statut = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.enseignant.nom} - {self.jour} de {self.heure_debut} à {self.heure_fin} ({self.enseignant.specialite}, {self.niveau}, {self.classe})"

#     @property
#     def titre(self):
#         return f"Emploi du temps pour la filière {self.enseignant.specialite}, {self.niveau} - {self.classe}"

#     def __str__(self):
#         return f"{self.enseignant.nom} - {self.jour} de {self.heure_debut} à {self.heure_fin} ({self.specialite}, {self.niveau}, {self.classe})"

#     @property
#     def titre(self):
#         return f"Emploi du temps pour la filière {self.specialite}, {self.niveau} - {self.classe}"



class Livre(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    titre = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255)
    edition = models.CharField(max_length=255)
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    # bibliothecaire = models.ForeignKey(Bibliotheque, on_delete=models.CASCADE, related_name='livres')
    resume = models.TextField(verbose_name="Résumé", blank=True, null=True)
    nombre_de_page = models.IntegerField(verbose_name="Nombre de pages", blank=True, null=True)
    CATEGORIE_CHOICES = [
        ('informatique', 'Informatique'),
        ('mathematiques', 'Mathématiques'),
        ('physique', 'Physique'),
        ('chimie', 'Chimie'),
        ('biologie', 'Biologie'),
        ('litterature', 'Littérature'),
        ('histoire', 'Histoire'),
        ('geographie', 'Géographie'),
        ('philosophie', 'Philosophie'),
        ('arts', 'Arts'),
        # Ajoutez d'autres catégories ici
    ]
    categorie = models.CharField(max_length=255, choices=CATEGORIE_CHOICES, verbose_name="Catégorie", blank=True, null=True)
    date_publication = models.DateField(verbose_name="Date de publication", blank=True, null=True)
    couverture = models.ImageField(upload_to='couvertures/', verbose_name="Couverture", blank=True, null=True)

    class Meta:
        verbose_name = "Livre"
        verbose_name_plural = "Livres"

    def __str__(self):
        return self.titre


class Bibliotheque(models.Model):
    nom = models.CharField(max_length=255, verbose_name="Nom de la bibliothèque")
    responsable = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Bibliothécaire responsable")
    livres = models.ManyToManyField(Livre, related_name='bibliotheques', verbose_name="Livres")
    adresse = models.CharField(max_length=255, verbose_name="Adresse")
    telephone = models.CharField(max_length=255, verbose_name="Téléphone")
    statut = models.BooleanField(default=True, verbose_name="Active")
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Bibliothèque"
        verbose_name_plural = "Bibliothèques"

    def __str__(self):
        return self.nom

    def get_livres_disponibles(self):
        return self.livres.filter(statut=True)

    def get_livres_par_categorie(self, categorie):
        return self.livres.filter(categorie=categorie)


# Modèle Bibliothécaire
class Bibliothcaire(models.Model):
    adresse = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    statut = models.CharField(default="Personnel de l'université", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Bibliothécaire"
        verbose_name_plural = "Bibliothécaires"

    def __str__(self):
          return self.nom
    # def __str__(self):
        # return self.user.username if self.user else "Bibliothécaire sans compte"

# Modèle Livre


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

