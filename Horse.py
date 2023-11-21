class Horse(object):
    
    def __init__(self, couleur, nom, position = 0) -> None:
        self.couleur = couleur
        self.position = position
        self.nom = nom
        
    def seDeplacer(self, nb_case):
        pass
    
    def get_position(self):
        return self.position