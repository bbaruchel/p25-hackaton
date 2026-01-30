
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
        if x > self.x + self.width/2 : 
          if y > self.y + self.height/2 :
            ux = x - self.x - self.width
            uy = y - self.y - self.height
            if ux > uy :
              if uy < 0 :
                return (self.x+self.width,y)
              else :
                return (self.x+self.width,self.y+self.height)
            else :
              if ux < 0 :
                return (x,self.y+self.height)
              else :
                return (self.x+self.width,self.y+self.height)
          else    
            ux = x - self.x - self.width
            uy = y - self.y
            if ux > (-uy) :
              if ux < 0 :
                return (self.x+self.width,y)
              else :
                return (self.x+self.width,self.y)
            else :
              if (-uy) < 0 :
                return (x,self.y)
              else :
                return (self.x+self.width,self.y)
        else :
          if y > self.y + self.height/2 :
            ux = x - self.x - self.width
            uy = y - self.y - self.height
            if (-ux) > uy :
              if uy < 0 :
                return (self.x,y)
              else :
                return (self.x,self.y+self.height)
            else :
              if (-ux) < 0 :
                return (x,self.y+self.height)
              else :
                return (self.x,self.y+self.height)
          else    
            ux = x - self.x - self.width
            uy = y - self.y
            if (-ux) > (-uy) :
              if (-ux) < 0 :
                return (self.x,y)
              else :
                return (self.x+self.y)
            else :
              if (-uy) < 0 :
                return (x,self.y)
              else :
                return (self.x,self.y)


    def distplat(self, x,y) :
        if x > self.x + self.width/2 : 
          if y > self.y + self.height/2 :
            ux = x - self.x - self.width
            uy = y - self.y - self.height
            if ux > uy :
              if uy < 0 :
                return abs(ux)
              else :
                return (ux**2+uy**2)**0.5
            else :
              if ux < 0 :
                return abs(uy)
              else :
                return (ux**2+uy**2)**0.5
          else : 
            ux = x - self.x - self.width
            uy = y - self.y
            if ux > (-uy) :
              if ux < 0 :
                return abs(ux)
              else :
                return (ux**2+uy**2)**0.5
            else :
              if (-uy) < 0 :
                return abs(uy)
              else :
                return (ux**2+uy**2)**0.5
        else :
          if y > self.y + self.height/2 :
            ux = x - self.x - self.width
            uy = y - self.y - self.height
            if (-ux) > uy :
              if uy < 0 :
                return abs(ux)
              else :
                return (ux**2+uy**2)**0.5
            else :
              if (-ux) < 0 :
                return abs(uy)
              else :
                return (ux**2+uy**2)**0.5
          else :  
            ux = x - self.x - self.width
            uy = y - self.y
            if (-ux) > (-uy) :
              if (-ux) < 0 :
                return abs(ux)
              else :
                return (ux**2+uy**2)**0.5
            else :
              if (-uy) < 0 :
                return abs(uy)
              else :
                return (ux**2+uy**2)**0.5


