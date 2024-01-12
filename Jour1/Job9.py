class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC (self):
        prixTTC = self.prixHT * (self.TVA+100) /100
        return round(prixTTC, 2)
    
    def afficher (self):
        return f"Le prix HT est de : {self.prixHT} £\nLa TVA est de : {self.TVA} %\nLe prix TTC est de : {self.CalculerPrixTTC()} £"
    

        self.nom = nom

    def nouveau_prix(self, prix):
        self.prix = prix
 

        return f"le nom du produit est : {self.nom}"
        
    def prixHT_produit(self):
        return f"le prix HT du produit est :{self.prixHT}"

    def TVA_produit(self):
        return self.prixHT * self.TVA /100 
    
    def prixTTC_produit(self):
        return f"le prix TTC du produit est : {self.CalculerPrixTTC()}"