class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._en_marche = False
        self._reservoir = 50

    def get_marque(self):
        return self._marque

    def get_modele(self):
        return self._modele

    def get_annee(self):
        return self._annee

    def get_kilometrage(self):
        return self._kilometrage

    def get_en_marche(self):
        return self._en_marche

    def get_reservoir(self):
        return self._reservoir

    # Mutateurs (setters)
    def set_marque(self, marque):
        self._marque = marque

    def set_modele(self, modele):
        self._modele = modele

    def set_annee(self, annee):
        self._annee = annee

    def set_kilometrage(self, kilometrage):
        self._kilometrage = kilometrage

    def set_en_marche(self, en_marche):
        self._en_marche = en_marche

    def demarrer(self):
        if self._verifier_plein():
            self._en_marche = True
            print("La voiture est démarrée.")
        else:
            print("La voiture ne peut pas démarrer, le réservoir est trop bas.")

    def arreter(self):
        self._en_marche = False
        print("La voiture est arrêtée.")

    def _verifier_plein(self):
        return self._reservoir > 5

ma_voiture = Voiture("Toyota", "Camry", 2020, 25000)

print("Marque:", ma_voiture.get_marque())
print("Modèle:", ma_voiture.get_modele())
print("Année:", ma_voiture.get_annee())
print("Kilométrage:", ma_voiture.get_kilometrage())
print("En marche:", ma_voiture.get_en_marche())
print("Reservoir:", ma_voiture.get_reservoir())

ma_voiture.set_kilometrage(30000)
ma_voiture.set_en_marche(True)

ma_voiture.demarrer()
ma_voiture.arreter()
