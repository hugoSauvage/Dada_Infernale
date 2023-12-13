from random import *
from Horse import Horse

class jeuBase:
    def __init__(self, joueurs) -> None:
        self.joueurs = [Horse(joueur) for joueur in joueurs]
        self.victoire = False
        self.plateau = [None] * 56
        self.position = [0]

   
   
    def lancerDe(self)-> int :
        return random.randint(1, 6)
    

    def avancer_cheval(self, cheval, de)->int:
        cheval.position += de
    
    
    def afficher_plateau(self)->list:
        return self.plateau
    

    def jouer_tour(self, joueur):
        input(f"{joueur.nom} Appuyer sur Entrée pour lancer le dé")
        de = self.lancerDe()
        self.avancer_cheval(joueur, de)
        self.afficher_plateau()
        print(f"{joueur.nom} a avancé jusque la position {joueur.position}")
    

    def ajouter_cheval(self, cheval)->list:
        if self.couleur.cheval == "jaune":
            self.plateau.append(cheval)
            self.position = [0]
        if self.couleur.cheval == "rouge":
            self.plateau.append(cheval)
            self.position = [15]
        if self.couleur.cheval == "bleu":
            self.plateau.append(cheval)
            self.position = [29]
        if self.couleur.cheval == "vert":
            self.plateau.append(cheval)
            self.position = [43]

    def nbtour(self)-> bool:
        return self.position == 2*self.position         
    
    def afficher_positions(self)-> str:
        for cheval in self.chevaux:
            print(f"{cheval.nom}: {cheval.position}")


    def sauter( self, cheval_1,cheval_2):
        if cheval_1.position == cheval_2.position:
            cheval_1.position = cheval_2.position
            self.plateau.pop(cheval_2)
        if cheval_2.position == cheval_1.position:
            cheval_2.position = cheval_1.position
            self.plateau.pop(cheval_2)


    def victoire( self,cheval)-> str:
        while self.nbtour == False:
            return self.afficher_positions
        return ' vous avais gagner '


    def sortir( self)->object:
        if self.lancerDe == 6:
            self.ajouter_cheval

    
    


