import random
from Cheval import Cheval

class Joueur:
    def __init__(self, identifiant, ecurie, start_position):
        self.identifiant = identifiant
        self.ecurie = ecurie
        self.startPosition = start_position
        self.endPosition = (start_position + 47) % 48
        self.chevaux = [Cheval() for _ in range(4)]

    def lancer_de(self):
        return random.randint(1, 6)

    def cheval_arrive(self, id_cheval):
        if 0 <= id_cheval < len(self.chevaux):
            return self.chevaux[id_cheval].position == self.endPosition
        else:
            print("Erreur de saisie de l'id du cheval [0, 3]")

    def chevalDansLEcurie(self, id_cheval):
        if 0 <= id_cheval < len(self.chevaux):
            return self.chevaux[id_cheval].estDansLEcurie
        else:
            print("Erreur de saisie de l'id du cheval [0, 3]")

    def __str__(self):
        res = "\n".join(f"Cheval n°{i}: {cheval}" for i, cheval in enumerate(self.chevaux))
        return f"***** Joueur : {self.identifiant} ***** \n - Ecurie : {self.ecurie}\n - Chevaux :\n{res}"