import pygame
import sys
from settings import game_width, game_height, refresh_rate

class Window:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((game_width, game_height))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()

    def draw(self, bird_image, game):
        self.screen.blit(game.background.image, (0, 0))
        game.pipe.draw(self.screen)
        self.screen.blit(bird_image, game.bird.rect)

        game.land.draw(self.screen, game.land_x)

        pygame.display.update()

    def update(self):
        self.clock.tick(refresh_rate)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and pygame.BUTTON_LEFT:
                return True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_SPACE:
                    return True

        return None
