from collections import namedtuple
from typing import NamedTuple

Point = namedtuple('Point', ['x', 'y', 'z'])

class Point2(NamedTuple):
    x: int
    y: int
    z: int


p = Point(1,0,0)
p2 = Point(2,1,1)

if __name__ == '__main__':
    print(p)
    print(p._fields)
    print(p2)
    print(p._fields)
