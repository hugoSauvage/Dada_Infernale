class Plateau:
    def __init__(self):
        self.plateau = [(i, "libre") for i in range(48)]
        self.joueurs = {}

    def ajouter_joueur(self, joueur_id, position_depart):
        self.joueurs[joueur_id] = {'position': position_depart, 'chevaux': [None, None]}

    def deplacer_cheval_plateau(self, joueur_id, numero_cheval, deplacements):
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
    
    def __str__(self) -> str:
        return f"{self.plateau}"
    

plateauTest = Plateau()
print(plateauTest)