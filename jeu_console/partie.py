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
        print(f"{self.joueur_actuel.identifiant} a lancé un {self.lancer_de}")

    def jouer_tour(self):
        self.joueur_actuel.score += self.lancer_de
        print(
            f"{self.joueur_actuel.identifiant} a maintenant un score de {self.joueur_actuel.score}")

    def joueur_suivant(self):
        self.joueur_actuel = self.joueurs[(self.joueurs.index(
            self.joueur_actuel) + 1) % len(self.joueurs)]

    def jouer_tout(self):
        random.shuffle(self.joueurs)  # shuffle the joueurs list
        while not self.fin_de_partie:
            for joueur in self.joueurs:
                while True:
                    try:
                        if input(f'Appuyez sur "a" pour que {joueur.identifiant} joue...').lower() == 'a':
                            break
                    except:
                        pass

                self.lancer_le_de()
                self.jouer_tour(joueur)

                while joueur.score >= 100:
                    if joueur.score > 100:
                        print(f'{joueur.identifiant} a été éliminé.')
                    else:
                        print(f'{joueur.identifiant} et {joueur.autre_joueur()} sont à égalité.')

                    joueur.score = 0

                    if self.joueurs[0].score >= 100:
                        self.fin_de_partie = True
                        print(f'Félicitations, {self.joueur_actuel.identifiant} a gagné !')
                        break

                    random.shuffle(self.joueurs)  # shuffle the joueurs list after each player's turn

                    if self.joueurs[0].score >= 100:
                        self.fin_de_partie = True
                        print(f'Félicitations, {self.joueur_actuel.identifiant} a gagné !')
                        break

        self.joueur_actuel = self.joueurs[0]  # Reset the current player to the first player in the original list after the game is over

    def jouer_tour(self, joueur):
        joueur.score += self.lancer_de
        print(f"{joueur.identifiant} a maintenant un score de {joueur.score}")