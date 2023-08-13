from collections import namedtuple
from typing import NamedTuple

Point = namedtuple('Point', ['x', 'y', 'z'])

class Point2(NamedTuple):
    x: int
    y: int
    z: int


p = Point(1, 0, 0)
p2 = Point(2, 1, 1)

class Employee(NamedTuple):
    id: int
    name: str
    role: str

    def __repr__(self):
        return f'{type(self).__name__}(id={self.id}, name={self.name}, role{self.role})'

# Simulating database query result
query_result = [(1, 'Alice', 'Manager'), (2, 'Bob', 'Developer')]
employees = [Employee(*row) for row in query_result]

if __name__ == '__main__':
    print(p)
    print(p._fields)
    print(p2)
    print(p._fields)
    print(f"Coordinates of the point are x={p2.x} y={p2.y} and z={p2.z}")
    print(Employee)
    print(employees)
