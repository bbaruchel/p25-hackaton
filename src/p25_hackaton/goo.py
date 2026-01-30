from .platform import Platform
from .spring import Spring

class Goo():
    def __init__(self, position_x: float, position_y: float,goos : list["Goo"], platforms : list[Platform], rayon:float= 0.01, masse: float= 0.4):
        
        self.x = position_x
        self.y = position_y
        self.vx = 0
        self.vy = 0
        self.rayon = rayon
        self.masse = masse
        self.dming = 0.2
        self.dminp = 0.1
        self.voisins = []
        self.platforms = []
        for g in goos :
             d = self.dist(g)
             if d <= self.dming :
                 r = Spring(d,d)
                 self.voisins.append((g,r))
        for p in platforms :
             d = p.distplat(self.x,self.y)
             if d <= self.dminp :
                 r = Spring(d,d)
                 self.platforms.append((p,r))
    def dist(self, g) :
        return ((g.x-self.x)**2+(g.y-self.y)**2)**0.5
