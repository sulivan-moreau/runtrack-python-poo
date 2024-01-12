import random

class Carte:
    """ Classe représentant une carte avec une valeur et une couleur. """
    def __init__(self, valeur, couleur):
        self.valeur = valeur  # La valeur de la carte (2-10, Valet, Dame, Roi, As)
        self.couleur = couleur  # La couleur de la carte (Pique, Coeur, Carreau, Trefle)

    def __repr__(self):
        """ Représentation de la carte sous forme de chaîne. """
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    """ Classe représentant le jeu de Blackjack. """

    # Valeurs et couleurs possibles pour les cartes
    valeurs = [str(n) for n in range(2, 11)] + ["Valet", "Dame", "Roi", "As"]
    couleurs = ["Pique", "Coeur", "Carreau", "Trefle"]

    def __init__(self):
        """ Initialisation du jeu : création du paquet de cartes et initialisation des mains du joueur et du croupier. """
        # Création d'un paquet de 52 cartes
        self.paquet = [Carte(valeur, couleur) for couleur in self.couleurs for valeur in self.valeurs]
        self.joueur_main = []  # Main du joueur
        self.croupier_main = []  # Main du croupier

    def melanger(self):
        """ Mélange le paquet de cartes. """
        random.shuffle(self.paquet)

    def distribuer(self):
        """ Distribue deux cartes à chaque joueur. """
        for _ in range(2):
            self.joueur_main.append(self.paquet.pop())
            self.croupier_main.append(self.paquet.pop())

    def valeur_main(self, main):
        """ Calcule la valeur totale d'une main donnée. """
        total = 0
        as_count = 0  # Compteur d'As dans la main
        for carte in main:
            if carte.valeur in ["Valet", "Dame", "Roi"]:
                total += 10
            elif carte.valeur == "As":
                as_count += 1
                total += 11
            else:
                total += int(carte.valeur)

        # Ajustement pour les As (peuvent valoir 1 ou 11)
        while total > 21 and as_count:
            total -= 10
            as_count -= 1

        return total

    def prendre_carte(self, main):
        """ Ajoute une carte à la main donnée. """
        main.append(self.paquet.pop())

    def jouer_joueur(self):
        """ Simule le tour du joueur (non interactif). """
        while self.valeur_main(self.joueur_main) < 17:
            self.prendre_carte(self.joueur_main)
            if self.valeur_main(self.joueur_main) > 21:
                print("Joueur dépasse 21. Croupier gagne.")
                return False
        return True

    def jouer_croupier(self):
        """ Simule le tour du croupier. """
        while self.valeur_main(self.croupier_main) < 17:
            self.prendre_carte(self.croupier_main)

    def determiner_gagnant(self):
        """ Détermine le gagnant de la partie. """
        joueur_total = self.valeur_main(self.joueur_main)
        croupier_total = self.valeur_main(self.croupier_main)

        if joueur_total > 21:
            return "Croupier gagne"
        elif croupier_total > 21 or joueur_total > croupier_total:
            return "Joueur gagne"
        elif joueur_total < croupier_total:
            return "Croupier gagne"
        else:
            return "Égalité"

    def jouer(self):
        """ Lance une partie de Blackjack. """
        self.melanger()
        self.distribuer()

        print("Main initiale du joueur:", self.joueur_main)
        print("Main initiale du croupier:", [self.croupier_main[0], "Carte cachée"])

        if not self.jouer_joueur():
            return

        self.jouer_croupier()

        print("Main finale du joueur:", self.joueur_main)
        print("Main finale du croupier:", self.croupier_main)

        resultat = self.determiner_gagnant()
        print(resultat)
