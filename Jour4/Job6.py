
class Vehicule:
    def __init__ (self, marque, modèle, année, prix):
        self.marque = marque
        self.modèle = modèle
        self.année = année
        self.prix = prix
        
    def informationsVehicule(self):
        print(f"marque : {self.marque}\nmodèle : {self.modèle}\nannée : {self.année}\nprix :{self.prix}")

    def demarrer(self):
        print("Attention, je roule.")


class Voiture(Vehicule):
    def __init__(self, marque, modèle, année, prix, portes = 4):
        Vehicule.__init__(self, marque, modèle, année, prix)
        self.portes = portes
        
    def informationsVehicule(self):
        print(f"marque = {self.marque}\nmodèle = {self.modèle}\nannée = {self.année}\nprix = {self.prix}\nportes = {self.portes}\n")

    def demarrer(self):
        print("Attention, je roule avec ma voiture à 4 roues.")



# Créer une classe Moto qui hérite de la classe Vehicule et ajouter l'attribut roue qui contient par défaut l’entier 2.
class Moto(Vehicule):
    def __init__ (self, marque, modèle, année, prix, roue = 2):
        Vehicule.__init__(self, marque, modèle, année, prix)
        self.roue = roue

# Créer à nouveau une méthode informationsVehicule dans la classe Moto qui affiche l'intégralité des informations de la moto.
    def informationsVehicule(self):
        print(f"marque = {self.marque}\nmodèle = {self.modèle}\nannée = {self.année}\nprix = {self.prix}\nroue = {self.roue}\n")

    def demarrer(self):
        print("Attention, je roule avec ma moto à 2 roues.")




peugeot205 = Voiture("Peugeot", "205", "1998", "300 £", 4)
peugeot205.informationsVehicule()
ducati2000 = Moto("Ducati", "2000", "2001", "3000 £", 2)
ducati2000.informationsVehicule()
peugeot205.demarrer()
ducati2000.demarrer()


