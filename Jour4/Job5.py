from math import pi
# Récupérer votre classe Forme crée juste au-dessus.
class Forme:
    pass

    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        largeur = self.largeur
        hauteur = self.hauteur
        aire =  largeur * hauteur
        print (f"L'aire du rectangle ({self.largeur} x {self.hauteur}) est : {aire} m3")
        return aire

# Créer une classe fille nommée Cercle qui hérite de la classe Forme et possédant un attribut radius.
class Cercle(Forme):
    def __init__ (self, radius):
        self.radius = radius

# Surcharger la méthode aire dans la classe Cercle pour qu'elle renvoie l’aire du cercle.
    def aire(self):
        aire =  pi * (self.radius * self.radius)
        # radius = self.radius
        print (f"L'aire du cercle de rayon ({self.radius}) est : {aire} m3")
        return aire

# Créez une instance de chaque classe Rectangle et Cercle et utilisez-les pour tester les
# différentes surcharges de la méthode aire en affichant les résultats en console.
rectangle = Rectangle(4,5)
rectangle.aire()

cercle = Cercle(5)
cercle.aire()