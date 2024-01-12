class Animal:
    def __init__(self, age=0, prenom=""):
        self.age = age
        self.prenom = prenom

    def vieillir(self):
        self.age += 1

    def nommer(self):
        self.prenom = input("Comment l'animal s'appelle-t-il ? ")


animal = Animal()
print("L'age de l'animal est : ",animal.age," ans")
animal.vieillir()
print("L'age de l'animal est : ",animal.age," ans")
animal.nommer()
print("L'animal se nomme ",animal.prenom )