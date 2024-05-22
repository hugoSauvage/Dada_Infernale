from Cheval import Cheval
from joueur import Joueur
from partie import Partie

joueurs = [
    Joueur("Joueur1", "Rouge", 0),
    Joueur("Joueur2", "Bleu", 12),
    Joueur("Joueur3", "Vert", 24),
    Joueur("Joueur4", "Jaune", 36)
]

partie = Partie(joueurs)
partie.jouer_tout()