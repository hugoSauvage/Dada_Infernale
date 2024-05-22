class Cheval:
    def __init__(self):
        self.position = -1  # Position initiale du cheval
        self.estDansLEcurie = True  # Indique si le cheval est dans l'écurie ou non

    def seDeplacer(self, deplacement):
        # Méthode pour déplacer le cheval
        if not self.estDansLEcurie:
            self.position = (self.position + deplacement) % 48  # Pour un plateau circulaire

    def sortirEcurie(self):
        # Méthode pour faire sortir le cheval de l'écurie
        if self.estDansLEcurie:
            self.estDansLEcurie = False
            self.position = 0  # Position de départ sur le plateau

    def __str__(self):
        return f"Position: {self.position}, Dans l'écurie: {self.estDansLEcurie}"