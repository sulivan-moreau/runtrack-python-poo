# Créer une classe Rectangle avec des attributs privés, longueur et largeur initialisées
# dans le constructeur.
class Rectangle:
    def __init__(self, longueur, largeur):
        self.__length = longueur
        self.__width = largeur

# Créer des assesseurs et mutateurs afin de pouvoir afficher et modifier les attributs de la
# classe.
    def get_length(self):
        return self.__length
    
    def set_length(self, longueur):
        self.__length = longueur

    def get_width(self):
        return self.__width
    
    def set_width(self, largeur):
        self.__width = largeur


# Créer un rectangle avec les valeurs suivantes : longueur 10 et largeur 5.
rectangle = Rectangle(10, 5)
longueur = rectangle.get_length()
largeur = rectangle.get_width()
print(f"Longueur du rectangle : {longueur}\nLargeur du rectangle : {largeur}")
# Changer la valeur de la longueur et de la largeur
rectangle.set_length(20)
rectangle.set_width(15)

# vérifier que les modifications soient bien prises en compte.
longueur = rectangle.get_length()
largeur = rectangle.get_width()
print(f"Longueur du rectangle : {longueur}\nLargeur du rectangle : {largeur}")