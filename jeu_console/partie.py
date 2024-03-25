import random
from joueur import * 


class Partie:
    def __init__(self, joueurs):
        self.joueurs = joueurs
        self.joueur_actuel = random.choice(joueurs)
        self.lancer_de = 0
        self.fin_de_partie = False

    def lancer_le_de(self):
        self.lancer_de = random.randint(1, 6)

    def jouer_tour(self, joueur):
        self.lancer_le_de()
        joueur.score += self.lancer_de
        print(f"{joueur.identifiant} has a score of {joueur.score} after this turn")

    def joueur_suivant(self):
        self.joueur_actuel = self.joueurs[(self.joueurs.index(self.joueur_actuel) + 1) % len(self.joueurs)]

    def jouer_tout(self):
        random.shuffle(self.joueurs)
        while not self.fin_de_partie:
            for joueur in self.joueurs:
                self.jouer_tour(joueur)
                if joueur.score >= 100:
                    if self.joueurs[:2] == [joueur, joueur.altre_joueur()]:
                        print(f'{joueur.identifiant} and {joueur.altre_joueur()} are tied.')
                    else:
                        print(f'{joueur.identifiant} has won!')
                    self.fin_de_partie = True
                    break

        self.joueur_actuel = self.joueurs[0]

         