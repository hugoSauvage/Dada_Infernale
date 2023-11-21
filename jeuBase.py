from random import *
from Horse import Horse

class jeuBase:
    def __init__(self) -> None:
        self.chevaux = Horse
        for cheveau in Horse:
            self.ajouter_cheval(cheveau)

   
    def lancerDe(self):
        return random.randint(1, 6)
    
    def jouer_tour(self):
        for cheval in self.chevaux:
            pas = self.lancerDe() 
            cheval.avancer(pas)
    
    def ajouter_cheval(self, cheval):
        self.chevaux.append(cheval)

    def afficher_positions(self):
        for cheval in self.chevaux:
            print(f"{cheval.nom}: {cheval.position}")
    