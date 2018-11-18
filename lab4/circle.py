#!/usr/local/bin/python3
# NAME: Your Name
# FILE: circle.py
# DESC: A Shape class set x,y coordinates, 
#       moves objects, and reports location.

import math
from shape import Shape

class Circle(Shape):
    pi = 3.14159265359
    def __init__(self, x=0, y=0, radius=1):
        Shape.__init__(self, x, y)
        self.radius = radius

    def area(self):
        return  math.pi * self.radius ** 2

    def __str__(self):
        return Shape.__str__(self) + ", radius: {radius}, \
area: {area:.2f}".format(radius=self.radius, area = self.area())


    @classmethod
    def is_collision(Circle,c1, c2):
        """Test whether two circle objects are occupying the same space."""
        if c1.radius + c2.radius >= Circle.distance(c1, c2):
            return True

        
    @classmethod
    def distance(Circle,c1,c2):
        return math.sqrt(((c1.x-c2.x)**2)+((c1.y-c2.y)**2))
        
        
def _main():
    """Testing Circle class for area(), move(), location(), 
    __str__(), is_collision"""
    print("--- START ---")
    c1x = -10
    c1y = 0
    c2x = 10
    c2y = 0
    i1 = 0
    i2 = 0
    c1 = Circle(0, 0, 5)
    c2 = Circle(0, 0, 5)
    for i in range(10):
        print('--')
        print('Circle  1: ',c1)
        print('Circle  2: ',c2)
        print("Collision: ",Circle.is_collision(c1, c2))
        i1 += i
        i2 -= i
        c1.move(i, i1)
        c2.move(i, i2)
    print("c1 Final location: ", c1.location())
    print("c2 Final location: ", c2.location())
    print(c1)
    print(c2)
    print("--- END ---")   


# The Circle._main() function will be executed when this file is run as a standalone script.
if __name__ == '__main__':
    _main()