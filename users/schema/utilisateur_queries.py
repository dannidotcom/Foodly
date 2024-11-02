import graphene

from users.schema.utilisateur_type import UtilisateurType
from users.services.utilisateur_service import UtilisateurService


class Query(graphene.ObjectType):
    utilisateur = graphene.Field(UtilisateurType, id=graphene.Int())
    tous_les_utilisateurs = graphene.List(UtilisateurType)

    def resolve_utilisateur(root, info, id):
        return UtilisateurService.obtenir_utilisateur(id)

    def resolve_tous_les_utilisateurs(root, info):
        return UtilisateurService.get_all_utilisateur()