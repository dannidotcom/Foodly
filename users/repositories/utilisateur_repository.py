


from users.models.utilisateur import Utilisateur


class UtilisateurRepository:
    @staticmethod
    def get_by_id(id):
        return Utilisateur.objects.get(id=id)

    @staticmethod
    def get_all():
        return Utilisateur.objects.all()

    @staticmethod
    def create(data):
        utilisateur = Utilisateur(**data)
        utilisateur.save()
        return utilisateur
    
    @staticmethod
    def update(id, data):
        utilisateur = Utilisateur.objects.get(id=id)
        for key, value in data.items():
            setattr(utilisateur, key, value)
        utilisateur.save()
        return utilisateur

    @staticmethod
    def delete(id):
        utilisateur = Utilisateur.objects.get(id=id)
        utilisateur.delete()
        return True