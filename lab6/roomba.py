#!/usr/local/bin/python3
# Modified by: Irina Golovko
# Name: roomba.py
# Date: July 15, 2018


# Douglas Putnam, CCSF
# roomba.py, Derived from random_walk.py by
# John Guttag, Eric Grimson, 6.00 Introduction to Computer Science
# Massachusetts Institute of Technology: MIT OpenCouseWare),
# http://ocw.mit.edu (Accessed [Date]). 
# License: Creative Commons BY-NC-SA


import math, random, pylab

class Location(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    def move(self, xc, yc):
        return Location(self.x+float(xc), self.y+float(yc))
    def getCoords(self):
        return self.x, self.y
    def getDist(self, other):
        ox, oy = other.getCoords()
        xDist = self.x - ox
        yDist = self.y - oy
        return math.sqrt(xDist**2 + yDist**2)

class CompassPt(object):
    possibles = ('N', 'S', 'E', 'W')
    def __init__(self, pt):
        if pt in self.possibles: self.pt = pt
        else: raise ValueError('in CompassPt.__init__')
    def move(self, dist):
        if self.pt == 'N': return (0, dist)
        elif self.pt == 'S': return (0, -dist)
        elif self.pt == 'E': return (dist, 0)
        elif self.pt == 'W': return (-dist, 0)
        else: raise ValueError('in CompassPt.move')

class Field(object):
    def __init__(self, roomba, loc):
        self.roomba = roomba
        self.loc = loc
    def move(self, cp, dist):
        oldLoc = self.loc
        xc, yc = cp.move(dist)
        self.loc = oldLoc.move(xc, yc)
    def getLoc(self):
        return self.loc
    def getRoomba(self):
        return self.roomba

class Roomba(object):
    def __init__(self, name):
        self.name = name
    def move(self, field, time = 1):
        if field.getRoomba() != self:
            raise ValueError('Roomba.move called with roomba not in field')
        for i in range(time):
            pt = CompassPt(random.choice(CompassPt.possibles))
            field.move(pt, 1)
            

def performTrial(time, f):
    """performTrial() takes two arguments: time in seconds and a Pylab Field object."""
    start = f.getLoc()
    x_coords = []
    y_coords = []
    for t in range(1, time + 1):
        f.getRoomba().move(f)
        newLoc = f.getLoc()
        x_coords.append(newLoc.getCoords()[0])
        y_coords.append(newLoc.getCoords()[1])
    return x_coords,y_coords


roomba = Roomba("Irina's Roomba")
for i in range(1):
    f = Field(roomba, Location(0, 0))

    # Get the x,y coordinates tuple of lists
    coords = performTrial(500, f)
    
    # Feed the x,y lists to pylab.plot
    pylab.plot(coords[0],coords[1],marker='D',linestyle=':',color='magenta')
 
xc = coords[0] 
yc = coords[1] 

# first coordinates
xf = xc[0]  
yf = yc[0]

# last coordinates
xl = xc[len(xc) -1]  
yl = yc[len(yc) - 1]

pylab.plot(xf, yf, marker='*',color='blue')
pylab.plot(xl, yl, marker='*',color='blue')
pylab.annotate('Start', xy=(xf, yf), color='blue', weight='bold') 
pylab.annotate('Finish', xy=(xl, yl), color='blue', weight='bold')
               
pylab.title('Roomba Trip', color='blue', weight='bold')
pylab.xlabel('East - West of the room', color='blue', weight='bold')
pylab.ylabel('North - South of the room', color='blue', weight='bold')
pylab.show()
