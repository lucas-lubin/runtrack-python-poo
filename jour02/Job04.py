class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self._nom = nom
        self._prenom = prenom
        self._numero_etudiant = numero_etudiant
        self._credits = 0
        self._level = self._student_eval()  

    def add_credits(self, nombre_credits):
        if nombre_credits > 0:
            self._credits += nombre_credits
            self._level = self._student_eval() 
        else:
            print("Erreur : Le nombre de crédits doit être supérieur à zéro.")

    def _student_eval(self):
        if self._credits >= 90:
            return "Excellent"
        elif self._credits >= 80:
            return "Très bien"
        elif self._credits >= 70:
            return "Bien"
        elif self._credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print("Nom:", self._nom)
        print("Prénom:", self._prenom)
        print("Numéro d'étudiant:", self._numero_etudiant)
        print("Niveau:", self._level)
        print("Total de crédits:", self._credits)

john_doe = Student("Doe", "John", 145)

john_doe.add_credits(30)
john_doe.add_credits(25)
john_doe.add_credits(15)

john_doe.student_info()