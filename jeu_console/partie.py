import random
from plateau import Plateau


class Partie:
    def __init__(self, joueurs):
        self.joueurs = joueurs
        self.joueur_actuel = random.choice(joueurs)
        self.lancer_de = 0
        self.fin_de_partie = False

    def lancer_le_de(self):
        self.lancer_de = random.randint(1, 6)
        print(f"{self.joueur_actuel.identifiant} a lancé un {self.lancer_de}")

    def jouer_tour(self):
        self.joueur_actuel.score += self.lancer_de
        print(
            f"{self.joueur_actuel.identifiant} a maintenant un score de {self.joueur_actuel.score}")

    def joueur_suivant(self):
        self.joueur_actuel = self.joueurs[(self.joueurs.index(
            self.joueur_actuel) + 1) % len(self.joueurs)]

    def boucle_de_jeu(self):
        while not self.fin_de_partie:
            self.lancer_le_de()
            self.jouer_tour()
            self.joueur_suivant()
            if self.joueur_actuel.score >= 100:
                self.fin_de_partie = True
