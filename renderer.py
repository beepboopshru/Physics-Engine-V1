# renderer.py

import pygame
import sys
from body import Body

class PygameRenderer:
    def __init__(self, width, height, caption="Physics Simulation"):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()

    def clear_screen(self, color=(0, 0, 0)):
        self.screen.fill(color)

    def draw_body(self, body, color=(0, 255, 0), radius=10):
        # We need to convert the Vector position to a tuple of integers for Pygame.
        # We also have to handle the case where the position is off-screen.
        if 0 <= body.position.x <= self.width and 0 <= body.position.y <= self.height:
            pygame.draw.circle(self.screen, color, (int(body.position.x), int(body.position.y)), radius)

    def flip_display(self, fps=60):
        pygame.display.flip()
        self.clock.tick(fps)

    def check_for_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()