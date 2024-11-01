

from django.db import models
from users.models.utilisateur import Utilisateur

class Livreur(models.Model):
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name="livreur")
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    statut = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return f"Livreur: {self.utilisateur.nom}"