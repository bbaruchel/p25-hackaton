
class Platform: 
    def __init__(self, x : float, y : float, width : float, height : float, start : bool, end : bool, range : float = 0.01) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.range = range
        self.start = start
        self.end = end
    
    def distplat(self, x,y) :
        if x > self.x + self.width/2 : 
          if y > self.y + self.height/2 :
            ux = x - self.x - self.width
            uy = y - self.y - self.height
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
            ux = x - self.x - self.width
            uy = y - self.y
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
          if y > self.y + self.height/2 :
            ux = x - self.x - self.width
            uy = y - self.y - self.height
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
            ux = x - self.x - self.width
            uy = y - self.y
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


