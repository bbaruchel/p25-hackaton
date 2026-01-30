class Spring():
    def __init__(self,l_0 :float, l : float, k : float = 100):
        self.k = k
        self.l_0 = l_0
        self.l = l

    def force(self) -> float:
        return self.k * (self.l - self.l_0)