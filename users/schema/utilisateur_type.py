import graphene
from graphene_django.types import DjangoObjectType

from users.models.utilisateur import Utilisateur


class UtilisateurType(DjangoObjectType):
    class Meta:
        model = Utilisateur
        #fields = '__all__'
        exclude = ['mot_de_passe']
        