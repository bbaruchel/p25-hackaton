
class Platform: 
    def __init__(self, x, y, width, height, range = 10):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.range = range

    def in_reach(self, x, y):
        return self.x - self.range <= x <= self.x + self.width + self.range and self.y - self.range - self.height <= y <= self.y  + self.range 
    