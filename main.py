from Horse import *
from Bot import *
import random

print("""
      Bienvenue dans le jeu de petit chevaux
      1 - Jouer""")

menu1 = input("Tapez 1 pour jouer  : ")
if menu1 == "1":
    def_nom = input("Choisissez votre nom : ")
    def_couleur = input("""
                        Choisissez la couleur de votre choix : 
                        1 - Jaune
                        2 - Rouge
                        3 - Bleu
                        4- Vert
                        """)
    
    if def_couleur == "1":
        j1 = Horse(def_nom, "Jaune")
        b1 = Bot("Bot1", "Rouge")
        b2 = Bot("Bot2", "Vert")
        b3 = Bot("Bot3", "Bleu")
    elif def_couleur == "2":
        j1 = Horse(def_nom, "Rouge")
        b1 = Bot("Bot1", "Jaune")
        b2 = Bot("Bot2", "Vert")
        b3 = Bot("Bot3", "Bleu")
    elif def_couleur == "3":
        j1 = Horse(def_nom, "Bleu")
        b1 = Bot("Bot1", "Rouge")
        b2 = Bot("Bot2", "Vert")
        b3 = Bot("Bot3", "Jaune")
    elif def_couleur == "4":
        j1 = Horse(def_nom, "Vert")
        b1 = Bot("Bot1", "Rouge")
        b2 = Bot("Bot2", "Jaune")
        b3 = Bot("Bot3", "Bleu")
    
    print("Voici votre perso : ")
    print(j1)
    print("Voici vos adversaire : ")
    print(b1)
    print(b2)
    print(b3)
    input("Lancer le dé : ")
    j1.lancerDe()
    input("Lancer le dé : ")
    b1.lancerDe()
    input("Lancer le dé : ")
    b2.lancerDe()
    input("Lancer le dé : ")
    b3.lancerDe()
    input("Lancer le dé : ")
    j1.lancerDe()
    