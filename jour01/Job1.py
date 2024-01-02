class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

operation_instance = Operation()

print("Objet Operation instancié avec les valeurs par défaut :")
print("Nombre1 :", operation_instance.nombre1)
print("Nombre2 :", operation_instance.nombre2)  