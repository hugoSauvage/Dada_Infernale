from random import *
from Horse import Horse

class jeuBase:
    def __init__(self) -> None:
        self.chevaux_bleu = [Horse("bleu",1), Horse("bleu",2),Horse("bleu",3),Horse("bleu",4) ]
        self.chevaux_rouge = [Horse("rouge",1),Horse("rouge",2),Horse("rouge",3),Horse("rouge",4)]
        self.chevaux_jaune = [Horse("jaune",1),Horse("jaune",2),Horse("jaune",3),Horse("jaune",4)]
        self.chevaux_vert = [Horse("vert",1),Horse("vert",2),Horse("vert",3),Horse("vert",4)]
    
    def lancerDe(self):
        return random.randint(1, 6)
    
    def jouer_tour(self):
        pass
    

    