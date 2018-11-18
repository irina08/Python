#!/usr/local/bin/python3
# Creator: Irina Golovko
# Name: module_demo.py
# Description: This script uses functions c2f(),
# f2c(), circ(), area() from helpers.py module
# July 7, 2018

import helpers

print("Testing functions from imported module 'helpers':")
# code to test area() from helpers.py
radius = 20
print("Testing area() function:")
print("Area of a circle with radius of {} is {:.2f} \
square units.".format(radius, helpers.area(radius)))
print()

# code to test circ() from helpers.py
print("Testing circ() function:")
print("A circle with a radius of {} has a circumference of {:.2f} \
units".format(radius, helpers.circ(radius)))
print()

# code to test the f2c() function 
f1 = 100.00
f2 = -459.67
f3 = -520.00
print("Testing f2c() function:")
print("{} degree Fahrenheit is equal to {:.2f} \
degree Celsius.".format(f1, helpers.f2c(f1)))
print("{} degree Fahrenheit is equal to {:.2f} \
degree Celsius.".format(f2, helpers.f2c(f2)))
print("{} degree Fahrenheit is equal to {} \
degree Celsius.".format(f3, helpers.f2c(f3)))
print()
    
# code to test the c2f() function 
c1 = 10.50
c2 = -273.15
c3 = -280.0
print("Testing c2f() function:")
print("{} degree Celsius is equal to {:.2f} \
degree Fahrenheit.".format(c1, helpers.c2f(c1)))
print("{} degree Celsius is equal to {:.2f} \
degree Fahrenheit.".format(c2, helpers.c2f(c2)))
print("{} degree Celsius is equal to {} \
degree Fahrenheit.".format(c3, helpers.c2f(c3)))
print()

