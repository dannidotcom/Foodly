from django.db import models

# Modèle Utilisateur
class Utilisateur(models.Model):
    ROLE_CHOICES = [
        ('admin', 'ROLE_ADMIN'),
        ('client', 'ROLE_CUSTOMER'),
        ('livreur', 'ROLE_DELIVERY'),
    ]
    role = models.CharField(max_length=45, choices=ROLE_CHOICES)
    email = models.EmailField(max_length=255, unique=True)
    nom = models.CharField(max_length=70)
    prenom = models.CharField(max_length=70)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    mot_de_passe = models.CharField(max_length=70)
    validation_token = models.CharField(max_length=70, blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
