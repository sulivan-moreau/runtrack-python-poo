# Créer une classe nommée Forme possédant une méthode nommée aire qui renvoie 0.
class Forme:
    pass

    def aire(self):
        return 0
    
# Créer une classe Rectangle qui hérite de la classe Forme et qui possède deux attributs largeur et hauteur.
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

# Surcharger la méthode aire dans la classe Rectangle afin qu’elle ne renvoie plus 0, mais l’aire du rectangle.
    def aire(self):
        largeur = self.largeur
        hauteur = self.hauteur
        aire =  largeur * hauteur
        print (f"L'aire du rectangle ({self.largeur} x {self.hauteur}) est : {aire} m3")
        return aire

# Écrire en console le résultat de la méthode aire de la classe Rectangle.
rectangle = Rectangle(4,5)
rectangle.aire()