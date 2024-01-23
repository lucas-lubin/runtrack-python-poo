class Ville:
    def __init__(self, nom, habitants):
        self.__nom = nom
        self.__habitants = habitants

    def get_nom(self):
        return self.__nom

    def get_habitants(self):
        return self.__habitants

    def ajouter_population(self):
        self.__habitants += 1

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age

    def get_ville(self):
        return self.__ville

    def ajouter_population(self):
        self.__ville.ajouter_population()

paris = Ville("Paris", 1000000)
print(paris.get_habitants())

marseille = Ville("Marseille", 861635)
print(marseille.get_habitants())

john = Personne("John", 45, paris)
myrtile = Personne("Myrtile", 4, paris)
chloe = Personne("Chloé", 18, marseille)

print(paris.get_habitants())
print(marseille.get_habitants())

jean = Personne("Jean", 30, paris)
print(jean.get_nom(), paris.get_habitants())

jean.ajouter_population()
print(paris.get_habitants())

marie = Personne("Marie", 25, marseille)
print(marie.get_nom(), marseille.get_habitants())