# Name: Maggie Wolff
# Due Date: 2/26/20
# Assignment 0701 War and Random Numbers
# I have not given or received any unauthorized assistance on this assignment.
# Video Link: https://youtu.be/H5Xm91u7ev8


import time 
import os
import math

class WarAndPeacePseudoRandomNumberGenerator:
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


prng = WarAndPeacePseudoRandomNumberGenerator()
prng.getSeed()
prng.random()
prng


def findMinMaxMean(stop):
    'generates X random numbers and returns min, max, mean'
    
    n = 0
    min = 1
    max = 0
    sum = 0
    
    while n < stop:
        r = prng.random()
        n += 1
        sum += r
        
        if r < min:
            min = r 
        elif r > max:
            max = r

    average = sum / n

    print('\ngenerated',n,'random numbers')
    print('\naverage is', average)
    print('min is', min)
    print('max is', max)

findMinMaxMean(10000)
