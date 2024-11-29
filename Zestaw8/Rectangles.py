
from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # Chcemy, aby x1 < x2, y1 < y2.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        if not (x1<x2) and (y1<y2):
          raise ValueError("Wrong values")

    def __str__(self):          # "[(x1, y1), (x2, y2)]"
        string1 = "[(" + str(self.pt1.x) + ", " + str(self.pt1.y) + "), (" + str(self.pt2.x) + ", " + str(self.pt2.y) + ")]"
        return string1

    def __repr__(self):         # "Rectangle(x1, y1, x2, y2)"
        string1 = "Rectangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(self.pt2.y) + ")"
        return string1

    def __eq__(self, other):    # obsługa rect1 == rect2
        if isinstance(other, Rectangle):
          return (self.pt1 == other.pt1 and self.pt2 == other.pt2)
        return False


    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):           # zwraca środek prostokąta
        pt = Point(0,0)
        pt.x = (self.pt1.x + self.pt2.x) // 2
        pt.y = (self.pt1.y + self.pt2.y) // 2
        return pt

    def area(self):             # pole powierzchni
        X = self.pt2.x - self.pt1.x
        Y = self.pt2.y - self.pt1.y
        P = X * Y
        return P

    def move(self, x, y):       # przesunięcie o (x, y)
        R = Rectangle(0,0,0,0)
        R.pt1.x, R.pt1.y = self.pt1.x + x, self.pt1.y + y
        R.pt2.x, R.pt2.y = self.pt2.x + x, self.pt2.y + y
        return R
    def intersection(self, other):  # część wspólna prostokątów

      #assigning x for pt1
      if (self.pt1.x <= other.pt1.x) and (other.pt1.x in range(self.pt1.x, self.pt2.x)) :
        x1 = other.pt1.x
      elif (self.pt1.x > other.pt1.x) and (self.pt1.x in range(other.pt1.x, other.pt2.x)) :
        x1 = self.pt1.x
      else:
        raise ValueError("Brak częsci wspólnej")

      #assigning x for pt2
      if (self.pt2.x <= other.pt2.x):
        x2 = self.pt2.x
      elif (self.pt1.x > other.pt1.x) :
        x2 = other.pt2.x

      #assinging y for pt1
      if (self.pt1.y <= other.pt1.y) and (other.pt1.y in range(self.pt1.y, self.pt2.y)) :
        y1 = other.pt1.y
      elif (self.pt1.y > other.pt1.y) and (self.pt1.y in range(other.pt1.y, other.pt2.y)) :
        y1 = self.pt1.y
      else: raise ValueError("Brak częsci wspólnej")

        #assigning y for pt2
      if (self.pt2.y <= other.pt2.y) :
        y2 = self.pt2.y
      elif (self.pt1.y > other.pt1.y) :
        y2 = other.pt2.y
      return Rectangle(x1, y1, x2, y2)

    def cover(self, other):    # prostąkąt nakrywający oba
      x1 = min(self.pt1.x, other.pt1.x)
      y1 = min(self.pt1.y, other.pt1.y)
      x2 = max(self.pt2.x, other.pt2.x)
      y2 = max(self.pt2.y, other.pt2.y)
      return Rectangle(x1, y1, x2, y2)

    def make4(self):            # zwraca krotkę czterech mniejszych
      centr = self.center()
      R1 = Rectangle(self.pt1.x, centr.y, centr.x, self.pt2.y) #pierwszy prostokat
      R2 = Rectangle(centr.x, centr.y, self.pt2.x, self.pt2.y) #drugi prostokat
      R3 = Rectangle(self.pt1.x, self.pt1.y, centr.x, centr.y) #trzeci prostokąt
      R4 = Rectangle(centr.x, self.pt1.y, self.pt2.x,centr.y) #czwarty prostokąt

      return (R1,R2,R3,R4)

    @classmethod
    def from_points(cls, sequence):
      return cls(sequence[0].x, sequence[0].y, sequence[1].x, sequence[1].y)

    @property
    def top(self):
      return self.pt2.y
    @property
    def bottom(self):
      return self.pt1.y
    @property
    def left(self):
      return self.pt1.x
    @property
    def right(self):
      return self.pt2.x
    @property
    def width(self):
      return self.pt2.x - self.pt1.x
    @property
    def height(self):
      return self.pt2.y - self.pt1.y
    @property
    def bottomleft(self):
      return self.pt1
    @property
    def topleft(self):
      return Point(self.pt1.x,self.pt2.y)
    @property
    def bottomright(self):
      return Point(self.pt2.x,self.pt1.y)
    @property
    def topright(self):
      return self.pt2




