import random


class Joueur:
    NB_PLAYERS = 2

    def __init__(self, identifiant, start_position=0):
        self.identifiant = identifiant
        self.score = 0
        self.position = start_position
        self.end_position = 100

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