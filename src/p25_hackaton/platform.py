
class Platform: 
    def __init__(self, x : float, y : float, width : float, height : float, start : bool, end : bool, range : float = 0.01) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.range = range
        self.start = start
        self.end = end

    def in_reach(self, x, y):
        return self.x - self.range <= x <= self.x + self.width + self.range and self.y - self.range - self.height <= y <= self.y  + self.range 
    