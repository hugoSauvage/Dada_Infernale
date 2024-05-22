import pygame
import Button
import sys

pygame.init()

#Pour créer une fenetre
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("The Whorses") #Titre Fenetre

#Chargement d'image en tout genre 
boutonJouer = pygame.image.load("./assets/Boutons/boutonJouer.png").convert_alpha()
boutonQuitter = pygame.image.load("./assets/Boutons/boutonQuitter.png").convert_alpha()
boutonReglages = pygame.image.load("./assets/Boutons/boutonReglages.png").convert_alpha()
fond = pygame.image.load("./assets/background.jpg").convert()



def is_mouse_over_button(button, mouse_pos):
    button_rect = button.get_rect()
    return button_rect.collidepoint(mouse_pos)

def options():
    pygame.display.set_caption("The Whorses : Options")

    screen.fill("Black")

    options_retour = Button(image=pygame.image.load("./assets/Boutons/boutonQuitter.png"), pos=(640, 250))

def play():
    pass
    


# def open_parameter():
#     # ouvrir parametre
#     pass

def main_menu():
    MENU_MOUSE_POS= pygame.mouse.get_pos()

    while True:
        screen.blit(fond, (0, 0))

        PLAY_BUTTON = Button(image=pygame.image.load("./assets/Boutons/boutonJouer.png") , pos=(640, 250))
        OPTIONS_BUTTON = Button(image=pygame.image.load("./assets/Boutons/boutonReglages.png") , pos=(640, 400))
        QUIT_BUTTON = Button(image=pygame.image.load("./assets/Boutons/boutonQuitter.png") , pos=(640, 550))

        for button in [PLAY_BUTTON,OPTIONS_BUTTON,QUIT_BUTTON]:
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                
        pygame.display.flip()
        pygame.display.update()

main_menu()
pygame.quit()

