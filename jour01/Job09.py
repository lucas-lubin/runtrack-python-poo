class Produit:
   def __init__(self, nom, prixHT, TVA):
       self.nom = nom
       self.prixHT = prixHT
       self.TVA = TVA

   def CalculerPrixTTC(self):
       return self.prixHT + (self.prixHT * self.TVA / 100)

   def afficher(self):
       print(f"Nom : {self.nom}")
       print(f"Prix HT : {self.prixHT}")
       print(f"TVA : {self.TVA}")
       print(f"Prix TTC : {self.CalculerPrixTTC()}")

   def changerNom(self, nouveau_nom):
       self.nom = nouveau_nom

   def changerPrix(self, nouveau_prix):
       self.prixHT = nouveau_prix

   def getNom(self):
       return self.nom

   def getPrix(self):
       return self.prixHT
produit1 = Produit("Produit 1", 100, 20)
produit1.afficher()

produit2 = Produit("Produit 2", 200, 10)
produit2.afficher()

produit1.changerNom("Nouveau Produit 1")
produit1.changerPrix(150)
produit1.afficher()

produit2.changerNom("Nouveau Produit 2")
produit2.changerPrix(250)
produit2.afficher()