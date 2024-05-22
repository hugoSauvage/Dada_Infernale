import pygame

pygame.init()

# Pour créer une fenetre
screen = pygame.display.set_mode((0, 0), pygame.NOFRAME)
pygame.display.set_caption("The Whorses")

# Charger l'image de la carte
map = pygame.image.load("./assets/Maps/Whorses.png").convert_alpha()

# Redimensionner l'image de la carte
map = pygame.transform.scale(map, (1600, 1000))

# Charger l'image du bouton
bouton_quitter = pygame.image.load("./assets/Boutons/boutonQuitter.png").convert_alpha()
bouton_des = pygame.image.load("./assets/Boutons/boutonLancerDeDes.png").convert_alpha()

# Créer un objet Rect pour le bouton
bouton_rect = bouton_quitter.get_rect()

# Définir la position du bouton
bouton_rect.x = 70
bouton_rect.y = 900

b1 = pygame.image.load("./assets/Cheval/chevalBleu.png").convert_alpha()
b2 = pygame.image.load("./assets/Cheval/chevalBleu.png").convert_alpha()
b3 = pygame.image.load("./assets/Cheval/chevalBleu.png").convert_alpha()
b4 = pygame.image.load("./assets/Cheval/chevalBleu.png").convert_alpha()
r1 = pygame.image.load("./assets/Cheval/chevalRouge.png").convert_alpha()
r2 = pygame.image.load("./assets/Cheval/chevalRouge.png").convert_alpha()
r3 = pygame.image.load("./assets/Cheval/chevalRouge.png").convert_alpha()
r4 = pygame.image.load("./assets/Cheval/chevalRouge.png").convert_alpha()
j1 = pygame.image.load("./assets/Cheval/chevalJaune.png").convert_alpha()
j2 = pygame.image.load("./assets/Cheval/chevalJaune.png").convert_alpha()
j3 = pygame.image.load("./assets/Cheval/chevalJaune.png").convert_alpha()
j4 = pygame.image.load("./assets/Cheval/chevalJaune.png").convert_alpha()
v1 = pygame.image.load("./assets/Cheval/chevalVert.png").convert_alpha()
v2 = pygame.image.load("./assets/Cheval/chevalVert.png").convert_alpha()
v3 = pygame.image.load("./assets/Cheval/chevalVert.png").convert_alpha()
v4 = pygame.image.load("./assets/Cheval/chevalVert.png").convert_alpha()

b1 = pygame.transform.scale(b1, (50, 50))
b2 = pygame.transform.scale(b2, (50, 50))
b3 = pygame.transform.scale(b3, (50, 50))
b4 = pygame.transform.scale(b4, (50, 50))
r1 = pygame.transform.scale(r1, (50, 50))
r2 = pygame.transform.scale(r2, (50, 50))
r3 = pygame.transform.scale(r3, (50, 50))
r4 = pygame.transform.scale(r4, (50, 50))
j1 = pygame.transform.scale(j1, (50, 50))
j2 = pygame.transform.scale(j2, (50, 50))
j3 = pygame.transform.scale(j3, (50, 50))
j4 = pygame.transform.scale(j4, (50, 50))
v1 = pygame.transform.scale(v1, (50, 50))
v2 = pygame.transform.scale(v2, (50, 50))
v3 = pygame.transform.scale(v3, (50, 50))
v4 = pygame.transform.scale(v4, (50, 50))

cases = [(740, 950), (740, 875), (740, 800), (740, 725), (740, 650), (740, 575),
         (670, 575), (600, 575), (530, 575), (460, 575), (395, 575), 
         (395, 485), (395, 390),
         (465, 390), (535, 390), (605, 390), (675, 390), (745, 390), 
         (745, 320), (745, 250), (745, 180), (745, 110), (745, 30), 
         (825, 30), (905, 30),
         (905, 100), (905, 180), (905, 250), (905, 320), (905, 390),
         (975, 390), (1035, 390), (1105, 390), (1175, 390), (1240, 390),
         (1240, 485), (1240, 575),
         (1180, 575), (1110, 575), (1050, 575), (980, 575), (910, 575),
         (910, 650), (910, 720), (910, 800), (910, 870), (910, 940),
         (830, 940)]

# Boucle principale du jeu
running = True
while running:
    # Traitement des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifier si le bouton est cliqué
            if bouton_rect.collidepoint(event.pos):
                running = False


    # Dessin de l'image de la carte
    screen.blit(map, (50, 25))
    screen.blit(bouton_des, (1415, 60))

    # Dessin du bouton
    screen.blit(bouton_quitter, bouton_rect)

    screen.blit(b1, (1000, 80))
    screen.blit(b2, (1075, 80))
    screen.blit(b3, (1150, 80))
    screen.blit(b4, (1225, 80))
    screen.blit(r1, (1000, 700))
    screen.blit(r2, (1075, 700))
    screen.blit(r3, (1150, 700))
    screen.blit(r4, (1225, 700))
    screen.blit(j1, (425, 80))
    screen.blit(j2, (500, 80))
    screen.blit(j3, (575, 80))
    screen.blit(j4, (650, 80))
    screen.blit(v1, (425, 700))
    screen.blit(v2, (500, 700))
    screen.blit(v3, (575, 700))
    screen.blit(v4, (650, 700))
    
    screen.blit(v4, (740, 950))
    screen.blit(v4, (740, 875))
    screen.blit(v4, (740, 800))
    screen.blit(v4, (740, 725))
    screen.blit(v4, (740, 650))
    screen.blit(v4, (740, 575))
    
    screen.blit(v4, (670, 575))
    screen.blit(v4, (600, 575))
    screen.blit(v4, (530, 575))
    screen.blit(v4, (460, 575))
    screen.blit(v4, (395, 575))
    
    screen.blit(v4, (395, 485))
    screen.blit(v4, (395, 390))
    
    screen.blit(v4, (465, 390))
    screen.blit(v4, (535, 390))
    screen.blit(v4, (605, 390))
    screen.blit(v4, (675, 390))
    screen.blit(v4, (745, 390))
    
    screen.blit(v4, (745, 320))
    screen.blit(v4, (745, 250))
    screen.blit(v4, (745, 180))
    screen.blit(v4, (745, 110))
    screen.blit(v4, (745, 30))
    
    screen.blit(v4, (825, 30))
    screen.blit(v4, (905, 30))
    
    screen.blit(v4, (905, 100))
    screen.blit(v4, (905, 180))
    screen.blit(v4, (905, 250))
    screen.blit(v4, (905, 320))
    screen.blit(v4, (905, 390))
    
    screen.blit(v4, (975, 390))
    screen.blit(v4, (1035, 390))
    screen.blit(v4, (1105, 390))
    screen.blit(v4, (1175, 390))
    screen.blit(v4, (1240, 390))
    
    screen.blit(v4, (1240, 485))
    screen.blit(v4, (1240, 575))
    
    screen.blit(v4, (1180, 575))
    screen.blit(v4, (1110, 575))
    screen.blit(v4, (1050, 575))
    screen.blit(v4, (980, 575))
    screen.blit(v4, (910, 575))
    
    screen.blit(v4, (910, 650))
    screen.blit(v4, (910, 720))
    screen.blit(v4, (910, 800))
    screen.blit(v4, (910, 870))
    screen.blit(v4, (910, 940))
    
    screen.blit(v4, (830, 940))
    
    
    # Mise à jour de l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
