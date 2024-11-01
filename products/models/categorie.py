from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)

    def __str__(self):
        return self.nom