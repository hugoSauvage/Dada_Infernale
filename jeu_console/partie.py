import random
from Cheval import *
from plateau import *
import keyboard 

class Partie:
    def __init__(self, joueurs):
        self.joueurs = joueurs
        self.joueur_actuel = joueurs[0]
        self.lancer_de = 0
        self.fin_de_partie = False


    def joueur_suivant(self):
        # Obtient l'index du joueur actuel dans la liste joueurs.
        index_joueur_actuel = self.joueurs.index(self.joueur_actuel)
        # Calcule l'index du prochain joueur dans la liste joueurs.
        index_prochain_joueur = (index_joueur_actuel + 1) % len(self.joueurs)
        # Assigne le prochain joueur à l'attribut joueur_actuel.
        self.joueur_actuel = self.joueurs[index_prochain_joueur]

    def kill(self, joueur1, joueur2):
        # Vérifie si les positions des deux joueurs sont les mêmes et s'ils ne sont
        # pas le même joueur.
        if joueur1.position == joueur2.position and joueur1 != joueur2:
            # Affiche un message indiquant que le premier joueur a tué le
            # deuxième joueur.
            print(f"{joueur1.identifiant} a tué {joueur2.identifiant}!")
            # Réinitialise le score et la position du deuxième joueur.
            joueur2.score = 0
            joueur2.position = 0
            # Affiche un message indiquant que le deuxième joueur doit obtenir un 6
            # pour rejouer.
            print(f"{joueur2.identifiant} doit faire un 6 pour rejouer.")

    def jouer_tour(self, joueur):
        # Vérifie si la partie n'est pas terminée.
        if not self.fin_de_partie:
            # Génère un nombre aléatoire entre 1 et 6 et l'assigne à l'attribut
            # lancer_de.
            n=self.lancer_de()
            # Déplace le cheval du joueur en fonction du nombre généré.
            Cheval.seDeplacer(n)
            # Vérifie si le cheval du joueur a atteint la dernière position.
            if joueur.position == len(self.joueurs) * 10:
                # Définit l'attribut fin_de_partie à True.
                self.fin_de_partie = True
            else:
                # Incrémente le score du joueur.
                joueur.score += 1
                # Vérifie si le cheval du joueur est à la même position que
                # le cheval du deuxième joueur.
                if joueur.position == self.joueurs[1].position:
                    # Appelle la méthode kill pour tuer le cheval du deuxième joueur.
                    self.kill(joueur, self.joueurs[1])
                # Vérifie si le score du joueur est supérieur ou égal à 100.
                if joueur.score >= 100:
                    # Définit l'attribut fin_de_partie à True.
                    self.fin_de_partie = True
                else:
                    # Affiche un message indiquant la position du joueur.
                    print(f"{joueur.identifiant} est sur la case {joueur.position}.")
                    # Attend que le joueur appuie sur la touche 'a'.
                    while True:
                        if keyboard.is_pressed('a'):
                            keyboard.read_key()
                            break

    def jouer_tout(self):
        # Mélange la liste joueurs.
        random.shuffle(self.joueurs)
        # Boucle jusqu'à ce que la partie soit terminée.
        while not self.fin_de_partie:
            # Parcourt tous les joueurs dans la liste joueurs.
            for joueur in self.joueurs:
                # Appelle la méthode jouer_tour pour jouer un tour pour le joueur
                # actuel.
                self.jouer_tour(joueur)
                # Vérifie si le cheval du joueur actuel a atteint la dernière
                # position.
                if joueur.position >= 100:
                    # Vérifie si le joueur actuel et le deuxième joueur sont liés.
                    if self.joueurs[:2] == [joueur, joueur.autre_joueur()]:
                        # Affiche un message indiquant que le joueur actuel
                        # et le deuxième joueur sont liés.
                        print(f'{joueur.identifiant} et {joueur.autre_joueur()} sont liés.')
                    else:
                        # Affiche un message indiquant que le joueur actuel a gagné.
                        print(f'{joueur.identifiant} a gagné !')
                    # Définit l'attribut fin_de_partie à True.
                    self.fin_de_partie = True
                    # Interrompt la boucle.
                    break