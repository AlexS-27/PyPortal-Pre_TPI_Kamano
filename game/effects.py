import pygame
import random

class Particle:
    def __init__(self, x, y, color):
        self.x, self.y = x, y
        self.color = color
        self.vx, self.vy = random.uniform(-4, 4), random.uniform(-4, 4)
        self.lifetime = 255

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.lifetime -= 10

    def draw(self, surface):
        if self.lifetime > 0:
            s = pygame.Surface((4, 4))
            s.set_alpha(self.lifetime)
            s.fill(self.color)
            surface.blit(s, (self.x, self.y))
