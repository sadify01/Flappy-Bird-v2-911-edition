import pygame
import os
from settings import land_width, land_height, land_x, land_y

class Land:
    def __init__(self):
        self.x = land_x
        self.y = land_y
        self.image = pygame.image.load(os.path.join('assets', 'land.png')).convert()
        self.image = pygame.transform.scale(self.image, (land_width, land_height))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, surface, land_x):
        for i in range(2):
            surface.blit(self.image, (land_x + land_width * i, land_y))
