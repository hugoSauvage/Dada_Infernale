from joueur import *
from plateau import *
from joueur import *
from partie import *
import random

# print("""
#       Bienvenue dans le jeu de petit chevaux
#       1 - Jouer""")

# menu1 = input("Tapez 1 pour jouer  : ")
# if menu1 == "1":
#     def_nom = input("Choisissez votre nom : ")
#     def_couleur = input("""
#                         Choisissez la couleur de votre choix : 
#                         1 - Jaune
#                         2 - Rouge
#                         3 - Bleu
#                         4- Vert
#                         """)
    
#     if def_couleur == "1":
#         j1 = Horse(def_nom, "Jaune")
#         b1 = Bot("Bot1", "Rouge")
#         b2 = Bot("Bot2", "Vert")
#         b3 = Bot("Bot3", "Bleu")
#     elif def_couleur == "2":
#         j1 = Horse(def_nom, "Rouge")
#         b1 = Bot("Bot1", "Jaune")
#         b2 = Bot("Bot2", "Vert")
#         b3 = Bot("Bot3", "Bleu")
#     elif def_couleur == "3":
#         j1 = Horse(def_nom, "Bleu")
#         b1 = Bot("Bot1", "Rouge")
#         b2 = Bot("Bot2", "Vert")
#         b3 = Bot("Bot3", "Jaune")
#     elif def_couleur == "4":
#         j1 = Horse(def_nom, "Vert")
#         b1 = Bot("Bot1", "Rouge")
#         b2 = Bot("Bot2", "Jaune")
#         b3 = Bot("Bot3", "Bleu")
    
#     print("Voici votre perso : ")
#     print(j1)
#     print("Voici vos adversaire : ")
#     print(b1)
#     print(b2)
#     print(b3)
#     input("Lancer le dé : ")
#     j1.lancerDe()
#     input("Lancer le dé : ")
#     b1.lancerDe()
#     input("Lancer le dé : ")
#     b2.lancerDe()
#     input("Lancer le dé : ")
#     b3.lancerDe()
#     input("Lancer le dé : ")
#     j1.lancerDe()

# Définir les positions de départ pour chaque joueur
positions_depart = {
    1: (0, 0),  # Les chevaux du joueur 1 commencent sur la ligne 0, colonnes 0 et 1
    2: (0, 11),  # Les chevaux du joueur 2 commencent sur la ligne 0, colonnes 11 et 12
    3: (5, 0),  # Les chevaux du joueur 3 commencent sur la ligne 5, colonnes 0 et 1
    4: (5, 11)  # Les chevaux du joueur 4 commencent sur la ligne 5, colonnes 11 et 12
}

# Commencer le jeu
players = [Joueur(i) for i in range(1, 5)]
game = Partie(players)
game.boucle_de_jeu()
