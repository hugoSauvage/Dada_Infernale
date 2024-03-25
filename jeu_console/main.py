from joueur import *
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

# Commencer le jeu
joueurs = [Joueur(1), Joueur(2), Joueur(3), Joueur(4)]
partie = Partie(joueurs)
partie.jouer_tout()


joueurs = [Joueur(f'Joueur {i + 1}') for i in range(5)]
partie = Partie(joueurs)

partie.jouer_tout()
