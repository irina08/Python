#!/usr/local/bin/python3
# Creator: Irina Golovko
# Name: helpers.py
# Description: Classes, namespaces, main function
# July 7, 2018

# For pi
import math 
 
# Use _main() for testing the module
def _main():

    print("#" * 28,"\n", "Testing...1, 2, 3...testing!\n", "#" * 28, "\n", sep="")

    # code to test area() and circ()
    radius = 10
    print("A circle with a radius of {} has a circumference of {:.2f} \
units and an area of {:.2f} square units.".format(radius, circ(radius), area(radius)))
    print()
    
    # code to test the f2c() function. 
    # Will print None if given temp < -459.67 F
    f_temp1 = 174.21
    f_temp2 = -459.67
    f_temp3 = -500.00
    print("{} degree Fahrenheit is equal to {:.2f} \
degree Celsius.".format(f_temp1, f2c(f_temp1)))
    print("{} degree Fahrenheit is equal to {:.2f} \
degree Celsius.".format(f_temp2, f2c(f_temp2)))
    print("{} degree Fahrenheit is equal to {} \
degree Celsius.".format(f_temp3, f2c(f_temp3)))
    print()
    
    # code to test the c2f() function. 
    # Will print None if given temp < -273.15 C 
    c_temp1 = 37.50
    print("{} degree Celsius is equal to {:.2f} \
degree Fahrenheit.".format(c_temp1, c2f(c_temp1)))
    c_temp2 = -273.15
    print("{} degree Celsius is equal to {:.2f} \
degree Fahrenheit.".format(c_temp2, c2f(c_temp2)))
    c_temp3 = -275.0
    print("{} degree Celsius is equal to {} \
degree Fahrenheit.".format(c_temp3, c2f(c_temp3)))
    print()

# Calculate the area of a circle of a given radius
def area(radius):
    return(radius * radius * math.pi)

# Calculate the circumference of a circle of a given radius
def circ(radius):
    return(radius * 2 * math.pi)


""" Triple quotes can be used to create multi-line comments

For temperature functions it's important to allow only valid temperatures. 
Your functions have to check that the user gives the function valid 
temperatures.

The lowest possible temperature, by international agreement,
is absolute zero (zero on the Kelvin scale). At 0 K (–273.15 °C; –459.67 °F), 
nearly all molecular motion ceases. Your script should
check that the input temperatures is not less than –273.15°C or –459.67°F.

The maximum possible temperature is 1.416785(71)×10**32 kelvins
(142 quintillion kelvins) --- there is no existing scientific theory
for the behavior of matter at these energies.
[https://en.wikipedia.org/wiki/Absolute_hot]
"""

def f2c(temp):
    """
    Converts Fahrenheit tempature to Celcius
    USAGE: print(f2c(f_temp)
    """
    if temp >= -459.67:
        return (temp - 32) * 5.0/9.0
# else: return None (it will return by default)


def c2f(temp):
    """ 
    Converts Celcius to Fahrenheit
    USAGE: print(c2f(c_temp)
    """
    if temp >= -273.15:
        return (temp * 1.8) + 32
# else: return None (it will return by default)
        
# testing code
# When run on the command line, this code will run
# but when the module is imported, it wont' run.
if __name__ == '__main__':
    _main()