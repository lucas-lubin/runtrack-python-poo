import Livre

def rendre(self):
        if not self.verification():
            self._disponible = True
            print("Livre rendu avec succès.")
        else:
            print("Erreur : Le livre n'a pas été emprunté.")

mon_livre = Livre("Le Titre du Livre", "L'Auteur du Livre", 300)

print("Titre :", mon_livre.get_titre())
print("Auteur :", mon_livre.get_auteur())
print("Nombre de pages :", mon_livre.get_nb_pages())
print("Disponible :", mon_livre.verification())

mon_livre.emprunter()
print("Disponible après emprunt :", mon_livre.verification())

mon_livre.emprunter()

mon_livre.rendre()
print("Disponible après rendu :", mon_livre.verification())

mon_livre.rendre()