import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1 facile, 2 moyen, 3 difficile): "))

    def lancerJeu(self):
        self.choisirNiveau()

        if self.niveau == 1:
            vie_joueur = 100
            vie_ennemi = 50
        elif self.niveau == 2:
            vie_joueur = 80
            vie_ennemi = 70
        elif self.niveau == 3:
            vie_joueur = 60
            vie_ennemi = 90
        else:
            print("Niveau non valide. Le jeu sera lancé avec le niveau facile par défaut.")
            vie_joueur = 100
            vie_ennemi = 50

        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)

        print(f"\nLe jeu commence avec le niveau {self.niveau}.\n")

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                print(f"\nFélicitations! Vous avez vaincu l'ennemi. {joueur.nom} remporte la victoire!")
                break

            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print(f"\nDommage! L'ennemi a vaincu {joueur.nom}. {ennemi.nom} remporte la victoire!")
                break

            print(f"\n{joueur.nom} - Vie: {joueur.vie} | {ennemi.nom} - Vie: {ennemi.vie}\n")

jeu = Jeu()
jeu.lancerJeu()