# map1 = [
#        [" |","┌", "-", " -", " -", "-", "┐", "●", "J", "M"," ┌", "-", " -", " -", "-","┐","|"],
#        [" |","|", "0", " 0", " 0", "0", "|", "●", "1", "●", "|", "0", "0", "0", "0", " |","|"],
#        [" |","|", "0", " 0", " 0", "0", "|", "●", "2", "●", "|", "0", "0", "0", "0", " |","|"],
#        [" |","|", "0", " 0", " 0", "0", "|", "●", "3", "●", "|", "0", "0", "0", "0", " |","|"],
#        [" |","|", "0", " 0", " 0", "0", "|", "●", "4", "●", "|", "0", "0", "0", "0", " |","|"],
#        [" |","└", "-", " -", " -", "-", "┘", "●", "5", "●", "└", "-", "-", "-", "-", " ┘","|"],
#        [" |", "M", " ●", " ●", "●", "●", "●","●", "6", "●", "●", "●", "●", "●", "●","●" ," |"],
#        [" |", "R", " 1", " 2", "3", "4", "5", "6","G", "6", "5", "4", "3", "2", "1","B", " |"],
#        [" |", "●", " ●", " ●", "●", "●", "●","●", "6", "●", "●", "●", "●", "●", "●","M" ," |"],
#        [" |","┌", "-", " -", " -", "-", "┐", "●", "5", "●", "┌", "-", "-", "-", "-", " ┐","|"],
#        [" |","|", "0", " 0", " 0", "0", "|", "●", "4", "●", "|", "0", "0", "0", "0", " |","|"],
#        [" |","|", "0", " 0", " 0", "0", "|", "●", "3", "●", "|", "0", "0", "0", "0", " |","|"],
#        [" |","|", "0", " 0", " 0", "0", "|", "●", "2", "●", "|", "0", "0", "0", "0", " |","|"],
#        [" |","|", "0", " 0", " 0", "0", "|", "●", "1", "●", "|", "0", "0", "0", "0", " |","|"],
#        [" |","└", "-", " -", " -", "-", "┘", "M", "V", "●", "└", "-", " -", " -", "-","┘","|"],

#        ]
# # crée une double liste avec dans un liste les ● puis mettre dans la liste une autre liste avec les caracthère spéciale

# import random

# class JeuDeSociete:
#     def __init__(self, map1):
#         self.map = map1
#         self.chevaux = {"hv": {"position": "0", "termine": False},
#                         "hr": {"position": "0", "termine": False},
#                         "hj": {"position": "0", "termine": False},
#                         "hb": {"position": "0", "termine": False}}

#     def lancer_de(self):
#         return random.randint(1, 6)

#     def deplacer_cheval(self, couleur):
#         de_resultat = self.lancer_de()
#         position_actuelle = self.chevaux[couleur]["position"]

#         if position_actuelle == "0" and de_resultat == 6:
#             # Le cheval apparaît sur le "1" car il a obtenu un 6
#             self.chevaux[couleur]["position"] = "M"
#         else:
#             # Déplacement normal sur les "●"
#             nouvelle_position = self.avancer_sur_les_cases(position_actuelle, de_resultat)
#             self.chevaux[couleur]["position"] = nouvelle_position

#             # Vérification si le cheval a terminé son tour
#             if nouvelle_position in ["hv", "hr", "hj", "hb"]:
#                 self.chevaux[couleur]["termine"] = True

#     def avancer_sur_les_cases(self, position_actuelle, de_resultat):
#         # Logique de déplacement sur les cases "●"
#         if position_actuelle == "0":
#             position_actuelle = 0
#             print("Tu y es presque, mais tu n'as pas fait six recomptes.")
#         if position_actuelle == "M" and "R" and "J" and "B" and "V":
#             valeur = 1
#             position_actuelle = valeur
#             nouvelle_position = int(position_actuelle) + de_resultat
#             if nouvelle_position > 15:
#                 nouvelle_position = 15  # Limite la position à 15
#             print(f' tu parcouru {nouvelle_position - position_actuelle} est maintenant tu est au "●" {nouvelle_position}! ')
#             return str(nouvelle_position)
#         if position_actuelle == "●":
#             valeur = 1
#             position_actuelle = valeur
#             nouvelle_position = int(position_actuelle) + de_resultat
#             if nouvelle_position > 15:
#                 nouvelle_position = 15  # Limite la position à 15
#             print(f' tu parcouru  {nouvelle_position - position_actuelle} est maintenant tu est au "●" {nouvelle_position}! ')
#             return str(nouvelle_position)

#     def __str__(self) -> dict:
#         return self.chevaux

