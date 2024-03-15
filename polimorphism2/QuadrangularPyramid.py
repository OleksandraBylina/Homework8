from Figure import Figure
class QuadrangularPyramid(Figure):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h
    def dimension(self):
        return 3
    def squareBase(self):
        return super().square()
    def squareSurface(self):
        result_re = super().square()
        l1 = ((self.a / 2) ** 2 + self.h ** 2) ** 0.5
        l2 = ((self.b / 2) ** 2 + self.h ** 2) ** 0.5
        result_tr_1 = l1 * self.b / 2
        result_tr_2 = l2 * self.a / 2
        return (result_re + 2 * result_tr_2 + 2 * result_tr_1)
    def volume(self):
        return super().square()*(1/3)*self.h
    def height(self):
        return self.h
    def __str__(self) -> str:
        return f"QuadrangularPyramid: a={self.a} b={self.b} h={self.h}"