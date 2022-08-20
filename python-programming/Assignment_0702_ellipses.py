# Name: Maggie Wolff
# Due Date: 2/26/20
# Assignment 0702 Overlapping Ellipses
# I have not given or received any unauthorized assistance on this assignment.
# Video Link: https://youtu.be/5kYRLsqE0KQ


import time 
import os
import math

class PseudoRandomNumberGenerator:
    'generates a pseudorandom number'

    def __init__ (self, n = (int( ((time.time()) % (math.sqrt(math.sqrt(time.time())))) + (math.sqrt(math.sqrt (time.time())) ) )) ):
        'initialize seed to timestamp if no seed value is passed in'
        self.seed = n

        # open War and Peace
        os.chdir('C:\\Users\\mwolff\\source\\repos\\Assignment_07')
        self.war = open('war-and-peace.txt', 'r')   
        self.war.close
               
    def getSeed(self):
        'return the value of the seed'
        return (self.seed)

    def random(self):
        'generates a random number'

        self.sum = 0 
        count = 1
        n2 = 1 
        self.war.read(self.seed)
        reset = (int( ((time.time()) % (math.sqrt(math.sqrt(time.time())))) + (math.sqrt(math.sqrt (time.time())) ) ))
        
        while count <= 16:
            # get two letters from the text
            if (self.war.read(99) == ''):
                self.war.seek(reset)
                l1 = self.war.read(1).lower()
            else:
                self.war.read(99)
                l1 = self.war.read(1).lower()
            if (self.war.read(99) == ''):
                self.war.seek(reset)
                l2 = self.war.read(1).lower()
            else:
                self.war.read(99)
                l2 = self.war.read(1).lower()
            
            #compare the 2 letters to generate a 0 or 1 and multiple by n2 /= 2
            if (l1 != l2) and (l1 != '') and (l2 != ''):
                n2 /= 2
                if l1 < l2:
                    n1 = 1
                else: 
                    n1 = 0
                self.sum += (n1 * n2)
                count += 1

        return (self.sum)

    def __repr__ (self):
        'representation of the random number'
        return 'Random number is ({})'.format(self.sum)




class Point():
    'takes x and y coordinates of a point'

    def __init__ (self, c1 = 0, c2 = 0):
        'initialize the coordinates'
        self.c1 = c1
        self.c2 = c2

    def returnCoords(self):
        'return the points'
        return (self.c1, self.c2)

    def __repr__ (self):
        'representation of the points'
        return 'Points are ({}, {})'.format(self.c1, self.c2)


class Ellipse():
    'takes two points and width of ellipse'

    def __init__ (self, p1 = (0,0), p2 = (0,0), w = 2):
        'initialize points and width'
        self.p1 = p1
        self.p2 = p2
        self.w = w

    def returnEllipse(self):
        'return the values of the ellipse'
        return (self.p1, self.p2, self.w)

    def __repr__ (self):
        'representation of the points and width'
        return 'Ellipse is ({},{}) and ({},{}) and width is {}'.format(self.p1.c1, self.p1.c2, self.p2.c1, self.p2.c2, self.w)



def box (e1, e2):
    'calculate area of box and coordinates of the corners'

    #find max width
    if e1.w > e2.w:
        wMax = e1.w
        wMin = e2.w
    else: 
        wMax = e2.w
        wMin = e1.w

    # find max and min x and y values and adjust with max/2 widths
    xMax = (wMax/2) + max(e1.p1.c1, e1.p2.c1, e2.p1.c1, e2.p2.c1)
    xMin = min(e1.p1.c1, e1.p2.c1, e2.p1.c1, e2.p2.c1) - (wMax/2)
    yMax = (wMax/2) + max(e1.p1.c2, e1.p2.c2, e2.p1.c2, e2.p2.c2)
    yMin = min(e1.p1.c2, e1.p2.c2, e2.p1.c2, e2.p2.c2) - (wMax/2)

    # calculate area of box
    area = (xMax - xMin) * (yMax - yMin) 

    return xMin, xMax, yMin, yMax, area


def checkRandomPoints(e1,e2,xRange,yRange,xMin,yMin):
    'generate random x,y points, check if they are within overlap, count how many are in overlap'

    overlapCount = 0 
    checkedCount = 0

    prng = PseudoRandomNumberGenerator()

    print('\nEllipse 1 is ({},{}) and ({},{}) with width of {}'.format(e1.p1.c1,e1.p1.c2,e1.p2.c1,e1.p2.c2,e1.w))
    print('Ellipse 2 is ({},{}) and ({},{}) with width of {}'.format(e2.p1.c1,e2.p1.c2,e2.p2.c1,e2.p2.c2,e2.w))

    # check random points

    while checkedCount < 100000:

        # generate random points 
        rx = xMin + (prng.random() * xRange)
        ry = yMin + (prng.random() * yRange)

        # check if in overlap
        e1d1 = math.sqrt( (rx - e1.p1.c1)**2 + (ry - e1.p1.c2)**2 )
        e1d2 = math.sqrt( (rx - e1.p2.c1)**2 + (ry - e1.p2.c2)**2 )

        e2d1 = math.sqrt( (rx - e2.p1.c1)**2 + (ry - e2.p1.c2)**2 )
        e2d2 = math.sqrt( (rx - e2.p2.c1)**2 + (ry - e2.p2.c2)**2 )

        if e1.w > (e1d1 + e1d2):
            if e2.w > (e2d1 + e2d2):
                overlapCount += 1
    
        checkedCount += 1

    print('\n',checkedCount,'points checked and',overlapCount,'points in overlap')
    overlapPercent = overlapCount / checkedCount

    return overlapPercent


def computeOverlapOfEllipses(e1, e2):
    'computes the area of overlap of two ellipses'

    # calculate box around ellipses
    xMin, xMax, yMin, yMax, area = box(e1, e2)

    # find range
    xRange = xMax - xMin
    yRange = yMax - yMin

    # generate random points, count how many are within overlap
    overlapPercent = checkRandomPoints(e1,e2,xRange,yRange,xMin,yMin)

    overlap = overlapPercent * area 
    print('Area of the overlap is', overlap)

    return overlap


##### circles with radius 1 = overlap should be pi
p1 = Point(0,0)
p2 = Point(0,0)
p3 = Point(0,0)
p4 = Point(0,0)

e1 = Ellipse(p1,p2,2)
e2 = Ellipse(p3,p4,2)

computeOverlapOfEllipses(e1, e2)


##### other example

p1 = Point(2,0)
p2 = Point(0,1)
p3 = Point(0,0)
p4 = Point(1,3)

e1 = Ellipse(p1,p2,4)
e2 = Ellipse(p3,p4,5)

computeOverlapOfEllipses(e1, e2)

    