from .platform import Platform
from .spring import Spring

class Goo():
    def __init__(self, position_x: float, position_y: float,goos : list["Goo"], platforms : list[Platform], speed: float = 1.0, rayon:float= 0.01, masse: float= 0.4):
        
        self.x = position_x
        self.y = position_y
        self.speed = speed
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
             d = self.distplat(p)
             if d <= self.dminp :
                 r = Spring(d,d)
                 self.platforms.append((p,r))
    def dist(self, g) :
        return ((g.x-self.x)**2+(g.y-self.y)**2)**0.5
    def distplat(self, platform) :
        if self.x > platform.x + platform.width/2 : 
          if self.y > platform.y + platform.height/2 :
            ux = x - platform.x - platform.width
            uy = y - platform.y - platform.height
            if ux > uy :
              if uy < 0 :
                return abs(ux)
              else :
                return sqrt(ux**2+uy**2)
            else :
              if ux < 0 :
                return abs(uy)
              else :
                return sqrt(ux**2+uy**2)
          else    
            ux = x - platform.x - platform.width
            uy = y - platform.y
            if ux > (-uy) :
              if ux < 0 :
                return abs(ux)
              else :
                return sqrt(ux**2+uy**2)
            else :
              if (-uy) < 0 :
                return abs(uy)
              else :
                return sqrt(ux**2+uy**2)
        else :
          if self.y > platform.y + platform.height/2 :
            ux = x - platform.x - platform.width
            uy = y - platform.y - platform.height
            if (-ux) > uy :
              if uy < 0 :
                return abs(ux)
              else :
                return sqrt(ux**2+uy**2)
            else :
              if (-ux) < 0 :
                return abs(uy)
              else :
                return sqrt(ux**2+uy**2)
          else    
            ux = x - platform.x - platform.width
            uy = y - platform.y
            if (-ux) > (-uy) :
              if (-ux) < 0 :
                return abs(ux)
              else :
                return sqrt(ux**2+uy**2)
            else :
              if (-uy) < 0 :
                return abs(uy)
              else :
                return sqrt(ux**2+uy**2)


