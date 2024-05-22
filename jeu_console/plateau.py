from Cheval import *
class Plateau:
    def __init__(self):
        self.plateau = [(i, "libre") for i in range(48)]
        self.joueurs = {}
        self.paradis = [(i, "libre") for i in range(7)]

    def ajouter_joueur(self, joueur_id, position_depart):
        self.joueurs[joueur_id] = {'position': position_depart, 'chevaux': [None, None]}

    def ajouter_paradis(self, position):
        self.paradis.append(position)

    def deplacer_cheval_plateau(self, joueur_id, numero_cheval, deplacements):
        # Obtient la position actuelle du cheval avec le numéro donné pour le
        # joueur avec l'identifiant donné.
        position_cheval = self.joueurs[joueur_id]['chevaux'][numero_cheval]
        # Calcule la nouvelle position du cheval en ajoutant les déplacements donnés
        # à la position actuelle.
        nouvelle_position = (position_cheval[0] + deplacements, position_cheval[1])
        # Vérifie si la nouvelle position est dans les limites du plateau et si elle
        # n'est pas déjà occupée par un autre cheval.
        if nouvelle_position[0] >= 0 and nouvelle_position[0] < 6 and nouvelle_position[1] >= 0 and nouvelle_position[1] < 12:
            if self.plateau[nouvelle_position[0]][nouvelle_position[1]] is None:
                # Si la nouvelle position est libre, met à jour la position du cheval
                # dans le dictionnaire joueurs et la liste plateau.
                self.plateau[position_cheval[0]][position_cheval[1]] = None
                self.plateau[nouvelle_position[0]][nouvelle_position[1]] = joueur_id
                self.joueurs[joueur_id]['chevaux'][numero_cheval] = nouvelle_position
            elif self.plateau[nouvelle_position[0]][nouvelle_position[1]] == joueur_id:
                # Si la nouvelle position est déjà occupée par le même cheval,
                # met à jour la position du cheval dans le dictionnaire joueurs
                # et la liste plateau.
                self.plateau[position_cheval[0]][position_cheval[1]] = None
                self.plateau[nouvelle_position[0]][nouvelle_position[1]] = joueur_id
                self.joueurs[joueur_id]['chevaux'][numero_cheval] = nouvelle_position
            elif self.plateau[nouvelle_position[0]][nouvelle_position[1]] != joueur_id:
                # Si la nouvelle position est déjà occupée par un autre cheval,
                # ne met pas à jour la position du cheval dans le dictionnaire joueurs
                # et la liste plateau.
                self.joueurs[joueur_id]['chevaux'][numero_cheval] = None
                self.joueurs[joueur_id][joueur_id] = nouvelle_position
                self.plateau[nouvelle_position[0]][nouvelle_position[1]] = joueur_id
        else:
            # Si la nouvelle position est en dehors des limites du plateau, ne met pas à jour
            # la position du cheval dans le dictionnaire joueurs et la liste plateau.
            return False
        return True

    def est_partie_terminee(self):
        for joueur in self.joueurs.values():
            if joueur['chevaux'][0] is not None and joueur['chevaux'][1] is not None and all([p in self.paradis for p in joueur['chevaux']]):
                return True
        return False

    def __str__(self) -> str:
        # Retourne le plateau sous forme de chaîne de caractères.
        return f"{self.plateau}"

plateauTest = Plateau()
print(plateauTest)