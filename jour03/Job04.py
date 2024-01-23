class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Statistiques de {self.nom} (#{self.numero}, {self.position}):")
        print(f"Buts marqués: {self.buts_marques}")
        print(f"Passes décisives: {self.passes_decisives}")
        print(f"Cartons jaunes: {self.cartons_jaunes}")
        print(f"Cartons rouges: {self.cartons_rouges}")
        print("\n")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom} :")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom_joueur, buts=0, passes_decisives=0, cartons_jaunes=0, cartons_rouges=0):
        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                joueur.buts_marques += buts
                joueur.passes_decisives += passes_decisives
                joueur.cartons_jaunes += cartons_jaunes
                joueur.cartons_rouges += cartons_rouges
                break


joueur1 = Joueur("Messi", 10, "Attaquant")
joueur2 = Joueur("Ronaldo", 7, "Attaquant")
joueur3 = Joueur("Iniesta", 8, "Milieu")

equipe1 = Equipe("Barcelona")
equipe2 = Equipe("Real Madrid")

equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur3)
equipe2.ajouterJoueur(joueur2)

print("Statistiques initiales :")
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

joueur1.marquerUnBut()
joueur2.recevoirUnCartonJaune()

equipe1.mettreAJourStatistiquesJoueur("Messi", buts=1)
equipe2.mettreAJourStatistiquesJoueur("Ronaldo", cartons_jaunes=1)

print("Statistiques après le match :")
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()
