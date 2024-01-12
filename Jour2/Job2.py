# Créer la classe Livre qui prend en attributs privés un titre, un auteur et un nombre de pages.
class Livre:
    def __init__(self, titre, auteur, pages):
        self.__title = titre
        self.__author = auteur
        self.__page_number = pages

# Créer les assesseurs et mutateurs nécessaires afin de pouvoir modifier et afficher les attributs.
    def get_title(self):
        return self.__title

    def set_title(self, titre):
        self.__title = titre
    
    def get_author(self):
        return self.__author

    def set_author(self, auteur):
        self.__author = auteur

    def get_page_number(self):
        return self.__page_number

    def set_page_number(self, pages):
        self.__page_number = pages

    # Pour changer le nombre de pages     
    def set_page_number(self, pages):
        try:
            # ce dernier doit être un nombre entier
            pages = int(pages)
            #  positif
            if pages > 0:
                self.__page_number = pages
            # sinon la valeur n’est pas changée et un message d’erreur est affiché.
            else:
                print("Erreur : Le nombre de pages doit être un nombre entier positif.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier pour le nombre de pages.")


# création de l'objet "les misérables" qui fait 100 pages
les_miserables = Livre("Les miserables","Victor Hugo", 1000)
print(les_miserables.get_page_number())
# Modifie le nombre de pages
les_miserables.set_page_number(2000)
print(les_miserables.get_page_number())
# Modifie le nombre de pages en flottant
les_miserables.set_page_number(1500.3)
print(les_miserables.get_page_number())
# Modifie le nombre de pages en négatif
les_miserables.set_page_number(-1500)
print(les_miserables.get_page_number())