class Spring():
    def __init__(self,l_0 :float, l : float, x0 :float = -1., y0 :float = -1., k : float = 100.) -> None:
        self.k = k
        self.l_0 = l_0
        self.distance = l
        self.x0 = x0
        self.y0 = y0

    def force(self) -> float:
        return -self.k * (self.distance - self.l_0)

