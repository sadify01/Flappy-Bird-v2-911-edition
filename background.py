import pygame
import os
from settings import background_width, background_height

class Background:
    def __init__(self):
        self.image = pygame.image.load(os.path.join('assets', 'sky_day.png')).convert()
        self.image = pygame.transform.scale(self.image, (background_width, background_height))

    def draw(self, surface):
        surface.blit(self.image, (0, 0))