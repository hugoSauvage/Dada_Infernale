import random
from Cheval import Cheval


class Joueur:
   
    def __init__(self, identifiant:str, ecurie:str, start_position:int):
        self.identifiant = identifiant
        self.paradis = [i for i in range(6)]
        self.ecurie = ecurie
        self.chevaux = [Cheval(), Cheval(), Cheval(), Cheval()]
        self.startPosition = start_position
        #On peut calculer la position de fin
        self.endPosition = ((start_position + 48) - 1) % 48

    def lancer_de(self):
        return random.randint(1, 6)
    
    def cheval_arrive(self, id_cheval: int):
        if id_cheval >= 0 and id_cheval <= 3 :
            return self.chevaux[id_cheval].position == self.endPosition
        print("Erreur de saisie de l'id du cheval [0, 3]")
    
    def chevalDansLEcurie(self, id_cheval: int):
        if id_cheval >= 0 and id_cheval <= 3:
            return self.chevaux[id_cheval].estDansLEcurie
        print("Erreur de saisie de l'id du cheval [0, 3]")
        
    def __str__(self) -> str:
        res = ""
        for i in range(len(self.chevaux)):
            res += "\n   --> Cheval n°" + str(i) + " case n°" + str(self.chevaux[i].position)
            res += " dans l'écurie " if self.chevaux[i].estDansLEcurie else " dans le plateau"
        return f"***** Joueur : {self.identifiant} ***** \n - Ecurie : {self.ecurie}\n - Chevaux :" + res


# Pour tester ! à supprimer !
j1 = Joueur("Mr Jouin", "Rouge", 0)


j1.chevaux[0].seDeplacer(0)
j1.chevaux[1].seDeplacer(3)
print(j1)
# print(j1.cheval_arrive(0))
print(j1.chevalDansLEcurie(2))

