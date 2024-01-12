# Créer une classe Commande avec les attributs privés, numéro de commande, liste de plats commandés et statut de la commande (en cours, terminée ou annulée).
class Commande:
    def __init__(self, numéro, plats, statut):
        self.__number = numéro
        self.__dishes = {}
        self.__status = "en cours"
  

# Ajouter un plat à la commande
# La liste des plats commandés doit être représentée sous forme de dictionnaire avec les noms des plats, le prix, le statut de la commande.
    def add_dish(self, dish, prix):
        if self.__status == "en cours":
            self.__dishes[dish] = {"plat": dish, "prix": prix, "status": "en cours"}

            print("\nle plat ajouté est : ",dish, "\nle prix de ce plat est : ",prix,"£ HT")


# Annuler une commande
    def cancel(self):
        self.__status = "annulée"
        print("\nLa commande est annulée")

# calculer le total d’une commande qui doit être en privé
    def __calculer_total_HT(self):
        self.__total = sum(plat["prix"] for plat in self.__dishes.values()if plat["status"]=='en cours')
        print("\nle total de la commande est : ",self.__total,"£ HT")
        return self.__total
    
    def resTotal(self):
        return self.__calculer_total_HT()
    
# afficher une commande avec son total à payer,       
    def afficher_commande(self):
        # print (f"\nles plats commandé sont : {self.__dishes[dish]}")
        print("\nLes plats commandés sont : ")
        for plat in self.__dishes.values():
            print(f"{plat['plat']} - {plat['prix']}£ HT")
        print(f"Le total est : {self.__total} HT\n")


# méthode permettant de calculer la TVA.
    def set_TVA(self):
        self.__calculer_total_HT()
        self.__TVA = self.__total * 0.2
        print(f"La TVA est de : {self.__TVA} £\n")
        return self.__TVA


# Utiliser l’encapsulation et l’abstraction pour créer cette classe de manière que
# les attributs ne puissent pas être modifiés de l’extérieur.
salade = "Salade"
steack = "Steack"
tarte = "Tarte"

# table_12 = Commande(1,{},"")
# table_12.add_dish(salade,10)
# table_12.cancel()

table_12 = Commande(1,{},"")
table_12.add_dish(steack,15)
table_12.add_dish(tarte,5)
table_12.resTotal()
table_12.afficher_commande()
table_12.set_TVA()
