# Name: Maggie Wolff
# Due Date: 02/12/2020
# Assignment 0502 Cup & Dice Game
# I have not given or received any unauthorized assistance on this assignment.
# Video Link:  https://youtu.be/7lWWCC5eSC8

import random 

def main():
    'betting game involving dice in a cup'

    name, balance = greeting()
    again = play()

    while (again == 1) and (balance > 0):
        goal = target()
        balance, bet = wager(balance)
        result = game()
        balance = newbalance(goal, balance, bet, result)
        report = summary(name, balance)
        if balance > 0:
            again = play()
    if balance <= 0:
        print('You do not have any more money. Goodbye.')
    else:
        print('Goodbye, '+ name + '. You ended with $' + str(balance))


def greeting():
    'greets user and sets starting balance to $100'
    name = input('Hello. What is your name?')
    balance = 100
    print('Welcome, ' + name +'. Your starting balance is $' + str(balance) + '.\n')

    return name, balance

def play():
    'asks if they would like to play the game'
    ask = input('Would you like to play a round of Cup & Dice?')
    if ask[0].lower() == 'y':
        return 1
    else:
        return 0

def target():
    'generate a random number for the goal'
    goal = random.randrange (1,101)
    print('The goal is',goal)
    return goal

def wager(balance):
    'ask the user for their bet, validate it is an acceptable bet, and update balance'
    status = 'bad'
    while status != 'good':
        bet = input('How much would you like to bet? (Enter the amount only, no $ needed.)')
        try:
            val = int(bet)
            bet = val
            if (val <= balance) and (val >= 0):
                balance = balance - int(bet)
                status = 'good'
            elif val < 0:
                print('Bet cannot be less than zero.')
            else:
                print('Bet cannot be greater than your balance.')
        except:
            print('Please enter an integer.')
    return balance, bet 

def game():
    'select the number of each die and roll'
    print('You can select how many of each die you\'d like to roll, your choices are 6-sided, 10-sided, and 20-sided.')
    n6 = int(input('How many 6-sided die?'))
    n10 = int(input('How many 10-sided die?'))
    n20 = int(input('How many 20-sided die?'))
    cup = Cup(n6,n10,n20)
    cup.roll()
    result = cup.getSum()
    print('You rolled:')
    print(cup)
    print('The sum is ' + str(result) + '.')
    return result 

def newbalance (goal, balance, bet, result):
    'compare the roll to the goal and calculate the new balance'
    if result == goal:
        credit = bet * 10
        print('Wow! You rolled the goal! You get $' + str(credit) + '. \n')
    elif result > goal:
        credit = 0
        print('Too high. You get $' + str(credit) + '. \n')
    elif (result >= (goal - 3)):
        credit = bet * 5
        print('Great job! You rolled within 3 under the goal! You get $' + str(credit) + '. \n')
    elif (result >= (goal - 10)):
        credit = bet * 2
        print('Good job! You rolled within 10 under the goal! You get $' + str(credit) + '. \n')
    else:
        credit = 0
        print('Too low. You get $' + str(credit) + '. \n')

    balance = balance + credit 

    return balance 

def summary(name, balance):
    'report the new balance to the user'
    print(name + ', your new balance is $' + str(balance))


######################################################################################
################################# Dice & Cup Classes #################################
######################################################################################

class SixSidedDie:
    'simulates rolling a 6-sided die'

    def __init__ (self, n = 6):
        'initialize sides of the die to 6'
        self.sides = n
               
    def roll(self):
        'simulate rolling the die by picking a random number based on the sides'
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


main()