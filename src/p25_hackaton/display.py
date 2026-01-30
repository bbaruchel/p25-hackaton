import pygame 
from .platform import Platform
from .goo import Goo

class Display:
    def __init__(self, width : float, height :float, start : Platform, end : Platform, platforms : list[Platform], goos : list[Goo]) -> None:
        self.width = width
        self.height = height
        self.start = start
        self.end = end
        self.platforms = platforms
        self.goos = goos
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("World of Goos")
        self.clock = pygame.time.Clock()
        pygame.init()
        self._clear()

    def _clear(self) -> None:
        self.screen.fill((0, 0, 0)) 

    def _add_goo(self, goo : Goo) -> None:
        pygame.draw.circle(self.screen, (0, 0, 255), (goo.center_x, goo.center_y), goo.rayon)

    def _add_platform(self, platform : Platform) -> None:
        if platform.is_start:
            color = (0, 255, 0)
        elif platform.is_end:
            color = (255, 0, 0)
        else :
            color = (255, 255, 255)
        pygame.draw.rect(self.screen, color, (platform.x, platform.y, platform.width, platform.height))

    
    def update(self, goos : list[Goo]) -> None:
        self._clear()

        for p in self.platforms :
            self._add_platform(p)
        
        for g in goos :
            self._add_goo(g)
        pygame.display.flip()
        self.clock.tick(60)

    
        
    
