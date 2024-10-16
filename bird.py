import pygame
import os
from settings import *

class Bird:
    def __init__(self):
        self.birds = []
        for num in range(1, 5):
            bird = pygame.image.load(os.path.join('assets', f'bird.png')).convert_alpha()
            bird = pygame.transform.scale(bird, (bird_width, bird_height))
            self.birds.append(bird)

        self.frame = frame
        self.rotation = bird_rotation
        self.movement = bird_movement
        self.rect = self.birds[0].get_rect(center=(game_width / (7 / 2), game_height / 2))
        self.frame_counter = frame_counter
        self.frame_counter2 = frame_counter2
        self.mask = pygame.mask.from_surface(self.birds[0])

    def animate(self):
        self.frame_counter2 += 1 * dt
        if self.frame_counter2 >= 5:
            self.frame_counter2 = 0
            self.frame += 1
            if self.frame == 4:
                self.frame = 0

    def rotate(self):
        if self.frame_counter == 90:
            if self.rotation > -90:
                self.rotation -= 6 * dt
            if self.rotation < -90:
                self.rotation = -90

    def check_collision(self, pipe_top_rect, pipe_bottom_rect, land_rect, pipe_top_mask, pipe_bottom_mask, land_mask):
        pipe_top_offset = (pipe_top_rect.x - self.rect.x, pipe_top_rect.y - self.rect.y)
        pipe_bottom_offset = (pipe_bottom_rect.x - self.rect.x, pipe_bottom_rect.y - self.rect.y)
        land_offset = (land_rect.x - self.rect.x, land_rect.y - self.rect.y)

        self.pipe_top_collision = self.mask.overlap(pipe_top_mask, pipe_top_offset)
        self.pipe_bottom_collision = self.mask.overlap(pipe_bottom_mask, pipe_bottom_offset)
        self.land_collision = self.mask.overlap(land_mask, land_offset)

        if self.pipe_top_collision or self.pipe_bottom_collision or self.land_collision:
            return True
        return False

    def update(self):
        self.movement += gravity
        self.rect.centery += self.movement

        if self.movement > 12:
            self.movement = 12

        if self.frame_counter < 90:
            self.frame_counter += 1

        bird_image = pygame.transform.rotate(self.birds[self.frame], self.rotation)
        self.rect = bird_image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(bird_image)

        return bird_image

    def flap(self):
        self.movement = 0
        self.movement -= 5.5
        self.rotation = 20
        self.frame_counter = 0
