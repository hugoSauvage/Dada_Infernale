class Cheval:
    """
    Un cheval est par défaut dans l'écurie du joueur et sa position est (-1, -1) 
    pour ne pas croire qu'il est dans le plateau
    """
    def __init__(self, position:int = -1) -> None:
        self.position = position
        self.estDansLEcurie = True
    
    def seDeplacer(self, position:int):
        self.estDansLEcurie = False
        self.position = position
    
    def __str__(self) -> str:
        return f"{self.position}"
    
