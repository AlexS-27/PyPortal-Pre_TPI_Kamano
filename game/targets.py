"""
File : game/targets.py
Description : This file contains all the settings for the targets
Autor : Alex Kamano
Version : 1.0
Project : PyPortal
Date : 3 March 2026
"""
import pygame
import random
from .base_settings import *

class Target:
    def __init__(self):
        # define the difficulty (size vs points)
        rand = random.random()
        if rand > 0.6: # 60% grand
            self.radius, self.point, self.color = 30, 10, GREEN
        elif rand > 0.2: # 40% medium
            self.radius, self.point, self.color = 20, 25, ORANGE
        else: # 20% small
            self.radius, self.point, self.color = 10, 50, RED

        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = random.randint(self.radius, HEIGHT - self.radius)
        self.spawn_time = pygame.time.get_ticks()
        self.current_scale = 0

    def draw(self, surface):
        # animation to enter
        if self.current_scale < self.radius:
            self.current_scale += 2

        # Design multicolor
        pygame.draw.circle(surface, DARK, (self.x, self.y), self.current_scale + 2)
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.current_scale)
        pygame.draw.circle(surface, WHITE, (self.x, self.y), self.current_scale // 3)
