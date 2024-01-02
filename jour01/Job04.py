class Personne:
   def __init__(self, nom, prenom):
       self.nom = nom
       self.prenom = prenom

   def se_presenter(self):
       print(f"Bonjour, je m'appelle {self.prenom} {self.nom}")

personne1 = Personne("Doe", "John")
personne2 = Personne("Jean", "Dupond")

personne1.se_presenter()
personne2.se_presenter()