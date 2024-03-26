from jeu_console.joueur import Joueur

class Bot(Joueur):
    def __init__(self, nom: str, pos: str) -> None:
        Joueur.__init__(self, nom, pos)