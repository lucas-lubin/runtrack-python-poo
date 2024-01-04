class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self._titre = titre
        self._auteur = auteur
        self._nb_pages = nb_pages

    def get_titre(self):
        return self._titre

    def get_auteur(self):
        return self._auteur

    def get_nb_pages(self):
        return self._nb_pages

    def set_titre(self, titre):
        self._titre = titre

    def set_auteur(self, auteur):
        self._auteur = auteur

    def set_nb_pages(self, nb_pages):
        if isinstance(nb_pages, int) and nb_pages > 0:
            self._nb_pages = nb_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

mon_livre = Livre("Le Titre du Livre", "L'Auteur du Livre", 300)

print("Titre :", mon_livre.get_titre())
print("Auteur :", mon_livre.get_auteur())
print("Nombre de pages :", mon_livre.get_nb_pages())

mon_livre.set_titre("Nouveau Titre")
mon_livre.set_auteur("Nouvel Auteur")
mon_livre.set_nb_pages(400)

print("Nouveau titre :", mon_livre.get_titre())
print("Nouvel auteur :", mon_livre.get_auteur())
print("Nouveau nombre de pages :", mon_livre.get_nb_pages())

mon_livre.set_nb_pages(-50)