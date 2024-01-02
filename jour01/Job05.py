class Point:
   def __init__(self, x, y):
       self.x = x
       self.y = y

   def afficherLesPoints(self):
       print(f"Les coordonnées du point sont ({self.x}, {self.y})")

   def afficherX(self):
       print(f"La coordonnée x du point est {self.x}")

   def afficherY(self):
       print(f"La coordonnée y du point est {self.y}")

   def changerX(self, nouveau_x):
       self.x = nouveau_x

   def changerY(self, nouveau_y):
       self.y = nouveau_y


point = Point(5, 7)
point.afficherLesPoints() 
point.afficherX()
point.afficherY() 
point.changerX(10)
point.changerY(15)
point.afficherLesPoints() 