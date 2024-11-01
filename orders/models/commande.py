from django.db import models

from users.models.adresse import Adresse
from users.models.livreur import Livreur
from users.models.utilisateur import Utilisateur

class Commande(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name="commandes")
    adresse = models.ForeignKey(Adresse, on_delete=models.SET_NULL, null=True, related_name="commandes")
    livreur = models.ForeignKey(Livreur, on_delete=models.SET_NULL, null=True, related_name="commandes")
    ref_commande = models.CharField(max_length=16)
    prix_total = models.FloatField()
    statut_paiement = models.CharField(max_length=45)
    statut_livraison = models.CharField(max_length=45)
    details_service_client = models.TextField(blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    date_paiement = models.DateTimeField(blank=True, null=True)
    date_prise_en_charge = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Commande : {self.ref_commande}"