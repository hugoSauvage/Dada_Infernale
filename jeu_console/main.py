from plateau import *
from joueur import *
from partie import *
import random

# Définir les positions de départ pour chaque joueur
positions_depart = {
    1: (0, 0),  # Les chevaux du joueur 1 commencent sur la ligne 0, colonnes 0 et 1
    2: (0, 11),  # Les chevaux du joueur 2 commencent sur la ligne 0, colonnes 11 et 12
    3: (5, 0),  # Les chevaux du joueur 3 commencent sur la ligne 5, colonnes 0 et 1
    4: (5, 11)  # Les chevaux du joueur 4 commencent sur la ligne 5, colonnes 11 et 12
}


# Pour tester ! à supprimer !
j1 = Joueur("Mr Jouin", "Rouge", 0)


j1.chevaux[0].seDeplacer(0)
j1.chevaux[1].seDeplacer(3)
print(j1)
# print(j1.cheval_arrive(0))
print(j1.chevalDansLEcurie(2))

