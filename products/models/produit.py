from django.db import models

from products.models.categorie import Categorie

class Produit(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="produits")
    code_barre = models.CharField(max_length=13, blank=True, null=True)
    ref = models.CharField(max_length=16)
    meta = models.CharField(max_length=255, blank=True, null=True)
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    prix_ht = models.FloatField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    date_publication = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.titre