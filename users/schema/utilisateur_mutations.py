import graphene
from .utilisateur_type import UtilisateurType
from ..services.utilisateur_service import UtilisateurService


class CreerUtilisateur(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        nom = graphene.String(required=True)
        prenom = graphene.String(required=True)
        role = graphene.String(required=True)
        telephone = graphene.String(required=True)
        mot_de_passe = graphene.String(required=True)

    utilisateur = graphene.Field(UtilisateurType)

    def mutate(self, info, email, nom, prenom, role, telephone, mot_de_passe):
        data = {
            'email': email,
            'nom': nom,
            'prenom': prenom,
            'role': role,
            'telephone': telephone,
            'mot_de_passe': mot_de_passe
        }
        utilisateur = UtilisateurService.creer_utilisateur(data)
        return CreerUtilisateur(utilisateur=utilisateur)

class UpdateUtilisateur(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        email = graphene.String()
        nom = graphene.String()
        prenom = graphene.String()
        role = graphene.String()
        telephone = graphene.String()
        mot_de_passe = graphene.String()

    utilisateur = graphene.Field(UtilisateurType)

    def mutate(self, info, id, email=None, nom=None, prenom=None, role=None, telephone=None, mot_de_passe=None):
        data = {
            'email': email,
            'nom': nom,
            'prenom': prenom,
            'role': role,
            'telephone': telephone,
            'mot_de_passe': mot_de_passe
        }
        # Filtrez les champs `None` pour ne mettre à jour que les champs fournis
        data = {k: v for k, v in data.items() if v is not None}
        utilisateur = UtilisateurService.modifier_utilisateur(id, data)

        return UpdateUtilisateur(utilisateur=utilisateur)

class DeleteUtilisateur(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        success = UtilisateurService.sup_utilisateur(id)
        return DeleteUtilisateur(success=success)

class GetAllUtilisateurs(graphene.Mutation):
    utilisateurs = graphene.List(UtilisateurType)

    def mutate(self, info):
        utilisateurs = UtilisateurService.get_all_utilisateur()
        return GetAllUtilisateurs(utilisateurs=utilisateurs)

# Assemblage des Mutations dans une Classe Mutation
class Mutation(graphene.ObjectType):
    creer_utilisateur = CreerUtilisateur.Field()
    update_utilisateur = UpdateUtilisateur.Field()
    delete_utilisateur = DeleteUtilisateur.Field()
    get_all_utilisateurs = GetAllUtilisateurs.Field()