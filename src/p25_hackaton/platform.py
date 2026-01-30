
class Platform: 
    def __init__(self, x : float, y : float, width : float, height : float, start : bool, end : bool, range : float = 0.01) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.range = range
    def distplat(platform) :
        bx = platform.x + platform.width/2
        by = platform.y + platform.height/2
        return sqrt((bx-x)**2+(by-self.y)**2)
