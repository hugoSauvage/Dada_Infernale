from jeuBase import *
class Horse(object):
    
    def __init__(self, couleur, nom) -> None:
        self.couleur = couleur
        self.position = 0
        self.nom = nom

        
    def se_deplacer(self):
        if self.position + self.lancerDe() >= 0:
            self.position += self.lancerDe() 
            print(f"Le pion s'est déplacé de {self.lancerDe()} cases. Nouvelle position : {self.get_position}")
        else:
            print("Déplacement impossible. La nouvelle position serait en dehors du plateau.")
    

    def get_position(self):
        return self.position