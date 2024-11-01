from django.db import models

from orders.models.commande import Commande
from products.models.produit import Produit

class CommandeProduit(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name="commande_produit")
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name="produits_commande")
    quantity = models.SmallIntegerField()
    details = models.CharField(max_length=255, blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)