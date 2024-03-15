from Triangle import Triangle
class TriangularPyramid(Triangle):
    def __init__(self, a, b, c, h):
        assert h>0
        super().__init__(a, b, c)
        self.h = h
    def dimention(self):
        return 3
    def volume(self):
        return (1/3)*super().square()*self.h
    def squareBase(self):
        return super().square()
    def squareSurface(self):
        half_diagonal = ((self.a**2 + self.b**2)**0.5)/2
        bone = (half_diagonal**2 + self.h**2)**0.5
        halfperimeter1 = bone * 2 + self.a
        halfperimeter2 = bone * 2 + self.b
        triangle1 = (halfperimeter1 * (halfperimeter1 - self.a) * (halfperimeter1 - bone) * (halfperimeter1 - bone)) ** 0.5
        triangle2 = (halfperimeter2 * (halfperimeter2 - self.b) * (halfperimeter2 - bone) * (halfperimeter2 - bone)) ** 0.5
        return triangle1 * 2 + triangle2 * 2 + super().square()
    def height(self):
        return self.h
    def __str__(self) -> str:
        return f"triangularpyramid: a={self.a} h={self.h}"