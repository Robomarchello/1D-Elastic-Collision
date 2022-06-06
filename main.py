import pygame
from pygame.locals import *
from src.scripts.collision import get_elastic, Object, ObjectHandler

pygame.init()

class App():
    def __init__(self, ScreenSize, caption):
        self.ScreenSize = ScreenSize
        
        self.screen = pygame.display.set_mode(ScreenSize)
        pygame.display.set_caption(caption)
        
        self.clock = pygame.time.Clock()

        self.objects = []
        self.objects.append(Object(3, -5, [450, 100], ScreenSize))
        self.objects.append(Object(5, 5, [0, 100], ScreenSize))

        self.ObjectHandler = ObjectHandler(self.objects)

    def loop(self):
        screen = self.screen
        while True:
            screen.fill((255, 255, 255))

            self.ObjectHandler.update(screen)
            

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    raise SystemExit

            self.clock.tick(60)
            pygame.display.update()

if __name__ == '__main__':
    app = App((500, 100), 'elastic collision')
    
    app.loop()