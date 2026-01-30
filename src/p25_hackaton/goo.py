from platform import Platform

class Goo():
    def __init__(self, goos, platforms, position_x: float, position_y: float, speed: float = 1.0, rayon:float= 0.01, masse: float= 0.4):
        
        self.center_x = position_x
        self.center_y = position_y
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
                 self.voisins.append((g,d))
        for p in platforms :
             d = self.distplat(p)
             if d <= self.dminp :
                 self.voisins.append((p,d))
    def dist(self, g) :
        return ((g.x-self.center_x)**2+(g.y-self.center_y)**2)**0.5
    def distplat(self, platform) :
        return 0.1
    

    
