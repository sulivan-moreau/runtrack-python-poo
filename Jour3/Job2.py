# Créer une classe CompteBancaire avec les attributs privés, numéro de compte, nom, prénom et solde.
# Ajoutez l’attribut decouvert à votre classe CompteBancaire, cet attribut aura pour valeur un booléen. Si le client a le droit à un découvert, la valeur de cet attribut sera True et des opérations pourront être effectuées même si le solde est de zéro (méthode retrait).

#  Cette classe doit posséder les méthodes suivantes :
# ➔ afficher : qui affiche le détail sur le compte.
# ➔ afficherSolde : cette méthode affiche dans le terminal le solde du client.
# ➔ versement : cette méthode prend un paramètre le montant du versement et ajoute celui-ci au solde du client.
# ➔ retrait : cette méthode prend un entier en argument (le montant à retirer) ,enlève ce montant au solde du compte et affiche le nouveau solde.
# ➔ agios : cette méthode permet d’appliquer des agios au solde du compte si celui-ci est négatif.
# ➔ virement : cette méthode prend en paramètre une référence, un compte bancaire (celui qui reçoit l’argent) et un montant.


class CompteBancaire:
    def __init__ (self, numéro, nom, prénom, solde, decouvert, virement):
        self.__number = numéro
        self.__LastName = nom
        self.__firstName = prénom
        self.__credit = solde
        self.__overdraft = True
        self.__amount = virement

    def get_credit(self):
        return self.__credit
        
    def set_credit(self, solde):
        self.__credit = solde

    def afficher(self):
        print(f"afficher({self.__number})\nnuméro de compte : {self.__number}\nNom : {self.__LastName}\nPrénom : {self.__firstName}\nSolde : {self.__credit} brouzoufs\n")

    def afficherSolde(self):
        print(f"\nLe {self.__number} présente un solde de {self.__credit} brouzoufs")     

    def retrait (self, debit):
        if self.__credit > debit or self.__overdraft == True:
            self.debit = int(debit)
            self.__credit -= self.debit
            print(f"\nretrait({debit})\nLe nouveau solde est : {self.__credit} brouzoufs")
        # Veillez à ce que le compte possède bien le montant disponible sinon un message d’erreur est affiché.
        elif self.__credit < debit and self.__overdraft == False:
            print (f"\nLe découvert n'est pas autorisé, faites un rerait moins important.")

    def agios(self):
        #  A faire une fois par mois
        if self.__overdraft == True and self.__credit < 0 :
            self.__credit = self.__credit + (self.__credit*0.05)
            print(f"\nDes agios ont été appliqués. Le solde du {self.__number} est désormais de {self.__credit} brouzoufs")

    def versement(self, versement):
            self.__credit += versement
            print(f"\nAprès versement, le {self.__number} présente un solde de {self.__credit} brouzoufs")
            return self.__credit

    def virement(self, ref, compte, montant):
        self.amount = montant
        if self.__credit >= montant:
            self.__credit -= montant
            compte.versement(montant)
            print(f"\nVirement de {montant} brouzoufs vers le compte {compte.__number} effectué.\n")
        else:
            print("\nErreur : Solde insuffisant pour effectuer le virement.")

        # compte.set_credit = compte.get_credit() + montant
        # print(f"virement de {self.amount} brouzoufs\n")


# Créez un compte avec les valeurs de construction de votre choix 
account1 = CompteBancaire("compte n°1", "Jean", "Aimar", 500, True, None)

# faites appel aux différentes méthodes afin de vérifier que tout fonctionne correctement.
# account1.afficher()
# account1.afficherSolde()
# account1.versement(250)
# account1.retrait(50)
# account1.afficherSolde()


# Créez une deuxième instance de la classe CompteBancaire. ce deuxième compte doit être à découvert (solde négatif).
# Faire un versement du premier compte vers celui à découvert afin de le remettre à zéro.
account2 = CompteBancaire("compte n°2", "Edouard", "Toulouse", -150, True, None)
account1.afficherSolde()
account2.afficherSolde()
account2.agios()
account1.virement(1, account2, 157.5)
