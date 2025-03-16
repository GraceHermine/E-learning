from django.db import models

# Create your models here.
class Departement(models.Model):
    nom = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2)

    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=False)
    last_updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.nom
    

class Club(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()

    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=False)
    last_updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.nom

class Evenement(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    date = models.DateField()
    lieu = models.CharField(max_length=255)

    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=False)
    last_updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.nom