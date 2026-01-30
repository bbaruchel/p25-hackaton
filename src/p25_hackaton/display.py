import pygame 
from .platform import Platform
from .goo import Goo
from .physique import verlet_integration_bis, spring_update

## Coeff d'échelle pour l'affichage (en raisonne en mètre pour la modélisation physique)
PIXELS_PER_METER = 1000

class Display:
    def __init__(self, width : float, height :float, start : Platform, end : Platform, platforms : list[Platform], goos : list[Goo]) -> None:
        pygame.init()

        self.width = width*PIXELS_PER_METER
        self.height = height*PIXELS_PER_METER
        self.start = start
        self.end = end
        self.platforms = platforms
        self.goos = goos
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("World of Goos")
        self.clock = pygame.time.Clock()

        self._clear()

    def _clear(self) -> None:
        self.screen.fill((255, 255, 255)) 

    def _add_goo(self, goo : Goo) -> None:
        pygame.draw.circle(self.screen, (0, 0, 0), (goo.x*PIXELS_PER_METER, goo.y*PIXELS_PER_METER), goo.rayon * PIXELS_PER_METER)

    def _draw_spring(self) -> None:
        for g in self.goos : 
            for (voisin, ressort) in g.voisins :
                pygame.draw.line(self.screen, (0,0,0), (g.x*PIXELS_PER_METER, g.y*PIXELS_PER_METER), (voisin.x*PIXELS_PER_METER, voisin.y*PIXELS_PER_METER), 1)
            for (platform, ressort) in g.platforms :
                p = (ressort.x0, ressort.y0)
                pygame.draw.line(self.screen, (0,0,0), (g.x*PIXELS_PER_METER, g.y*PIXELS_PER_METER), (p[0]*PIXELS_PER_METER, p[1]*PIXELS_PER_METER), 1)

    def _add_platform(self, platform : Platform) -> None:
        if platform.start:
            color = (0, 255, 0)
        elif platform.end:
            color = (255, 0, 0)
        else :
            color = (0, 0, 0)
        pygame.draw.rect(self.screen, color, (platform.x*PIXELS_PER_METER, platform.y*PIXELS_PER_METER, platform.width * PIXELS_PER_METER, platform.height * PIXELS_PER_METER))

    
    def update(self) -> None:
        verlet_integration_bis(self.goos,0.016)
        spring_update(self.goos)

        self._clear()

        for p in self.platforms :
            self._add_platform(p)
        
        for g in self.goos :
            self._add_goo(g)
        
        self._draw_spring()

        pygame.display.flip()
        self.clock.tick(60)

    
    def close(self) -> None:
        pygame.quit()


    def new_goo(self) -> None:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        new_goo = Goo(len(self.goos), position_x=mouse_x/PIXELS_PER_METER, position_y=mouse_y/PIXELS_PER_METER,goos = self.goos, platforms=self.platforms)
        self.goos.append(new_goo)

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.new_goo()
        return True
    
    def win(goos) : 
      visite = [False]*len(goos)
      for g in goos :
        if not (visite[g.id]) :
          todo = [g]
          hasstart = False
          hasend = False
          while len(todo) != 0 :
            s = todo.pop()
            if not visite[s.id] :
              visite[s.id] = True
              for (p,r) in s.platforms :
                if p.start : hasstart = True
                if p.end : hasend = True
              for (v,r) in s.voisins :
                todo.append(v)
          if hasstart && hasend : return True
      return False

    



