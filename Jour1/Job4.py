class Personne:
    def __init__(self, prenom, nom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("je suis ", self.prenom, self.nom)


Jean = Personne("Jean", "Dujardin")
Edouard = Personne("Edouard", "Dupont")
Kacem = Personne("Kacem", "Alwalid")

Jean.SePresenter()
Edouard.SePresenter()
Kacem.SePresenter()