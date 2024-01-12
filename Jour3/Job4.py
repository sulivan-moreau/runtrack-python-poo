class Joueur:
    """ Classe représentant un joueur de football. """
    def __init__(self, nom, numero, position):
        # Initialisation des attributs du joueur
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        """ Incrémente le nombre de buts marqués par le joueur. """
        self.buts += 1

    def effectuerUnePasseDecisive(self):
        """ Incrémente le nombre de passes décisives effectuées par le joueur. """
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        """ Incrémente le nombre de cartons jaunes reçus par le joueur. """
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        """ Incrémente le nombre de cartons rouges reçus par le joueur. """
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        """ Affiche les statistiques du joueur. """
        return f"{self.nom} (#{self.numero}, {self.position}) - Buts: {self.buts}, Passes: {self.passes_decisives}, Cartons Jaunes: {self.cartons_jaunes}, Cartons Rouges: {self.cartons_rouges}"

class Equipe:
    """ Classe représentant une équipe de football. """
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []  # Liste initiale vide de joueurs

    def ajouterJoueur(self, joueur):
        """ Ajoute un joueur à l'équipe. """
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        """ Affiche les statistiques de tous les joueurs de l'équipe. """
        for joueur in self.joueurs:
            print(joueur.afficherStatistiques())

    def mettreAJourStatistiquesJoueur(self, nom, buts=0, passes=0, jaunes=0, rouges=0):
        """ Met à jour les statistiques d'un joueur spécifique. """
        for joueur in self.joueurs:
            if joueur.nom == nom:
                joueur.buts += buts
                joueur.passes_decisives += passes
                joueur.cartons_jaunes += jaunes
                joueur.cartons_rouges += rouges

# Création et ajout de joueurs dans une équipe
equipe = Equipe("Les Aigles")
joueur1 = Joueur("John Doe", 10, "Attaquant")
joueur2 = Joueur("Jane Smith", 8, "Milieu")
equipe.ajouterJoueur(joueur1)
equipe.ajouterJoueur(joueur2)

# Simulation d'un match
joueur1.marquerUnBut()
joueur2.effectuerUnePasseDecisive()
joueur1.recevoirUnCartonJaune()

# Affichage des statistiques après le match
equipe.afficherStatistiquesJoueurs()
