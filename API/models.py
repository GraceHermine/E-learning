from django.db import models

class Etudiant(models.Model):
    matricule = models.CharField(max_length=50, unique=True)
    nom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.matricule

class Forum(models.Model):
    titre = models.CharField(max_length=255)
    date_creation = models.DateField()
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=False)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

class Reclamation(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    sujet = models.CharField(max_length=255)
    description = models.TextField()
    statut = models.CharField(max_length=50, choices=[("En attente", "En attente"), ("Traité", "Traité")])
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sujet} - {self.etudiant}"

class Cours(models.Model):
    GROUP_CHOICES = [
        ('Group 1', 'Group 1'),
        ('Group 2', 'Group 2'),
        ('Group 3', 'Group 3'),
    ]

    group = models.CharField(max_length=50, choices=GROUP_CHOICES)
    heures = models.PositiveIntegerField()
    titre = models.CharField(max_length=200)
    description = models.TextField()
    credits = models.PositiveIntegerField()
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

class Cours(models.Model):
    GROUP_CHOICES = [
        ('Group 1', 'Group 1'),
        ('Group 2', 'Group 2'),
        ('Group 3', 'Group 3'),
    ]

    group = models.CharField(max_length=50, choices=GROUP_CHOICES)
    heures = models.PositiveIntegerField()
    titre = models.CharField(max_length=200)
    description = models.TextField()
    credits = models.PositiveIntegerField()
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

class Salle(models.Model):
    nom = models.CharField(max_length=100)
    capacite = models.PositiveIntegerField()
    type_salle = models.CharField(max_length=50)
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

class Evaluation(models.Model):
    TYPE_EVALUATION_CHOICES = [
        ('Examen', 'Examen'),
        ('Devoir', 'Devoir'),
        ('Projet', 'Projet'),
    ]

    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    type_evaluation = models.CharField(max_length=50, choices=TYPE_EVALUATION_CHOICES)
    date = models.DateField()
    duree = models.PositiveIntegerField()
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type_evaluation} - {self.date}"

class Note(models.Model):
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    etudiant = models.CharField(max_length=100)
    note = models.FloatField()
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.etudiant} - {self.note}"
