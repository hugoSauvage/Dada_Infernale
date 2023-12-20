from Horse import Horse

class Bot(Horse):
    def __init__(self, nom: str, couleur: str) -> None:
        Horse.__init__(self, nom, couleur)