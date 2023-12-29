import random
class Horse(object):
    
    def __init__(self, nom, couleur) -> None:
        self.nom = nom
        self.couleur = couleur
        self.position = 0
        self.etat = False
    
    def jouer_tour(self, joueur):
        input(f"{joueur.nom} Appuyer sur Entrée pour lancer le dé")
        de = self.lancerDe()
        self.avancer_cheval(joueur, de)
        self.afficher_plateau()
        print(f"{joueur.nom} a avancé jusque la position {joueur.position}")

    def ajouter_cheval(self, cheval)->list:
        if self.couleur.cheval == "Jaune":
            self.plateau.append(cheval)
            self.position = [0]
        if self.couleur.cheval == "Rouge":
            self.plateau.append(cheval)
            self.position = [15]
        if self.couleur.cheval == "Bleu":
            self.plateau.append(cheval)
            self.position = [29]
        if self.couleur.cheval == "Vert":
            self.plateau.append(cheval)
            self.position = [43]

    
    def afficher_positions(self)-> str:
        for cheval in self.chevaux:
            print(f"{cheval.nom}: {cheval.position}")

    def sauter(self, cheval_1,cheval_2):
        if cheval_1.position == cheval_2.position:
            cheval_1.position = cheval_2.position
            self.plateau.pop(cheval_2)
        if cheval_2.position == cheval_1.position:
            cheval_2.position = cheval_1.position
            self.plateau.pop(cheval_2)

    def victoire( self, cheval)-> str:
        while self.nbtour == False:
            return self.afficher_positions
        return ' vous avais gagner '

    def __str__(self) -> str:
        l1 = f"**** {self.nom} ****\n"
        l2 = f"  - couleur : {self.couleur}\n"
        return l1 + l2
