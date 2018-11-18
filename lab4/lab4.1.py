#!/usr/local/bin/python3
# NAME: Irina Golovko
# FILE: lab4.1.py
# DATE: July 7, 2018
# DESC: Usage of methods from Shape and Circle classes

from shape import Shape
from circle import Circle

c1 = Circle(100, 100, 100)
c2 = Circle(150, 150, 100)

print("Testing Circle class for area(), move(), location(), is_collision()")
print("#" * 28,"\n", "Lab4.1.py\n", "#" * 28, "\n", sep="")
print("Starting with two circles:")
print("Circle 1: ", c1)
print("Circle 2: ", c2)
print()

c1_xdelta = 0
c1_ydelta = 0
c2_xdelta = 0
c2_ydelta = 0

t = [['Num', 'x1', 'y1', 'x2', 'y2', 'Distance', 'Collision?']]

# Test 20 (or more) times    
for i in range(1,21):
    c1.move(c1_xdelta, c1_ydelta)
    c2.move(c2_xdelta, c2_ydelta)
    l1 = c1.location()
    l2 = c2.location()
    df = Circle.distance(c1,c2)
    d = "{:.2f}".format(df)
    collision = str(Circle.is_collision(c1,c2))
    t.append([i, l1[0], l1[1], l2[0], l2[1], d, collision])
   
    c1_xdelta = c1_xdelta + 1
    c1_ydelta = c1_ydelta + 2
    c2_ydelta = c2_ydelta - 1
    c2_xdelta = c2_xdelta + 3
       

# For each list in t:
print('-' * 60)
for i in range (len(t)):
    b = t[i]
    print("|{0:>3}".format(b[0]), "|{0:>6}".format(b[1]), "|{0:>6}".format(b[2]), \
"|{0:>6}".format(b[3]), "|{0:>6}".format(b[4]), "|{0:>9}".format(b[5]), "|{0:>10}|".format(b[6]))
    print('-' * 60)



    