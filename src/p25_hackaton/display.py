import pygame 
from .platform import Platform
from .goo import Goo

class Display:
    def __init__(self, width : float, height :float, start : Platform, end : Platform) -> None:
        self.width = width
        self.height = height
        self.start = start
        self.end = end
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("World of Goos")
        self.clock = pygame.time.Clock()
        pygame.init()
        self._clear()

        #draw start and end platforms
        pygame.draw.rect(self.screen, (0, 255, 0), (start.x, start.y, start.width, start.height))
        pygame.draw.rect(self.screen, (255, 0, 0), (end.x, end.y, end.width, end.height))

    def _clear(self) -> None:
        self.screen.fill((0, 0, 0)) 

    def _add_goo(self, goo : Goo) -> None:
        pygame.draw.circle(self.screen, (0, 0, 255), (goo.center_x, goo.center_y), goo.rayon)

