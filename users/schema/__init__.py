import graphene
from .utilisateur_queries import Query as UtilisateurQuery
from .utilisateur_mutations import CreerUtilisateur

class Query(UtilisateurQuery, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    creer_utilisateur = CreerUtilisateur.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)