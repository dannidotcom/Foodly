from django.db import models

from products.models.produit import Produit
from users.models.livreur import Livreur


class StockLivreur(models.Model):
    livreur = models.ForeignKey(Livreur, on_delete=models.CASCADE, related_name="stocks")
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name="livreurs")
    quantite_total = models.IntegerField()
    quantite_restante = models.IntegerField()
    date_prise_en_charge = models.DateTimeField()