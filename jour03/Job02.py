class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Numéro de compte: {self.__numero_compte}")
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prenom}")
        print(f"Solde: {self.__solde}")
        print(f"Découvert autorisé: {'Oui' if self.__decouvert else 'Non'}")

    def afficherSolde(self):
        print(f"Solde du compte: {self.__solde}")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} effectué. Nouveau solde: {self.__solde}")

    def retrait(self, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} effectué. Nouveau solde: {self.__solde}")
        else:
            print("Erreur: Solde insuffisant.")

    def agios(self):
        if self.__solde < 0:
            self.__solde += 0.05 * abs(self.__solde)
            print(f"Agios appliqués. Nouveau solde: {self.__solde}")

    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} effectué vers le compte {compte_destinataire.__numero_compte}. Nouveau solde: {self.__solde}")
        else:
            print("Erreur: Solde insuffisant.")

    def supprimerCompte(self):
        del self

    def modifierNom(self, nouveau_nom):
        self.__nom = nouveau_nom

    def modifierPrenom(self, nouveau_prenom):
        self.__prenom = nouveau_prenom

compte1 = CompteBancaire("123456", "Dupont", "Jean", 1000)
compte1.afficher()
compte1.versement(500)
compte1.afficherSolde()
compte1.retrait(200)
compte1.afficherSolde()

compte2 = CompteBancaire("789012", "Martin", "Paul", -500, decouvert=True)
compte2.afficher()
compte1.virement(compte2, 500)
compte2.afficherSolde()