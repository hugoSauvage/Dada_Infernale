import random
from Cheval import Cheval


class Joueur:
    NB_PLAYERS = 2

    def __init__(self, identifiant, ecurie:str):
        self.identifiant = identifiant
        self.paradis = [i for i in range(6)]
        self.ecurie = ecurie
        self.chevaux = [Cheval(), Cheval(), Cheval(), Cheval()]

    def autre_joueur(self):
        return self.identifiant if self.identifiant == 'joueur1' else 'joueur2'

    def lancer_de(self):
        return random.randint(1, 6)

    def deplacer_pion(self, valeur_de):
        self.position += valeur_de
        if self.position >= self.end_position:
            self.position = self.end_position

    def est_arrive(self):
        return self.position == self.end_position

    def __str__(self) -> str:
        res = ""
        for i in range(len(self.chevaux)):
            res += "\n   --> Cheval n°" + str(i) + " case n°" + str(self.chevaux[i].position)
            res += " dans l'écurie " if self.chevaux[i].estDansLEcurie else " dans le plateau"
        return f"***** Joueur : {self.identifiant} ***** \n - Ecurie : {self.ecurie}\n - Chevaux :" + res


# Pour tester ! à supprimer !
j1 = Joueur("Mr Jouin", "Rouge")
print(j1)

j1.chevaux[0].seDeplacer(0)
j1.chevaux[1].seDeplacer(3)
print(j1)

