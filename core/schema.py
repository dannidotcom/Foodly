import graphene
from users.schema import Query as UtilisateurQuery
from users.schema import Mutation as UtilisateurMutation

class Query(UtilisateurQuery, graphene.ObjectType):
    pass

class Mutation(UtilisateurMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)