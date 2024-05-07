class Painting():
    def __init__(self, medium):
        self.medium = medium

    def paint(self, brush):
        self.mode = "painting"
        self.brush = brush

    def whereisit(self, where):
        self.where = where

class Acrylic(Painting):
    def __init__(self, painttype):
        super().__init__("Painting")
        self.solvent = "water"
        self.sides = 4
        self.color = 4
        self.painttype = painttype

    def paint(self, brush):
        super().paint(brush)
        print("Painting with", self.painttype, "with a", self.brush, "brush.")


class Collage(Painting):
    def __init__(self, painttype, framed):
        super().__init__("Collage")
        if (framed):
            self.framed = 4
        else:
            self.framed = 0
        self.solvent = "thinner"
        self.painttype = painttype

    def paint(self, brush):
        super().paint(brush)
        print("Painting with", self.painttype, "with a", self.brush, "brush.")

    def whereisit(self, where):
        super().whereisit(where)
        print("It is located in", self.where)

acrylic1 = Acrylic("plastic")
acrylic2 = Acrylic("latex")
collage1 = Collage("spray paint", True)

print(collage1.solvent)
print(acrylic1.painttype)
print(acrylic2.solvent)

acrylic1.paint("flat")
acrylic2.paint("new")
collage1.paint("crappy")
collage1.whereisit("Paducah")
