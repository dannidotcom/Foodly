from users.models.utilisateur import Utilisateur
from ..repositories.utilisateur_repository import UtilisateurRepository


class UtilisateurService:
    @staticmethod
    def creer_utilisateur(data):
        utilisateur = UtilisateurRepository.create(data)
        
        return utilisateur

    @staticmethod
    def obtenir_utilisateur(id):
        return UtilisateurRepository.get_by_id(id)
    
    @staticmethod
    def get_all_utilisateur():
        return UtilisateurRepository.get_all()
    
    @staticmethod
    def modifier_utilisateur(id, user: Utilisateur):
        return UtilisateurRepository.update(id, user)

    @staticmethod
    def sup_utilisateur(id):
        return UtilisateurRepository.delete(id)