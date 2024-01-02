class Operation:
   def __init__(self, nombre1, nombre2):
       self.nombre1 = nombre1
       self.nombre2 = nombre2

operation = Operation(12, 3)

print("La valeur de nombre1 est : ", vars(operation)["nombre1"])
print("La valeur de nombre2 est : ", vars(operation)["nombre2"])

