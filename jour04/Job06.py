class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("Marque: ", self.marque)
        print("Modele: ", self.modele)
        print("Annee: ", self.annee)
        print("Prix: ", self.prix)

        def demarrer(self):
            print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes
    
        
        def demarrer(self):
            print("La voiture démarre")

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de portes: ", self.portes)

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues=2):
        super().__init__(marque, modele, annee, prix)
        self.roues = roues

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de roues: ", self.roues)
    
        def demarrer(self):
            print("La moto démarre")