# Créer une classe Personne qui aura comme attribut age prenant un entier et initialisé à 14 par défaut.
class Personne:
    def __init__ (self, age = 14):
        if isinstance(age, int):
            self.age = age
        else:
            print("Erreur : Veuillez fournir un entier pour l'âge.")


# une méthode afficherAge qui affichera en console l'âge de la personne
    def afficherAge(self):
        print(f"La personne à {self.age} age.")
 
# une méthode bonjour qui écrit en console ‘Hello’.
    def bonjour():
        print("Hello")

# Créer une méthode modifierAge prenant en paramètre un entier et permettant de modifier l'âge de la personne.
    def modifierAge(self, nouvel_age):
        if isinstance(nouvel_age, int):
            self.age = nouvel_age
        else:
            print("Erreur : Veuillez fournir un entier pour l'âge.")

# Créer une classe Eleve qui hérite de la classe Personne qui n’a pas d’attribut
class Eleve(Personne):
    pass
# Et une méthode publique allerEnCours qui affiche : “Je vais en cours”
    def allerEnCours(self):
        print("Je vais en cours")

#  ainsi qu’une méthode afficherAge qui écrit en console : “J’ai XX ans”.
    def afficherAge(self):
        print(f"J'ai {self.age} ans")


# Créer une classe Professeur avec un attribut privé matiereEnseignée, qui indiquera la matière du professeur
class Professeur:
    def __init__ (self, matiereEnseignée):
        self.__matiereEnseignée = matiereEnseignée


#  et une méthode publique enseigner qui affiche : “Le cours va commencer”.
    def enseigner(self):
        print("Le cours va commencer")


# Instancier une classe Personne et une classe Eleve.
personne = Personne()
eleve = Eleve()
# Afficher l'âge par défaut de l’élève en console.
eleve.afficherAge()