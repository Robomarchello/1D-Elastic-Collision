#elastic collision is a collision where kinetic energy is fully conserved
#m1 v1 = m2 v2
#v1 + v2 = v1f + v2f
#https://www.youtube.com/watch?v=CFbo_nBdBco&t=365s
#https://en.wikipedia.org/wiki/Elastic_collision#One-dimensional_Newtonian
import pygame

pygame.init()

def get_elastic(vel1, mass1, vel2, mass2):
    ratio1 = (mass1 - mass2) / (mass1 + mass2)
    ratio2 = (2 * mass1) / (mass1 + mass2)
    ratio3 = (2 * mass2) / (mass1 + mass2)

    vel1f = ratio1 * vel1 + ratio3 * vel2
    vel2f = ratio2 * vel1 + ratio1 * vel2
    
    return [vel1f, vel2f]

font = pygame.font.Font('src/font.ttf', 15)

class Object():
    def __init__(self, mass, velocity:pygame.Vector2, position, ScreenSize):
        self.mass = mass
        self.velocity = velocity

        self.rect = pygame.Rect(0, 0, 40 + mass * 4, 40 + mass * 4)
        self.rect.bottomleft = position
        self.position = pygame.Vector2(self.rect.topleft)

        self.massText = font.render(f'm={self.mass}', False, (0, 0, 0))
        self.massTextPos = self.massText.get_rect(center = self.rect.center)
        
        self.ScreenSize = ScreenSize
        
    def collision_resolve(self, other:'Object'):
        #collision is pretty bad:(
        if self.rect.colliderect(other.rect):
            afterVelocities = get_elastic(self.velocity, self.mass, other.velocity, other.mass)
            self.velocity = afterVelocities[0]
            other.velocity = afterVelocities[1]
            
            while self.rect.colliderect(other.rect):
                self.update()
                other.update()

    def update(self):
        self.position[0] += self.velocity
        self.rect.topleft = self.position
        self.massTextPos.center = self.rect.center

        if self.rect.left < 0 and self.velocity < 0:
            self.velocity = -self.velocity

        if self.rect.right > self.ScreenSize[0] and self.velocity > 0:
            self.velocity = -self.velocity

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

        screen.blit(self.massText, self.massTextPos)

class ObjectHandler():
    def __init__(self, objects):
        self.objects = objects

        obj = self.objects.copy()

    def update(self, screen:pygame.Surface):
        #function resolves the collision and draws objects
        for object in self.objects:
            object.update()
            object.draw(screen)
                
            for other in self.objects:
                if object is not other:
                    object.collision_resolve(other)