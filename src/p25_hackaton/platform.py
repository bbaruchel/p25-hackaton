
class Platform: 
    def __init__(self, x, y, width, height, range = 10):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.range = range
    def distplat(platform) :
        bx = platform.x + platform.width/2
        by = platform.y + platform.height/2
        return sqrt((bx-x)**2+(by-self.y)**2)
    
