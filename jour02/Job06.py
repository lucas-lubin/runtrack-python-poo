class Commande:
    def __init__(self, numero_commande):
        self._numero_commande = numero_commande
        self._plats = {}  
        self._statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        if self._statut_commande == "en cours":
            self._plats[nom_plat] = {"prix": prix_plat, "statut": "en cours"}
            print(f"Plat '{nom_plat}' ajouté à la commande.")
        else:
            print("La commande ne peut pas être modifiée, elle est déjà en cours de traitement.")

    def annuler_commande(self):
        if self._statut_commande == "en cours":
            self._plats.clear()
            self._statut_commande = "annulée"
            print("La commande a été annulée.")
        else:
            print("La commande ne peut pas être annulée, elle est déjà en cours de traitement ou a été terminée.")

    def _calculer_total(self):
        total = sum(plat["prix"] for plat in self._plats.values())
        return total

    def afficher_commande(self):
        print(f"Commande #{self._numero_commande} - Statut: {self._statut_commande}")
        for nom_plat, plat in self._plats.items():
            print(f"{nom_plat} - Prix: {plat['prix']}€ - Statut: {plat['statut']}")
        total = self._calculer_total()
        print(f"Total à payer : {total}€")

    def calculer_tva(self, taux_tva):
        total = self._calculer_total()
        tva = total * (taux_tva / 100)
        return tva

ma_commande = Commande(101)

ma_commande.ajouter_plat("Pizza", 10)
ma_commande.ajouter_plat("Salade", 5)

ma_commande.afficher_commande()

tva_calculée = ma_commande.calculer_tva(20)
print(f"TVA à payer : {tva_calculée}€")

ma_commande.annuler_commande()
ma_commande.afficher_commande()
