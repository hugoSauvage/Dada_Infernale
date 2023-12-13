from jeuBase import *
import random
class Horse(object):
    
    def __init__(self, nom, couleur) -> None:
        self.nom = nom
        self.couleur = couleur
        self.position = 0
        self.etat = False
    
    def lancerDe(self):
        input("Appuyer sur Entrée pour lancer le dé")
        return random.randint(1, 6)
    
    def se_deplacer(self):
        if self.position + self.lancerDe() >= 0:
            self.position += self.lancerDe() 
            print(f"Le pion s'est déplacé de {self.lancerDe()} cases. Nouvelle position : {self.get_position}")
        else:
            print("Déplacement impossible. La nouvelle position serait en dehors du plateau.")

    def get_position(self):
        return self.position
    
    def __str__(self) -> str:
        l1 = f"**** {self.nom} ****\n"
        l2 = f"  - couleur : {self.couleur}\n"
        return l1 + l2