import pygame

pygame.init()

#Pour créer une fenetre
screen = pygame.display.set_mode((0,0), pygame.NOFRAME)
# screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("The Whorses")
# pygame.display.set_icon("./assets/Cheval/ChevalVert.png")

boutonJouer = pygame.image.load("./assets/Boutons/boutonJouer.png").convert_alpha()
boutonQuitter = pygame.image.load("./assets/Boutons/boutonQuitter.png").convert_alpha()

print("size of image is (width,height):", boutonQuitter.get_size())
#Boucle jeu 
run = True
while run:
    
    screen.fill((52, 78, 91))
    screen.blit(boutonJouer, (0,300))
    screen.blit(boutonQuitter,(800,700))

    
    #Evenement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #faire bouton clickable ici avec une zone entre autant et autant qui fera une action soit quitter le jeu sur le bouton quitter 
            mouse_pos = event.pos
            print("Hello")
        elif event.type == pygame.K_F4:
            pygame.quit()
            
    pygame.display.flip()
    pygame.display.update()

pygame.quit()