# # Exemple d'utilisation
# jeu = JeuDeSociete(map1)

# # Déplacer le cheval rouge
# jeu.deplacer_cheval("hr")
# print("Position du cheval rouge:", jeu.chevaux["hr"]["position"])
# print("Tour terminé:", jeu.chevaux["hr"]["termine"])
# print(map1)
# print(jeu.__str__())

# from Horse import *


# ligne1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# maison =[1,2,3,4,5,6]


# def déplacement (self,position_départ : int)-> int:
#     position = self.lancer_de()
#     return position + position_départ

# def verification(self):
#     pass

# def jeux (self):
#     if self.chevaux.couleur == "vert":
#         position = ligne1[0]
#         a = self.déplacement(position)
#         mouvement = ligne1[a]
#     elif self.chevaux.couleur == "jaune":
#         position = ligne1[14]
#         a = self.déplacement(position)
#         mouvement = ligne1[a]
#     elif self.chevaux.couleur == "bleu":
#         position = ligne1 =[28]
#         a = self.déplacement(position)
#         mouvement = ligne1[a]
#     elif self.chevaux.couleur == "rouge":
#         position = ligne1[42]
#         a = self.déplacement(position)
#         mouvement = ligne1[a]
#     return mouvement



# autre solution 
plateau = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
         22, 24, 26, 28, 30, 32, 34, 36, 38, 40,
         42, 44, 46, 48, 50]

import random

class Joueur:
    def __init__(self, nom, couleur):
        self.nom = nom
        self.couleur = couleur
        self.position = 0

    def deplacer(self, espaces):
        self.position += espaces
        if self.position > len(plateau) - 1:
            self.position = len(plateau) - 1
        elif self.position < 0:
            self.position = 0
        self.position += plateau[self.position]

    def __str__(self):
        return f"{self.nom} ({self.couleur})"

def deplacer_joueur(joueur, espaces):
    joueur.deplacer(espaces)
    print(f"{joueur.nom} ({joueur.couleur}) est maintenant sur l'espace {joueur.position}.")

def lancer_de():
    return random.randint(1, 6)

def jouer_tour(joueur):
    espaces = lancer_de()
    print(f"{joueur.nom} ({joueur.couleur}) a lancé un {espaces}.")
    deplacer_joueur(joueur, espaces)

def gerer_collision(joueur1, joueur2):
    if joueur1.position == joueur2.position:
        joueur1.position += plateau[joueur1.position]
        print(f"{joueur1.nom} ({joueur1.couleur}) a atterri sur le même espace que {joueur2.nom} ({joueur2.couleur}) et a été renvoyé en arrière!")
    elif joueur2.position == joueur1.position:
        joueur2.position += plateau[joueur2.position]
        print(f"{joueur2.nom} ({joueur2.couleur}) a atterri sur le même espace que {joueur1.nom} ({joueur1.couleur}) et a été renvoyé en arrière!")

def jouer_partie(joueurs):
    while True:
        for joueur in joueurs:
            jouer_tour(joueur)
            for autre_joueur in joueurs:
                if autre_joueur != joueur:
                    gerer_collision(joueur, autre_joueur)
            if joueur.position == len(plateau) - 1:
                print(f"{joueur.nom} ({joueur.couleur}) a gagné le jeu!")
                return True


def deplacer_joueur(joueur, espaces):
    joueur.deplacer(espaces)
    print(f"{joueur.nom} est maintenant sur la case {joueur.position}.")

import random

def lancer_de():
    return random.randint(1, 6)

def jouer_tour(joueur):
    espaces = lancer_de()
    print(f"{joueur.nom} a obtenu un {espaces}.")
    deplacer_joueur(joueur, espaces)


def gerer_collision(joueur1, joueur2):
    if joueur1.position == joueur2.position:
        joueur1.position += plateau[joueur1.position]
        print(f"{joueur1.nom} est arrivé sur la même case que {joueur2.nom} et a été renvoyé en arrière!")
    elif joueur2.position == joueur1.position:
        joueur2.position += plateau[joueur2.position]
        print(f"{joueur2.nom} est arrivé sur la même case que {joueur1.nom} et a été renvoyé en arrière!")



# joueur1 = Joueur("Joueur 1")
# joueur2 = Joueur("Joueur 2")

# while joueur1.position < len(plateau) and joueur2.position < len(plateau):
#     jouer_tour(joueur1)
#     jouer_tour(joueur2)
#     gerer_collision(joueur1, joueur2)

joueurs = [Joueur("Joueur 1", "rouge"), Joueur("Joueur 2", "bleu"), Joueur("Joueur 3", "vert"), Joueur("Joueur 4", "jaune")]
jouer_partie(joueurs)

