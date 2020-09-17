import re

class Salarie():
    """classe salarie définie par :
    - matricule
    - nom
    - prenom
    - salaire brut
    - taux de cotisation sociale
    - salaire net
    - date de naissance
    """
 
    def __init__(self, mat, name, nickname, salaire, taux, date):
        if self.IsValidMatricule(mat) and self.IsValidNomPrenom(name) and self.IsValidNomPrenom(nickname) and self.IsValidTaux(taux):
            self._matricule = mat
            self._nom = name
            self._prenom = nickname
            self._salaireBrut = salaire
            self._salaireNet = self.calculSalaireNet(salaire,taux)
            self._tauxCS = taux
            self._dateNaissance = date
        else :
            return None

    def calculSalaireNet (self, salaire, taux):
        self._salaireNet = salaire*(1-taux)

    def IsValidMatricule (self, mat):
        # la validité du matricule doit etre de forme 2 chiffres + 3 lettres + 2 chiffres
        if not re.search("^\d{2}[A-Z]{3}\d{2}$",mat):
            print('Erreur sur la saisie du matricule')
            return False
        else:
            return True

    def IsValidNomPrenom (self, nomPrenom):
        #vérifie la validité du nom ou prenom, il ne doit pas comporter de nuémrique 
        #et doit être compris entre 3 et 30 caractères
        if re.search("^[a-zA-Z]{3,30}$",nomPrenom):
            return True
        else:
            print('Erreur lors de la saisie du nom ou prénom')
            return False

    def IsValidTaux (self, taux ):
        #vérifie si le taux de charge sociale est compris entre 0.0 et 0.6
        #c'est à entre 0 et 60%
        if taux >= 0.0 and taux <= 0.6:
            return True
        else:
            print("La saisie du taux est incorrecte.")
            return False