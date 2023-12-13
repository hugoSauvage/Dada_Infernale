from random import *
from Horse import Horse

class jeuBase:
    def __init__(self, joueurs) -> None:
        self.joueurs = [Horse(joueur) for joueur in joueurs]
        self.victoire = False
   
    def lancerDe(self):
        return random.randint(1, 6)
    
    def avancer_cheval(self, cheval, de):
        cheval.position += de
    
    def afficher_plateau(self):
        pass
    
    def jouer_tour(self, joueur):
        input(f"{joueur.nom} Appuyer sur Entrée pour lancer le dé")
        de = self.lancerDe()
        self.avancer_cheval(joueur, de)
        self.afficher_plateau()
        print(f"{joueur.nom} a avancé jusque la position {joueur.position}")
    
    def ajouter_cheval(self, cheval):
        self.chevaux.append(cheval)

    def afficher_positions(self):
        for cheval in self.chevaux:
            print(f"{cheval.nom}: {cheval.position}")
    