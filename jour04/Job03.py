class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    def get_longueur(self):
        return self._longueur

    def set_longueur(self, valeur):
        self._longueur = valeur

    def get_largeur(self):
        return self._largeur

    def set_largeur(self, valeur):
        self._largeur = valeur

    def perimetre(self):
        return 2*(self._longueur + self._largeur)

    def surface(self):
        return self._longueur * self._largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self._hauteur = hauteur

    def get_hauteur(self):
        return self._hauteur

    def set_hauteur(self, valeur):
        self._hauteur = valeur

    def volume(self):
        return self._longueur * self._largeur * self._hauteur
    


rectangle = Rectangle(5, 6)
print(rectangle.perimetre()) 
print(rectangle.surface()) 

parallelepipede = Parallelepipede(5, 6, 7)
print(parallelepipede.perimetre()) 
print(parallelepipede.surface()) 
print(parallelepipede.volume()) 