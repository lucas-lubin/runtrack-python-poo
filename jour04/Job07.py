import random



class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = self.creerPaquet()

    def melangerPaquet(self):
        random.shuffle(self.paquet)

    def distribuerCarte(self):
        return self.paquet.pop()
        

    def jouerPartie(self):
        self.melangerPaquet()
        main = self.distribuerCarte()
        bot = self.distribuerCarte()
        print("\nVous avez :", main, "\nLe bot a :", bot)

        while True:
            somme = self.calculerSomme([main, bot])
            if somme == 21:
                return "Félicitations ! Vous avez gagné avec un Blackjack !"
            elif somme > 21:
                return "Désolé, vous avez perdu. Vous avez dépassé 21 points."

            choix = input("Voulez-vous une autre carte ? (Oui / Non) : ")
            if choix.lower() == 'non':
                break
            else:
                main.append(self.distribuerCarte())
                print("Vous avez :", main)

        while True:
            somme = self.calculerSomme(bot)
            if somme >= 17:
                break
            else:
                bot.append(self.distribuerCarte())
                print("Le bot a :", bot)

        if self.calculerSomme(main) > self.calculerSomme(bot):
            return "Félicitations ! Vous avez gagné !"
        else:
            return "Désolé, vous avez perdu. Le bot a plus de points."

    def calculerSomme(self, main):
        somme = 0
        for carte in main:
            if carte[0] == 'V':
                somme += 11
            elif carte[0] == 'D':
                somme += 12
            elif carte[0] == 'R':
                somme += 13
            else:
                somme += int(carte[0])
        return somme

    def creerPaquet(self):
        val = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'V', 'D', 'R']
        coul = ['Coeur', 'Trèfle', 'Carreau', 'Pique']
        paquet = [(val[i], coul[j]) for i in range(len(val)) for j in range(len(coul))]
        return paquet