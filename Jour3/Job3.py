class Tache:
    """ Classe représentant une tâche individuelle. """
    def __init__(self, titre, description):
        self.titre = titre  # Titre de la tâche
        self.description = description  # Description de la tâche
        self.statut = "à faire"  # Statut initial de la tâche

    def __repr__(self):
        """ Représentation de la tâche sous forme de chaîne de caractères. """
        return f"{self.titre} - {self.description} - {self.statut}"

class ListeDeTaches:
    """ Classe représentant une liste de tâches. """
    def __init__(self):
        self.taches = []  # Liste initiale vide de tâches

    def ajouterTache(self, tache):
        """ Ajoute une nouvelle tâche à la liste. """
        self.taches.append(tache)

    def supprimerTache(self, titre):
        """ Supprime une tâche de la liste en fonction de son titre. """
        self.taches = [tache for tache in self.taches if tache.titre != titre]

    def marquerCommeFinie(self, titre):
        """ Marque une tâche comme terminée en fonction de son titre. """
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "terminé"

    def afficherListe(self):
        """ Retourne la liste actuelle des tâches. """
        return self.taches

    def filterListe(self, statut):
        """ Retourne une liste des tâches filtrée par statut. """
        return [tache for tache in self.taches if tache.statut == statut]

# Tests
liste = ListeDeTaches()
# Ajout de tâches
liste.ajouterTache(Tache("Faire les courses", "Acheter du lait, des œufs et du pain"))
liste.ajouterTache(Tache("Nettoyage", "Nettoyer la cuisine"))
# Marquer une tâche comme terminée
liste.marquerCommeFinie("Nettoyage")

print("Liste complète des tâches :")
for tache in liste.afficherListe():
    print(tache)

print("\nTâches à faire :")
for tache in liste.filterListe("à faire"):
    print(tache)

# Supprimer une tâche
liste.supprimerTache("Faire les courses")
print("\nListe après suppression d'une tâche :")
for tache in liste.afficherListe():
    print(tache)
