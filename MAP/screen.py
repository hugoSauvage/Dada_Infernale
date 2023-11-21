import pygame

class Screen:
    def __init__(self) -> None:
        self.display = pygame.display.set_mode((1280,720))#pygame.FULLSCREEN
        pygame.display.set_caption("Ludo:GoatEdition")
        self.Clock = pygame.time.Clock()
        self.framerate = 60

    def update(self):
        pygame.display.flip() 
        pygame.display.update()
        self.Clock.tick(self.framerate)
        self.display.fill((0, 0, 0))

    def get_size(self):
        return self.display.get_size()
    
    def get_display(self):
        return self.display
