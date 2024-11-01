
from django.db import models

# Modèle Adresse
class Adresse(models.Model):
    adresse_1 = models.CharField(max_length=255)
    adresse_2 = models.CharField(max_length=255, blank=True, null=True)
    code_postal = models.CharField(max_length=10)
    ville = models.CharField(max_length=255)
    pays = models.CharField(max_length=120)
    label = models.CharField(max_length=140)
    description = models.CharField(max_length=70, blank=True, null=True)
    code_acces = models.CharField(max_length=10, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.label} - {self.ville}"