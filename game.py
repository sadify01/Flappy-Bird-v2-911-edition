from settings import *
from window import Window
from background import Background
from bird import Bird
from land import Land
from pipe import Pipe

class Game:
    def __init__(self):
        self.window = Window()
        self.background = Background()
        self.land = Land()
        self.bird = Bird()
        self.pipe = Pipe()

        self.land_x = 0

        self.running = True
        self.game_over = False

    def reset_game(self):
        self.bird.rect = self.bird.birds[0].get_rect(center=(game_width / (7 / 2), game_height / 2))
        self.pipe = Pipe()
        self.game_over = False

    def update_game(self):
        bird_image = self.bird.update()

        pipe_top_rect, pipe_bottom_rect, pipe_top_mask, pipe_bottom_mask = self.pipe.get_collision_rects_and_masks()

        if self.bird.check_collision(pipe_top_rect, pipe_bottom_rect, self.land.rect, pipe_top_mask, pipe_bottom_mask, self.land.mask):
            self.game_over = True

        if self.game_over:
            if self.bird.land_collision:
                self.bird.movement = 0
                self.bird.frame = 1
            else:
                self.bird.rotate()
            if self.bird.frame != 1:
                self.bird.animate()
        else:
            self.bird.animate()
            self.bird.rotate()
            self.update_pipes_and_land()

        return bird_image

    def update_pipes_and_land(self):
        self.land_x -= 5 * dt
        if self.land_x <= -land_width:
            self.land_x = 0

        self.pipe.update()

    def run(self):
        while self.running:
            self.window.update()
            event_result = self.window.handle_events()

            if event_result is False:
                self.running = False
            elif event_result is True:
                self.bird.flap()
                if self.game_over:
                    self.reset_game()

            bird_image = self.update_game()
            self.window.draw(bird_image, self)
