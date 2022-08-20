# Name: Maggie Wolff
# Due Date: 02/12/2020
# Assignment 0501 Dice & Cups
# I have not given or received any unauthorized assistance on this assignment.
# Video Link:  https://youtu.be/6ZHHxO73sT8

class SixSidedDie:
    'simulates rolling a 6-sided die'

    def __init__ (self, n = 6):
        'initialize sides of the die to 6'
        self.sides = n
               
    def roll(self):
        'simulate rolling the die by picking a random number based on the number of sides'
        self.value = random.randrange(1,self.sides+1,1)

    def getFaceValue(self):
        'return the value of the roll'
        return (self.value)

    def __repr__ (self):
        'representation of the value'
        return 'SixSidedDie({})'.format(self.value)


class TenSidedDie(SixSidedDie):
    'simulates rolling a 10-sided die, inherits rolling function from SixSidedDie'

    def __init__ (self, n = 10):
        'initialized sides of die to 10'
        self.sides = n

    def __repr__ (self):
        'representation of the value'
        return 'TenSidedDie({})'.format(self.value)


class TwentySidedDie(SixSidedDie):
    'simulates rolling a 20-sided die, inherits rolling function from SixSidedDie'

    def __init__ (self, n = 20):
        'initialized sides of die to 20'
        self.sides = n

    def __repr__ (self):
        'representation of the value'
        return 'TwentySidedDie({})'.format(self.value)


class Cup():
    'simulates rolling a certain number of die and returns the sum of the face values'

    def __init__ (self, n6 = 1, n10 = 1, n20 = 1):
        'sets the number of each die in the cup'
        self.six = n6
        self.ten = n10
        self.twenty = n20

    def roll (self):
        'simulates rolling the dice in the cup'
        self.value = 0
        self.lst = []
        if self.six > 0:
            for i in range(self.six):
                p = SixSidedDie()
                p.roll()
                p.getFaceValue()
                self.value += p.getFaceValue()
                self.lst.append(p)
        if self.ten > 0:
            for i in range(self.ten):
                p = TenSidedDie()
                p.roll()
                p.getFaceValue()
                self.value += p.getFaceValue()
                self.lst.append(p)
        if self.twenty > 0:
            for i in range(self.twenty):
                p = TwentySidedDie()
                p.roll()
                p.getFaceValue()
                self.value += p.getFaceValue()
                self.lst.append(p)
    def getSum(self): 
        'returns the sum of the face values of the dice'
        return (self.value)

    def __repr__ (self):
        'representation of the face value of each die'
        return 'Cup({})'.format(self.lst)


cup = Cup(4,1,2)
cup.roll()
cup.getSum()
cup

#help(cup)