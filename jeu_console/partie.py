import random
from joueur import * 
import keyboard 


class Partie:
    def __init__(self, joueurs):
        self.joueurs = joueurs
        self.joueur_actuel = random.choice(joueurs)
        self.lancer_de = 0
        self.fin_de_partie = False

    def lancer_le_de(self):
        self.lancer_de = random.randint(1, 6)

    def joueur_suivant(self):
        self.joueur_actuel = self.joueurs[(self.joueurs.index(self.joueur_actuel) + 1) % len(self.joueurs)]

    def kill(self, joueur1, joueur2):
        if joueur1.position == joueur2.position and joueur1 != joueur2:
            print(f"{joueur1.identifiant} a tué {joueur2.identifiant}!")
            joueur2.score = 0
            joueur2.position = 0
            print(f"{joueur2.identifiant} faut faire 6 pour rejouer")

    def jouer_tour(self, joueur):
        if not self.fin_de_partie:
            self.lancer_le_de()
            joueur.deplacer_pion(self.lancer_de)
            if joueur.position == len(self.joueurs) * 10:
                self.fin_de_partie = True
            else:
                joueur.score += 1
                if joueur.position == self.joueurs[1].position:
                    self.kill(joueur, self.joueurs[1])
                if joueur.score >= 100:
                    self.fin_de_partie = True
                else:
                    print(f"{joueur.identifiant} est sur la case {joueur.position}.")
                    while True:
                        if keyboard.is_pressed('a'):
                            keyboard.read_key()
                            break

    def jouer_tout(self):
        random.shuffle(self.joueurs)
        while not self.fin_de_partie:
            for joueur in self.joueurs:
                self.jouer_tour(joueur)
                if joueur.position >= 100:
                    if self.joueurs[:2] == [joueur, joueur.autre_joueur()]:
                        print(f'{joueur.identifiant} et {joueur.autre_joueur()} sont liés.')
                    else:
                        print(f'{joueur.identifiant} a gagner !')
                    self.fin_de_partie = True
                    break
                else:
                    while True:
                        if keyboard.is_pressed('a'):
                            keyboard.read_key()
                            break
