from deplacement import *
map1 = [
       [" |","┌", "-", " -", " -", "-", "┐", "●", "x", "●"," ┌", "-", " -", " -", "-","┐","|"],
       [" |","|", "s", " s", " s", "s", "|", "●", "1", "●", "|", "0", "0", "0", "0", " |","|"],
       [" |","|", "s", " s", " s", "s", "|", "●", "2", "●", "|", "0", "0", "0", "0", " |","|"],
       [" |","|", "s", " s", " s", "s", "|", "●", "3", "●", "|", "0", "0", "0", "0", " |","|"],
       [" |","|", "s", " s", " s", "s", "|", "●", "4", "●", "|", "0", "0", "0", "0", " |","|"],
       [" |","└", "-", " -", " -", "-", "┘", "●", "5", "●", "└", "-", "-", "-", "-", " ┘","|"],
       [" |", "●", " ●", " ●", "●", "●", "●","●", "6", "●", "●", "●", "●", "●", "●", "●" ," |"],
       [" |", "x", " 1", " 2", "3", "4", "5", "6","v", "6", "5", "4", "3", "2", "1",  "x"," |"],
       [" |", "●", " ●", " ●", "●", "●", "●","●", "6", "●", "●", "●", "●", "●", "●", "●" ," |"],
       [" |","┌", "-", " -", " -", "-", "┐", "●", "5", "●", "┌", "-", "-", "-", "-", " ┐","|"],
       [" |","|", "s", " s", " s", "s", "|", "●", "4", "●", "|", "0", "0", "0", "0", " |","|"],
       [" |","|", "s", " s", " s", "s", "|", "●", "3", "●", "|", "0", "0", "0", "0", " |","|"],
       [" |","|", "s", " s", " s", "s", "|", "●", "2", "●", "|", "0", "0", "0", "0", " |","|"],
       [" |","|", "s", " s", " s", "s", "|", "●", "1", "●", "|", "0", "0", "0", "0", " |","|"],
       [" |","└", "-", " -", " -", "-", "┘", "●", "x", "●", "└", "-", " -", " -", "-","┘","|"],
       ]


def afficher_map(map):
    """
    Affiche la map dans la console
    
    >>> afficher_map(map1)

    """
    for line in map:
       print()
       for case in line:
           print(case, end="  ")


afficher_map(map1)