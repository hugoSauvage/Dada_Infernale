class Joueur:
    def __init__(self, numero, score=0):
        self.numero = numero
        self.score = score

    def autre_joueur(self):
        return f'Joueur {(self.numero % 2) + 1}'
    
