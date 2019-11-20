#!/usr/local/bin/python3

#!/usr/local/bin/python3
# NAME: student Irina Golovko
# FILE: sine_wave.py
# DATE: 02/02/2019
# DESC: Write a program that displays the curvature 
# of a sinusoid on the terminal in a single statement

import math 
from itertools import accumulate, repeat, takewhile

# Here is the easiest way to get sine wave using while loop:
#a=0
#while a < 15:
#    print(" "*int(30+30*math.sin(a)) + "*")
#    a+=.1

# If we would like to do it infinity we can use "while true".
# I chose to find sine of angels in the range (0,15) with 
# increment = 0.1, because than bigger increment than more sharp
# and ugly become our sinusoid.
# I chose indent step = 30 for more beautiful outputs on the terminal.
# The more value of indent step than outputs look more beatiful.  
# We need to convert decimal value of sin(a) to integer int(30+30*math.sin(a))
# because we can't multiply sequence by non-int of type 'float'

# *map(lambda a: " "*int(30+30*math.sin(a)) + "*")

# Unfortunately I found only one way to replace while loop
# is using itertools module. I created a list of values for
# finding sine of this values ([0, 0.1, 0.2, ....., 14.1, 14.2, ...., 14.9])
# using takewhile function with lambda and accumulate funtion 
# with lambda in the range between 0 (repeat(0) and 15 (x < 15) 
# and  increment = 0.1 (_: x + .1)

# list(takewhile(lambda i: i < 15, accumulate(repeat(0), lambda i, _: i + .1)))

# We can use math.sin(a) function for finding sine of 'a' 
# with import math module or 
# (e**(a*1j)).imag where e = 2.718281828459045 
# (2.718281828459045**(a*1j)).imag without importing module 'math'
# I prefer to use function math.sin(a) because it gives us 
# better looking outputs. 

# We need to print every member of a list on new line 
# sep='\n'


print(*map(lambda a: " "*int(30+30*math.sin(a)) + "*", 
     list(takewhile(lambda i: i < 15, accumulate(repeat(0), lambda i, _: i + .1)))),
     sep='\n')
 
