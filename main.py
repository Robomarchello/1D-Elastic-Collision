import pygame
from pygame.locals import *

pygame.init()

class App():
    def __init__(self, ScreenSize, caption):
        self.ScreenSize = ScreenSize
        
        self.screen = pygame.display.set_mode(ScreenSize)
        pygame.display.set_caption(caption)
        
        self.clock = pygame.time.Clock()

    def loop(self):
        while True:
            self.screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    raise SystemExit

            self.clock.tick(60)
            pygame.display.update()

if __name__ == '__main__':
    app = App((500, 100), 'elastic collision')
    
    app.loop()