# classe  Student qui a comme attributs privés un nom, un prénom, un numéro d’étudiants et un nombre de crédits par défaut à zéro.
# Ajouter l’attribut privé nommé level dans le constructeur de la classe Student qui prend en valeur la méthode __studentEval.
class Student:
    def __init__(self, nom, prenom, numero, credits, niveau):
        self.__name = nom
        self.__first_name = prenom
        self.__number = numero
        self.__points = 0
        self.__level = self.__studentEval()

# La méthode add_credits permet d’ajouter un nombre de crédits au total de celui de l’étudiant.
# Ce mutateur doit s’assurer que la valeur passée en argument est supérieure à zéro pour garantir l’intégrité
# de la valeur.
    def add_credits(self, bonus):
        if bonus>0:
            self.__points += bonus
        else:print("Il faut un nombre positif, on ne peut pas enlever de points de crédit")

# Méthode get_credits permet d'obtenir le nombre de crédits
    def get_credits(self):
        return self.__points

# créer une méthode nommée __studentEval qui sera privée Cette méthode retourne 
# “Excellent”   si le nombre de crédits est égal ou supérieur à 90
# “Très bien”   si le nombre est supérieur ou égal à 80
# “Bien”        si le nombre est supérieur ou égale à 70
# “Passable”    si égale ou supérieure à 60
# “Insuffisant” si inférieur à 60. 
    def __studentEval(self):
        if self.__points>=90:
            return "Excellent"
        elif self.__points>=80:
            return "Très bien"
        elif self.__points>=70:
            return "Bien"
        elif self.__points>=60:
            return "Passable"
        else:
            return "Insuffisant"

# Créer une méthode studentInfo qui écrit en console les informations de l’étudiant (nom, prénom, identifiant et niveau).
    def studentInfo(self):
        print("Nom :", self.__name)
        print("Prénom :", self.__first_name)
        print("Identifiant :", self.__number)
        print("Niveau :", self.__studentEval())
        

# Instancier un objet représentant l’étudiant John Doe qui possède le numéro d’étudiant 145. 
John_Doe = Student("Doe", "John" ,145, "credits", "niveau")

# Ajoutez-lui des crédits à trois reprises et imprimez son total de crédits en console.
John_Doe.add_credits(5)
John_Doe.add_credits(7)
John_Doe.add_credits(5)
print("Total de crédits de John Doe :", John_Doe.get_credits())

# Afficher les informations de l'étudiant John Doe
print("Ci dessous le résultat de la méthode studentInfo")
John_Doe.studentInfo()




