# Créer une classe Voiture qui a pour attributs privés une marque, modèle, année, kilométrage, en_marche (initialisé par défaut à False).
# Ajoutez à la classe Voiture l’attribut privé reservoir qui est initialisé à 50 par défaut dans le constructeur.
class Voiture:
    def __init__ (self, marque, modèle, année, km, en_marche, reservoire=50):
        self.__brand = marque
        self.__model = modèle
        self.__year = année
        self.__kilometrage = km
        self.__en_marche = False
        self.__fuel_tank = reservoire

# Cette classe doit posséder des mutateurs et assesseurs pour chaque attribut.
    def set_brand(self, marque):
        self.__brand = marque
    def get_brand(self):
        return self.__brand
    
    def set_model(self, modèle):
        self.__model = modèle
    def get_model(self):
        return self.__model

    def set_year(self, année):
        self.__year = année
    def get_year(self):
        return self.__year
    
    def set_kilometrage(self, km):
        self.__kilometrage = km
    def get_kilometrage(self):
        return self.__kilometrage
    

    def get_en_marche(self):
        return self.__en_marche
    
    def set_fuel_tank(self, carburant):
        self.__fuel_tank = carburant
    def get_fuel_tank(self):
        return self.__fuel_tank



# Une méthode arreter qui change la valeur de l’attribut en_marche en False.
    def arreter(self):
        self.__en_marche = False

# Créer une méthode privée verifier_plein qui retourne la valeur de l’attribut reservoir.
    def verifier_plein(self):
        return  self.__fuel_tank


# Créer une méthode demarrer qui change la valeur de l’attribut en_marche en True
# Si la valeur du réservoir est supérieure à 5 la voiture peut démarrer.
    def demarrer(self):
        if self.verifier_plein()>5:
            self.__en_marche = True
        else:
            self.__en_marche = False

panda = Voiture("Fiat", "Panda", 1998, 250000, "en_marche")
print(f"La marque du véhicule est : ",panda.get_brand(),"\nLe modèle du véhicule est : ",panda.get_model(),"\nL'année de mise en circulation du véhicule est : ",panda.get_year(),"\nLe kilométrage du véhicule est : ",panda.get_kilometrage(),"\Le véhicule est en marche : ",panda.get_en_marche(),"\nLe niveau d'essence est : ",panda.get_fuel_tank(),'L')

panda.demarrer()
print(f"\nAprès appel de la méthode demarrer, le véhicule est en marche : ",panda.get_en_marche(),"\n")

panda.set_fuel_tank(2)
print(f"Le niveau d'essence est maintenant de : ",panda.get_fuel_tank(),'L')
panda.demarrer()
print(f"Après appel de la méthode set_fuel_tank(2), le véhicule est en marche : ",panda.get_en_marche(),"\n")