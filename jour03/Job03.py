class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"{self.titre} - {self.description} ({self.statut})"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        self.taches = [t for t in self.taches if t.titre != titre]

    def marquerCommeFinie(self, titre):
        for t in self.taches:
            if t.titre == titre:
                t.statut = "terminée"
                break

    def afficherListe(self):
        return [str(t) for t in self.taches]

    def filterListe(self, statut):
        return [t for t in self.taches if t.statut == statut]


tache1 = Tache("Faire les courses", "Acheter des fruits et légumes")
tache2 = Tache("Réviser Python", "Préparer l'exercice de programmation")
tache3 = Tache("Faire du sport", "30 minutes de jogging")

liste_taches = ListeDeTaches()
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

print("Liste initiale:")
print(liste_taches.afficherListe())

liste_taches.supprimerTache("Faire du sport")
print("\nListe après suppression:")
print(liste_taches.afficherListe())

liste_taches.marquerCommeFinie("Faire les courses")
print("\nListe après marquer comme terminée:")
print(liste_taches.afficherListe())

taches_a_faire = liste_taches.filterListe("à faire")
print("\nTâches à faire:")
print([str(t) for t in taches_a_faire])
