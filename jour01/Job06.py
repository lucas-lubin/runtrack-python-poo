class Animal:
  def __init__(self):
      self.age = 0
      self.prenom = ""

  def afficherAge(self):
      print(f"L'âge de l'animal est {self.age}")

  def vieillir(self):
      self.age += 1

  def nommer(self, nom):
      self.prenom = nom

  def afficherNom(self):
      print(f"Le nom de l'animal est {self.prenom}")



animal = Animal()
animal.afficherAge()
animal.vieillir()
animal.afficherAge() 
animal.nommer("Rex")
animal.afficherNom() 