# Récupérer la classe Livre. Ajouter l'attribut privé : disponible ( initialisé par défaut à True ).
class Livre:
    def __init__(self, titre, auteur, pages, disponible):
        self.__title = titre
        self.__author = auteur
        self.__page_number = pages
        self.__available = True

    # Créer une méthode nommée vérification qui vérifie si le livre est disponible, c'est-à-dire
    # que la valeur de son attribut disponible est égale à True. Cette méthode doit retourner
    # True ou False.
    def verification(self):
        if self.__available == True:
            return True
        else:
            return False


# Ajouter une méthode emprunter qui rend le livre indisponible, la valeur de disponible devient False.
# Pour pouvoir emprunter un livre, il faut que celui-ci soit disponible.
# Vérifiez que celui-ci soit disponible sans utiliser l’attribut disponible
    def emprunter(self, verification):
        if verification == True:
            self.__available = False
        else:
            print("ce livre n'est pas disponible")


# Créer une méthode rendre qui dans un premier temps vérifie si le livre a bien été emprunté 
# ( sans utiliser l’attribut disponible), puis change la valeur de l’attribut disponible.
    def rendre(self, verification):
        if verification == False:
            self.__available = True
        else:
            print("ce livre à déjà été rendu")


les_miserables = Livre("Les miserables","Victor Hugo", 1000, "disponible")

les_miserables.emprunter(les_miserables.verification())
print(f"verification : ",les_miserables.verification())
les_miserables.emprunter(les_miserables.verification())
les_miserables.rendre(les_miserables.verification())
print(f"verification : ",les_miserables.verification())
les_miserables.rendre(les_miserables.verification())