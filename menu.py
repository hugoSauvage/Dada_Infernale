import pygame



pygame.init()

#Pour créer une fenetre
screen = pygame.display.set_mode((0,0), pygame.NOFRAME)
# screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("The Whorses")
# pygame.display.set_icon("./assets/Cheval/ChevalVert.png")

boutonJouer = pygame.image.load("./assets/Boutons/boutonJouer.png").convert_alpha()
boutonQuitter = pygame.image.load("./assets/Boutons/boutonQuitter.png").convert_alpha()
boutonReglages = pygame.image.load("./assets/Boutons/boutonReglages.png").convert_alpha()
print("size of image is (width,height):", boutonQuitter.get_size())



def is_mouse_over_button(button, mouse_pos):
    button_rect = button.get_rect()
    return button_rect.collidepoint(mouse_pos)


# def open_parameter():
#     # Code to open the parameter window goes here
#     pass


def open_game():
    # Create a new Pygame window
    parameter_screen = pygame.display.set_mode((0, 0), pygame.NOFRAME)
    pygame.display.set_caption("Paramètre")

    # Load the parameter window background image
    parameter_background = pygame.image.load("./assets/Parametre/background.png").convert_alpha()

    # Load the parameter window buttons
    boutonRetour = pygame.image.load("./assets/Boutons/boutonRetour.png").convert_alpha()

    # Boucle jeu 
    run_game = True
    while run_game:
        # Fill the screen with the background color
        parameter_screen.fill((52, 78, 91))

        # Draw the background image
        parameter_screen.blit(parameter_background, (0, 0))

        # Draw the buttons
        parameter_screen.blit(boutonRetour, (0, 0))

        # Evenement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if is_mouse_over_button(boutonRetour, mouse_pos):
                    run_game = False

        # Update the display
        pygame.display.flip()
        pygame.display.update()

    # Close the pa



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
            mouse_pos = event.pos
            if is_mouse_over_button(boutonParametre, mouse_pos):
                open_game()
            elif is_mouse_over_button(boutonQuitter, mouse_pos):
                run = False
        elif event.type == pygame.K_F4:
            pygame.quit()
            
    pygame.display.flip()
    pygame.display.update()

pygame.quit()

