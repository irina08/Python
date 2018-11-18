#!/usr/local/bin/python3
# NAME: Your Name
# FILE: shape.py
# DESC: A Shape class set x,y coordinates, 
#       moves objects, and reports location.

import math


class Shape:
    """Shape class: provides three methods:
    1.   __init__()  set initial x,y coordinates
    2.   move()      changes x,y coordinates
    3.   location()  returns x,y coordinates 
    The __str__() method is customized to show 
    an object's class and x,y coordinates."""

    # __init__() is the constructor. 
    # Instance methods always have a "self" parameter.
    def __init__(self, x, y):
        """Assign x,y coordinates to the object"""
        self.x = x
        self.y = y
        
    def move(self, deltaX, deltaY):
        """Moves Shape object by adding values 
        to the object's x and y coordinates."""
        self.x = self.x + deltaX
        self.y = self.y + deltaY


    # Custom __str__() method to report an objects properties
    # Every class inherits a __str__() method for the 
    # top-level Object class. We can modify it to produce more 
    # descriptive output for this class.
    def __str__(self):
        """Return class name, x, and y"""
        return "{}, x:{}, y:{}".format(type(self).__name__, self.x, self.y)


    def location(self):
        '''Returns a tuple containing the (x,y) coordinates of a Shape object'''
        return (self.x, self.y)
        
# Example Testing code to execute when module is run as a standalone script.
# This code will *not* run when the module is imported.
def _main():
    """Testing Shape class move(), location(), 
    and __str__() methods"""
    print("--- START ---")
    i2 = 0 
    c1 = Shape(0, 5)
    c2 = Shape(5, 5)
    for i in range(10):
        i2 += i 
        c1.move(i, i)
        c2.move(i, i2) 
        print('--')
        print('Shape 1: ',c1)
        print('Shape 2: ',c2)
    print("c1 location: ", c1.location())
    print("c2 location: ", c2.location())
    print("--- END ---")


# The Shape._main() function will be executed when this file is run as a standalone script.
if __name__ == '__main__':
    _main()