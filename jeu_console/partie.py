import keyboard

class Partie:
    def __init__(self, joueurs):
        self.joueurs = joueurs
        self.joueur_actuel = joueurs[0]
        self.fin_de_partie = False

    def joueur_suivant(self):
        index_joueur_actuel = self.joueurs.index(self.joueur_actuel)
        index_prochain_joueur = (index_joueur_actuel + 1) % len(self.joueurs)
        self.joueur_actuel = self.joueurs[index_prochain_joueur]

    def kill(self, cheval1, cheval2):
        if cheval1.position == cheval2.position and cheval1 != cheval2:
            print(f"{cheval1.joueur.identifiant} a tué {cheval2.joueur.identifiant}!")
            cheval2.position = -1
            cheval2.estDansLEcurie = True
    
    def afficher_positions(self):
        for joueur in self.joueurs:
            print(f"Joueur {joueur.identifiant}:")
            for i, cheval in enumerate(joueur.chevaux):
                print(f"  Cheval {i + 1}: Position {cheval.position}")

 
    def jouer_tour(self, joueur):
        print(f"\nTour du joueur {joueur.identifiant}")

        # Attendre que le joueur appuie sur 'a' pour lancer le dé
        print(f"{joueur.identifiant}, appuyez sur 'a' pour lancer le dé.")
        while True:
            if keyboard.is_pressed('a'):
                keyboard.read_key()  # Pour consommer la touche pressée
                break

        lancer = joueur.lancer_de()
        print(f"{joueur.identifiant} a lancé le dé et a obtenu {lancer}.")

        if lancer == 6:
            # Si le joueur a fait un six, proposer de sortir un cheval
            print(f"{joueur.identifiant}, vous avez fait un six! Voulez-vous sortir un nouveau cheval de l'écurie ? (y/n)")
            while True:
                if keyboard.is_pressed('y'):
                    keyboard.read_key()
                    cheval = next((c for c in joueur.chevaux if c.estDansLEcurie), None)
                    if cheval:
                        cheval.sortirEcurie()
                        print(f"{joueur.identifiant} a sorti un cheval de l'écurie.")
                    else:
                        print("Tous les chevaux sont déjà sur le plateau.")
                    break
                elif keyboard.is_pressed('n'):
                    keyboard.read_key()
                    # Si le joueur dit non, déplacer automatiquement un cheval de 6
                    cheval = next((c for c in joueur.chevaux if not c.estDansLEcurie), None)
                    if cheval:
                        cheval.seDeplacer(6)
                        print(f"{joueur.identifiant} a déplacé un cheval de 6 cases.")
                    break
        else:
            # Déplacer un cheval (exemple simplifié: toujours déplacer le premier cheval non dans l'écurie)
            chevaux_disponibles = [c for c in joueur.chevaux if not c.estDansLEcurie]
            if chevaux_disponibles:
                print("Chevaux disponibles à déplacer : ")
                for i, cheval in enumerate(chevaux_disponibles):
                    print(f"{i + 1}. Cheval à la position {cheval.position}")

                while True:
                    try:
                        choix_cheval = int(input("Choisissez le numéro du cheval à déplacer : "))
                        if 0 < choix_cheval <= len(chevaux_disponibles):
                            cheval = chevaux_disponibles[choix_cheval - 1]
                            cheval.seDeplacer(lancer)
                            print(f"{joueur.identifiant} a déplacé un cheval de {lancer} cases.")
                            break
                        else:
                            print("Choix invalide. Veuillez sélectionner un numéro de cheval valide.")
                    except ValueError:
                        print("Veuillez saisir un numéro entier.")

        # Vérifier si la partie est terminée (par exemple, un joueur a tous ses chevaux sur la dernière case)
        self.afficher_positions()  # Afficher les positions de tous les chevaux après ce tour
            
            
    def jouer_tout(self):
        while not self.fin_de_partie:
            for joueur in self.joueurs:
                self.jouer_tour(joueur)
                if self.fin_de_partie:
                    break
            self.joueur_suivant()


