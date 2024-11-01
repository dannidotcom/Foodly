from django.db import models

from users.models.adresse import Adresse
from users.models.utilisateur import Utilisateur

class AdresseClient(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name="adresses_clients")
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE, related_name="clients_adresse")