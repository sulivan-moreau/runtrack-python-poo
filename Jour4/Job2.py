class Personne:
    def __init__ (self, age = 14):
        if isinstance(age, int):
            self.age = age
        else:
            print("Erreur : Veuillez fournir un entier pour l'âge.")

    def afficherAge(self):
        print(f"La personne à {self.age} age.")

    def bonjour(self):
        nom_classe = type(self).__name__
        print(f"Le {nom_classe} dit 'bonjour'.")

    def modifierAge(self, nouvel_age):
        if isinstance(nouvel_age, int):
            self.age = nouvel_age
            nom_classe = type(self).__name__
            print(f"{nom_classe} à {nouvel_age} ans")
        else:
            print("Erreur : Veuillez fournir un entier pour l'âge.")

class Eleve(Personne):
    pass

    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    def __init__ (self, matiereEnseignée):
        self.__matiereEnseignée = matiereEnseignée

    def enseigner(self):
        print("Le cours va commencer")

personne = Personne()
eleve = Eleve()

# À l’aide de la classe Personne , Eleve et Professeur créent au-dessus, faites dire bonjour à votre élève grâce à la méthode bonjour
eleve.bonjour()
# ainsi que “Je vais en cours” grâce à la méthode allerEnCours.
eleve.allerEnCours()
# Redéfinir l'âge de l’élève à 15 ans.
eleve.modifierAge(15)
# Créer un objet Professeur, 40 ans, faite dire bonjour à votre professeur et commencer le cours grâce à la méthode enseigner.
professeur = Professeur("sieste")
professeur.modifierAge(40)
professeur.bonjour()
professeur.enseigner()