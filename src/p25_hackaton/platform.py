
class Platform: 
    def __init__(self, x : float, y : float, width : float, height : float, start : bool, end : bool, range : float = 0.01) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.range = range
        self.start = start
        self.end = end
    
    def proj(self, x,y) :
        px = min(max(x, self.x), self.x + self.width)
        py = min(max(y, self.y), self.y + self.height)
        return px, py


    def distplat(self, x,y) :
        px,py = self.proj(x,y)
        return ((px - x)**2 + (py - y)**2)**0.5


    def contact(self, x, y):
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height