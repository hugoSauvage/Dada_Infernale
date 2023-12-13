from Horse import *
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
    elif def_couleur == "2":
        j1 = Horse(def_nom, "Rouge")
    elif def_couleur == "3":
        j1 = Horse(def_nom, "Bleu")
    elif def_couleur == "4":
        j1 = Horse(def_nom, "Vert")
    
    print("Voici votre perso : ")
    print(j1)
    print("Lancer le dé : ")
    case = j1.lancerDe()
    print(f"Vous avez avancé de {case} cases")
    