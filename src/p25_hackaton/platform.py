
class Platform: 
    def __init__(self, x : float, y : float, width : float, height : float, start : bool, end : bool, range : float = 0.01) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.range = range
        self.start = start
        self.end = end
    
    @property
    def is_start(self) -> bool:
        return self.start
    @property
    def is_end(self) -> bool:
        return self.end
    
    
    def distplat(self, x : float, y : float) -> float:
        bx = self.x + self.width/2
        by = self.y + self.height/2
        return ((bx - x)**2+(by- y)**2)**0.5
