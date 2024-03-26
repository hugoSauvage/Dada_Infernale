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


# Create instances of Joueur class
joueur1 = Joueur(identifiant='joueur1')
joueur2 = Joueur(identifiant='joueur2')

# Create an instance of Partie class with the players
jeu = Partie(joueurs=[joueur1, joueur2])

# Start the game
jeu.jouer_tout()