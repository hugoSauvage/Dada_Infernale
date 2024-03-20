import random

class Plateau:
    def __init__(self):
        self.plateau = [[None for _ in range(12)] for _ in range(6)]
        self.joueurs = {}

    def ajouter_joueur(self, joueur_id, position_depart):
        self.joueurs[joueur_id] = {'position': position_depart, 'chevaux': [None, None]}

    def deplacer_cheval(self, joueur_id, numero_cheval, deplacements):
        position_cheval = self.joueurs[joueur_id]['chevaux'][numero_cheval]
        nouvelle_position = (position_cheval[0] + deplacements, position_cheval[1])
        if nouvelle_position[0] >= 0 and nouvelle_position[0] < 6 and nouvelle_position[1] >= 0 and nouvelle_position[1] < 12:
            if self.plateau[nouvelle_position[0]][nouvelle_position[1]] is None:
                self.plateau[position_cheval[0]][position_cheval[1]] = None
                self.plateau[nouvelle_position[0]][nouvelle_position[1]] = joueur_id
                self.joueurs[joueur_id]['chevaux'][numero_cheval] = nouvelle_position
            elif self.plateau[nouvelle_position[0]][nouvelle_position[1]] == joueur_id:
                self.plateau[position_cheval[0]][position_cheval[1]] = None
                self.plateau[nouvelle_position[0]][nouvelle_position[1]] = joueur_id
                self.joueurs[joueur_id]['chevaux'][numero_cheval] = nouvelle_position
            elif self.plateau[nouvelle_position[0]][nouvelle_position[1]] != joueur_id:
                self.joueurs[joueur_id]['chevaux'][numero_cheval] = None
                self.joueurs[joueur_id][joueur_id] = nouvelle_position
                self.plateau[nouvelle_position[0]][nouvelle_position[1]] = joueur_id
        else:
            return False
        return True

    def est_partie_terminee(self):
        for joueur in self.joueurs.values():
            if joueur['chevaux'][0] is not None and joueur['chevaux'][1] is not None and all([p == 5 for p in joueur['chevaux']]):
                return True
        return False
    
class Jeu:
    def __init__(self):
        self.plateau = Plateau()
        self.joueurs = {}
        self.joueur_actuel_id = None

    def ajouter_joueur(self, joueur_id, position_depart):
        self.joueurs[joueur_id] = {'position': position_depart, 'chevaux': [None, None]}

    def lancer_de(self):
        return random.randint(1, 6)

    def deplacer_cheval(self, joueur_id, numero_cheval):
        deplacements = self.lancer_de()
        if self.plateau.deplacer_cheval(joueur_id, numero_cheval, deplacements):
            self.joueurs[joueur_id]['position'] += deplacements

    def jouer_partie(self, joueurs):
        for i, joueur in joueurs.items():
            self.ajouter_joueur(i, joueur)
        self.joueur_actuel_id = random.choice(list(joueurs.keys()))

        while True:
            if self.plateau.est_partie_terminee():
                print(f"Le joueur {self.joueur_actuel_id} gagne!")
                break

            numero_cheval = None
            while numero_cheval is None:
                print

# Définir les positions de départ pour chaque joueur
positions_depart = {
    1: (0, 0),  # Les chevaux du joueur 1 commencent sur la ligne 0, colonnes 0 et 1
    2: (0, 11),  # Les chevaux du joueur 2 commencent sur la ligne 0, colonnes 11 et 12
    3: (5, 0),  # Les chevaux du joueur 3 commencent sur la ligne 5, colonnes 0 et 1
    4: (5, 11)  # Les chevaux du joueur 4 commencent sur la ligne 5, colonnes 11 et 12
}

# Créer une nouvelle instance de jeu
jeu = Jeu()

# Ajouter des joueurs au jeu
for joueur_id, position in positions_depart.items():
    jeu.ajouter_joueur(joueur_id, position)

# Commencer le jeu
jeu.jouer_partie(positions_depart)
