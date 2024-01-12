import random

class Personnage:
    """ Classe représentant un personnage dans le jeu. """
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        """ Effectue une attaque sur un adversaire, lui enlevant des points de vie. """
        degats = random.randint(5, 10)  # Dégâts aléatoires pour chaque attaque
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et cause {degats} points de dégâts!")

    def estVivant(self):
        """ Vérifie si le personnage est encore en vie. """
        return self.vie > 0

class Jeu:
    """ Classe gérant le déroulement du jeu. """
    def __init__(self):
        self.niveau = None
        self.joueur = None
        self.ennemi = None

    def choisirNiveau(self):
        """ Permet au joueur de choisir le niveau de difficulté. """
        self.niveau = int(input("Choisissez le niveau de difficulté (1-3): "))

    def lancerJeu(self):
        """ Lance le jeu en instanciant le joueur et l'ennemi en fonction du niveau choisi. """
        vie_joueur = 50 if self.niveau == 1 else 40 if self.niveau == 2 else 30
        vie_ennemi = 30 if self.niveau == 1 else 40 if self.niveau == 2 else 50

        self.joueur = Personnage("Joueur", vie_joueur)
        self.ennemi = Personnage("Ennemi", vie_ennemi)

        # Déroulement du jeu
        while self.joueur.estVivant() and self.ennemi.estVivant():
            self.joueur.attaquer(self.ennemi)
            if self.ennemi.estVivant():
                self.ennemi.attaquer(self.joueur)

        self.afficherGagnant()

    def afficherGagnant(self):
        """ Affiche le gagnant du combat. """
        if self.joueur.estVivant():
            print("Vous avez vaincu l'ennemi!")
        else:
            print("L'ennemi a gagné!")

# Création et lancement du jeu
jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()
