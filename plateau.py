from deplacement import *
map1 = [
       [" |","┌", "-", " -", " -", "-", "┐", "●", "J", "M"," ┌", "-", " -", " -", "-","┐","|"],
       [" |","|", "0", " 0", " 0", "0", "|", "●", "1", "●", "|", "0", "0", "0", "0", " |","|"],
       [" |","|", "0", " 0", " 0", "0", "|", "●", "2", "●", "|", "0", "0", "0", "0", " |","|"],
       [" |","|", "0", " 0", " 0", "0", "|", "●", "3", "●", "|", "0", "0", "0", "0", " |","|"],
       [" |","|", "0", " 0", " 0", "0", "|", "●", "4", "●", "|", "0", "0", "0", "0", " |","|"],
       [" |","└", "-", " -", " -", "-", "┘", "●", "5", "●", "└", "-", "-", "-", "-", " ┘","|"],
       [" |", "M", " ●", " ●", "●", "●", "●","●", "6", "●", "●", "●", "●", "●", "●","●" ," |"],
       [" |", "R", " 1", " 2", "3", "4", "5", "6","G", "6", "5", "4", "3", "2", "1","B", " |"],
       [" |", "●", " ●", " ●", "●", "●", "●","●", "6", "●", "●", "●", "●", "●", "●","M" ," |"],
       [" |","┌", "-", " -", " -", "-", "┐", "●", "5", "●", "┌", "-", "-", "-", "-", " ┐","|"],
       [" |","|", "0", " 0", " 0", "0", "|", "●", "4", "●", "|", "0", "0", "0", "0", " |","|"],
       [" |","|", "0", " 0", " 0", "0", "|", "●", "3", "●", "|", "0", "0", "0", "0", " |","|"],
       [" |","|", "0", " 0", " 0", "0", "|", "●", "2", "●", "|", "0", "0", "0", "0", " |","|"],
       [" |","|", "0", " 0", " 0", "0", "|", "●", "1", "●", "|", "0", "0", "0", "0", " |","|"],
       [" |","└", "-", " -", " -", "-", "┘", "M", "V", "●", "└", "-", " -", " -", "-","┘","|"],

       ]

import random

class JeuDeSociete:
    def __init__(self, map1):
        self.map = map1
        self.chevaux = {"hv": {"position": "0", "termine": False},
                        "hr": {"position": "0", "termine": False},
                        "hj": {"position": "0", "termine": False},
                        "hb": {"position": "0", "termine": False}}

    def lancer_de(self):
        return random.randint(1, 6)

    def deplacer_cheval(self, couleur):
        de_resultat = self.lancer_de()
        position_actuelle = self.chevaux[couleur]["position"]

        if position_actuelle == "0" and de_resultat == 6:
            # Le cheval apparaît sur le "1" car il a obtenu un 6
            self.chevaux[couleur]["position"] = "M"
        else:
            # Déplacement normal sur les "●"
            nouvelle_position = self.avancer_sur_les_cases(position_actuelle, de_resultat)
            self.chevaux[couleur]["position"] = nouvelle_position

            # Vérification si le cheval a terminé son tour
            if nouvelle_position in ["hv", "hr", "hj", "hb"]:
                self.chevaux[couleur]["termine"] = True

    def avancer_sur_les_cases(self, position_actuelle, de_resultat):
        # Logique de déplacement sur les cases "●"
        if position_actuelle == "0":
            position_actuelle = 0
            print("Tu y es presque, mais tu n'as pas fait six recomptes.")
        if position_actuelle == "M" and "R" and "J" and "B" and "V":
            valeur = 1
            position_actuelle = valeur
            nouvelle_position = int(position_actuelle) + de_resultat
            if nouvelle_position > 15:
                nouvelle_position = 15  # Limite la position à 15
            print(f' tu parcouru {nouvelle_position - position_actuelle} est maintenant tu est au "●" {nouvelle_position}! ')
            return str(nouvelle_position)
        if position_actuelle == "●":
            valeur = 1
            position_actuelle = valeur
            nouvelle_position = int(position_actuelle) + de_resultat
            if nouvelle_position > 15:
                nouvelle_position = 15  # Limite la position à 15
            print(f' tu parcouru  {nouvelle_position - position_actuelle} est maintenant tu est au "●" {nouvelle_position}! ')
            return str(nouvelle_position)

    def __str__(self) -> dict:
        return self.chevaux

# Exemple d'utilisation
jeu = JeuDeSociete(map1)

# Déplacer le cheval rouge
jeu.deplacer_cheval("hr")
print("Position du cheval rouge:", jeu.chevaux["hr"]["position"])
print("Tour terminé:", jeu.chevaux["hr"]["termine"])
print(jeu.__str__)
