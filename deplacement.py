from Horse import *
# déplacement du personnage sur la map

def deplacer_vers_haut(map):
    """
    Déplace le personnage représenté par "🧙" vers le haut sur la carte.
    
    >>> deplacer_vers_haut(map1)

    """
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "🧙":
                map[y][x] = 0
                if y > 0 and map[y-1][x]:
                    map[y-1][x] = "🧙"
                return


def deplacer_vers_bas(map):
    """
    Déplace le personnage représenté par "🧙" vers le bas sur la carte.
    
    >>> deplacer_vers_bas(map1)

    """
    for y in range(len(map)-1, -1, -1):
        for x in range(len(map[y])):
            if map[y][x] == "🧙":
                map[y][x] = 0
                if y < len(map)-1 and map[y+1][x]:
                    map[y+1][x] = "🧙"
                return


def deplacer_vers_gauche(map):
    """
    Déplace le personnage représenté par "🧙" vers la gauche sur la carte.
    
    >>> deplacer_vers_gauche(map1)

    """
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "🧙":
                map[y][x] = 0
                if x > 0 and map[y][x-1]:
                    map[y][x-1] = "🧙"
                return


def deplacer_vers_droite(map):
    """
    Déplace le personnage représenté par "🧙" vers le droite sur la carte.
    
    >>> deplacer_vers_droite(map1)

    """
    for y in range(len(map)):
        for x in range(len(map[y])-1, -1, -1):
            if map[y][x] == "🧙":
                map[y][x] = 0
                if x < len(map[y])-1 and map[y][x+1]:
                    map[y][x+1] = "🧙"
                return

         
def afficher_map(map):
    """
    Affiche la map dans la console
    
    >>> afficher_map(map1)

    """
    for line in map:
       print()
       for case in line:
           print(case, end="  ")


