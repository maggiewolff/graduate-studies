# Name: Maggie Wolff
# Due Date: 3/11/20
# Assignment_0902 Game of Life
# I have not given or received any unauthorized assistance on this assignment.
# Video Link: https://youtu.be/MTC96y8RfX4 



import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors

def conway(s,p):
    'generates a square board of size s with alive and dead cells based on probability p'

    b = Board(s,p)
    b.createArray()
    b.setValues()
    b.plot()

    return b

class Board:
    'create and modify board of alive and dead cells'

    def __init__(self, size = 10, prob = 0.1):
        'initialize size to 10 and probability to 0.1 if values not passed in'
        self.size = size
        self.prob = (prob)   

    def createArray(self):
        'create board as array with random values'
        self.board = np.random.random((self.size,self.size))

    def setValues(self):
        'sets value of each cell to alive or dead based on probability'
        self.board = (self.board <= self.prob).astype(int)
        
    def createEmptyArray(self):
        'create board of empty array'
        self.board = np.empty((0,self.size), int)

    def appendArray(self, newRow):
        'append values to board'
        self.board = np.append(self.board, np.array([newRow]), axis=0)

    def returnSize(self):
        'returns size of board'
        return self.size

    def plot(self):
        'generates visual plot of Board'
        plt.ion()
        plt.imshow(self.board, cmap=plt.get_cmap('BuPu'))
        plt.show()
        plt.draw()
        plt.pause(0.5)

    def __iter__(self, n):
        'iterates through array'
        return self.board[n]

    def __repr__(self):
        'representation of board with 0s and 1s'
        return('\nYour Board\n{}\n'.format(self.board))



def advance(b,t):
    'advances Conway board by t times'

    print('\nStarting Board\n',b,'\n')
    b1 = b
    count = 0
    size = b.returnSize()

    while count < t:
        #create new board based on prior board
        b2 = newBoard(b1,size)
        print('\nNew Board\n',b2,'\n')
        b2.plot()
        b1 = b2 
        count += 1

    return b2

def newBoard(b,s):
    'creates new board based on previous board'

    b_new = Board(s)
    b_new.createEmptyArray()
    count = 0

    while count < s:
        #create rows to append
        newRow = createRow(b,count,s)
        b_new.appendArray(newRow)
        count += 1

    return b_new

def createRow(b,n,s):
    'create new row to append to new board'

    r_new = []
    count = 0

    while count < s:
        #create items to add to new row
        newCell = createCell(b,n,count,s)
        r_new.append(newCell)
        count += 1

    return r_new

def createCell(b,x,y,s):
    'checks values of neighboring cells to determine if alive or dead'

    xrow = b.__iter__(x)
    xabove = b.__iter__(x-1)
    if x != (s-1):
        xbelow = b.__iter__(x+1)
    else:
        xbelow = b.__iter__(0)

    #get existing value (alive or dead) of cell in question
    cell = xrow[y]

    #get values of all eight neighbors and then sum
    n1 = xabove[y-1]
    n2 = xabove[y]
    n4 = xrow[y-1]
    n6 = xbelow[y-1]
    n7 = xbelow[y]
    if y != (s-1):
        n3 = xabove[y+1]
        n5 = xrow[y+1]
        n8 = xbelow[y+1]
    else:
        n3 = xabove[0]
        n5 = xrow[0]
        n8 = xbelow[0]

    nsum = n1+n2+n3+n4+n5+n6+n7+n8

    #determine if new cell is alive or dead 

    if cell == 0: 
        if nsum == 3:
            newcell = 1
        else:
            newcell = 0
    elif cell == 1:
        if (nsum == 2) or (nsum == 3): 
            newcell = 1
        else:
            newcell = 0

    return newcell 


s = 30
p = 0.6
t = 5

b = conway(s,p)
advance(b,t)

plt.pause(2)
plt.close()



