
class Rectangle:
    def __init__ (self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur
    
    # def set_longueur(self, longueur):
    #     self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur
    
    # def set_largeur(self, largeur):
    #     self.__longueur = largeur

    def perimetre(self):
        longueur = self.get_longueur()
        largeur = self.get_largeur()

        self.perimetre = 2 * (longueur +  largeur)

        print(f"le rectangle à un perimetre de {self.perimetre} m")

    def surface(self):
        longueur = self.get_longueur()
        largeur = self.get_largeur()

        self.surface = longueur * largeur

        print(f"le rectangle à une surface de {self.surface} m2")
        return self.surface
    
    def get_surface(self):
        print (self.surface)
        return self.surface

class Parallelepipede(Rectangle):
    def __init__ (self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        self.volume = self.surface() * self.hauteur
        print(f"le volume du parallelepipède est {self.volume} m3")


# rectangle = Rectangle(3,4)
# rectangle.perimetre()
# rectangle.surface()
# rectangle.get_surface()
parallelepipede = Parallelepipede(3,4,5)
parallelepipede.volume()