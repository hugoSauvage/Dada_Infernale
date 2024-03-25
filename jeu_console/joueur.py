import random

class Joueur:
    def __init__(self, identifiant):
        self.identifiant = identifiant
        self.score = 0

    def altre_joueur(self):
        # assuming there are always two players in the game
        return self.identifiant if self.identifiant == 'joueur1' else 'joueur2'
