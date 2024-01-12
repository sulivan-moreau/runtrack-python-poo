# Créer une classe Ville avec comme attributs privés un nom et un nombre d'habitants.
class Ville:
    def __init__ (self, nom, habitants):
        self.__name = nom
        self.__population = habitants
    
    def get_population(self):
        return self.__population

    def set_population(self, population):
        self.__population = population

    def get_name(self):
        return self.__name

    def afficher_population(self):
        print(f"La ville de {self.get_name()} compte {self.get_population()} habitants")


# Créer une classe Personne avec les attributs privés suivants : nom, âge et un objet de la classe ville.
class Personne:
    def __init__ (self, nom, âge, ville):
        self.__name = nom
        self.__age = âge
        self.__city = ville
   
# Ajouter la méthode ajouterPopulation dans la classe Personne qui permet d’augmenter de 1 le nombre d’habitants de la ville.
    def ajouterPopulation(self):
        population = self.__city.get_population() + 1
        self.__city.set_population(population)

# Créer un objet Ville avec comme arguments “Paris” et 1000000.
# Afficher en console le nombre d’habitants de la ville de Paris.
paris = Ville("Paris", 1000000)
paris.afficher_population()

# Créer un autre objet Ville avec comme arguments “Marseille” et 861635.
# Afficher en console le nombre d’habitants de la ville de Marseille.
marseille = Ville("Marseille", 861635)
marseille.afficher_population()

# Créer les objets suivants : John, 45 ans, habitant à Paris - Myrtille, 4 ans, habitant à Paris - Chloé, 18 ans, habitant à Marseille
John = Personne("John", 45, paris)
Myrtille = Personne("Myrtille", 4, paris)
Chloé = Personne("Chloé", 18, marseille)

John.ajouterPopulation()
Myrtille.ajouterPopulation()
Chloé.ajouterPopulation()

# Afficher le nombre d’habitants de Paris et de Marseille après l’arrivée de ces nouvelles personnes.
paris.afficher_population()
marseille.afficher_population()