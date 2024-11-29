import pytest

from points import Point
from Rectangles import Rectangle
# Test dla metody klasowej from_points
def test_from_points():
    pt1 = Point(0, 0)
    pt2 = Point(4, 5)
    rect = Rectangle.from_points([pt1, pt2])

    assert rect.pt1.x == 0
    assert rect.pt1.y == 0
    assert rect.pt2.x == 4
    assert rect.pt2.y == 5

# Test dla właściwości @property: top
def test_top():
    rect = Rectangle(0, 0, 4, 5)
    assert rect.top == 5

# Test dla właściwości @property: bottom
def test_bottom():
    rect = Rectangle(0, 0, 4, 5)
    assert rect.bottom == 0

# Test dla właściwości @property: left
def test_left():
    rect = Rectangle(0, 0, 4, 5)
    assert rect.left == 0

# Test dla właściwości @property: right
def test_right():
    rect = Rectangle(0, 0, 4, 5)
    assert rect.right == 4

# Test dla właściwości @property: width
def test_width():
    rect = Rectangle(0, 0, 4, 5)
    assert rect.width == 4

# Test dla właściwości @property: height
def test_height():
    rect = Rectangle(0, 0, 4, 5)
    assert rect.height == 5

# Test dla właściwości @property: bottomleft
def test_bottomleft():
    rect = Rectangle(0, 0, 4, 5)
    assert rect.bottomleft == rect.pt1

# Test dla właściwości @property: topleft
def test_topleft():
    rect = Rectangle(0, 0, 4, 5)
    assert rect.topleft == Point(0, 5)

# Test dla właściwości @property: bottomright
def test_bottomright():
    rect = Rectangle(0, 0, 4, 5)
    assert rect.bottomright == Point(4, 0)

# Test dla właściwości @property: topright
def test_topright():
    rect = Rectangle(0, 0, 4, 5)
    assert rect.topright == rect.pt2
