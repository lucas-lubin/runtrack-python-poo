class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

import math

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return math.pi * (self.rayon ** 2)
    

rectangle = Rectangle(5, 6)
cercle = Cercle(7)

print(rectangle.aire())
print(cercle.aire()) 