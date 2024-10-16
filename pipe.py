import pygame
import os
import random
from settings import game_width, pipe_width, pipe_height, space_size, dt

class Pipe:
    def __init__(self):
        self.pipe_top = pygame.image.load(os.path.join('assets', 'tower.png')).convert_alpha()
        self.pipe_top = pygame.transform.scale(self.pipe_top, (pipe_width, pipe_height))
        self.pipe_top_x_pos = game_width
        self.pipe_top_y_pos = random.randint(-600, -200)
        self.pipe_top_rect = self.pipe_top.get_rect(topleft=(self.pipe_top_x_pos, self.pipe_top_y_pos))
        self.pipe_top_mask = pygame.mask.from_surface(self.pipe_top)

        self.pipe_bottom = pygame.image.load(os.path.join('assets', 'tower.png')).convert_alpha()
        self.pipe_bottom = pygame.transform.scale(self.pipe_bottom, (pipe_width, pipe_height))
        self.pipe_bottom = pygame.transform.flip(self.pipe_bottom, 100, 100)
        self.pipe_bottom_x_pos = self.pipe_top_x_pos
        self.pipe_bottom_y_pos = self.pipe_top_rect.bottom + space_size
        self.pipe_bottom_rect = self.pipe_bottom.get_rect(topleft=(self.pipe_bottom_x_pos, self.pipe_bottom_y_pos))
        self.pipe_bottom_mask = pygame.mask.from_surface(self.pipe_bottom)

    def update(self):
        self.pipe_top_x_pos -= 5 * dt
        self.pipe_top_rect = self.pipe_top.get_rect(topleft=(self.pipe_top_x_pos, self.pipe_top_y_pos))
        self.pipe_bottom_x_pos = self.pipe_top_x_pos
        self.pipe_bottom_y_pos = self.pipe_top_rect.bottom + space_size
        self.pipe_bottom_rect = self.pipe_bottom.get_rect(topleft=(self.pipe_bottom_x_pos, self.pipe_bottom_y_pos))

        if self.pipe_top_x_pos <= -pipe_width:
            self.pipe_top_x_pos = game_width
            self.pipe_top_y_pos = random.randint(-600, -200)
            self.pipe_top_rect = self.pipe_top.get_rect(topleft=(self.pipe_top_x_pos, self.pipe_top_y_pos))
            self.pipe_bottom_x_pos = self.pipe_top_x_pos
            self.pipe_bottom_y_pos = self.pipe_top_rect.bottom + space_size
            self.pipe_bottom_rect = self.pipe_bottom.get_rect(topleft=(self.pipe_bottom_x_pos, self.pipe_bottom_y_pos))

    def draw(self, surface):
        surface.blit(self.pipe_top, self.pipe_top_rect)
        surface.blit(self.pipe_bottom, self.pipe_bottom_rect)

    def get_collision_rects_and_masks(self):
        return (self.pipe_top_rect, self.pipe_bottom_rect, self.pipe_top_mask, self.pipe_bottom_mask)
