# Name: Maggie Wolff
# Due Date: 3/4/20
# Assignment 0801 Plot Generator
# I have not given or received any unauthorized assistance on this assignment.
# Video Link:  https://youtu.be/mi36DsPENgk



import os
import random

class SimplePlotGenerator:
    'generates a simple plot'

    def __init__ (self, viewer = None):
        'initialize'
        self.viewer = viewer

    def registerViewer(self, viewer):
        'register the viewer'
        self.viewer = viewer

    def generate(self):
        'return "Something happens"'
        self.plot = 'Something happens'
        return (self.plot)

    def __repr__ (self):
        'representation'
        if self.viewer == None:
            return '\nSimplePlotGenerator\nThe plot is:\n{}\n'.format(self.plot)

pg = SimplePlotGenerator()
pg.generate()
pg


class RandomPlotGenerator(SimplePlotGenerator):
    'generates a random plot'

    def __init__ (self, viewer = None):
        'initialize'
        self.viewer = viewer

        # set filepath
        os.chdir('C:\\Users\\mwolff\\source\\repos\\Assignment_08')

    def randomWord(self, file):
        'choose random word'

        # open file and set range
        doc = open(file, 'r')  
        lst = list(doc.readlines())
        count = 0
        for i in lst:
            count += 1

        # pick random word
        spot = random.randrange(0,count)
        word = lst[spot].strip('\n')
        doc.close()

        return word

    def generate(self):
        'return a random plot'
        name = self.randomWord('plot_names.txt')
        adjective = self.randomWord('plot_adjectives.txt')
        profesion = self.randomWord('plot_profesions.txt')
        verb = self.randomWord('plot_verbs.txt')
        adjective_evil = self.randomWord('plot_adjectives_evil.txt')
        villain_job = self.randomWord('plot_villian_job.txt')
        villain = self.randomWord('plot_villains.txt')
        self.plot = (name + ' a ' + adjective + ' ' + profesion + ' must ' + verb + ' the ' + adjective_evil + ' ' + villain_job + ' ' + villain + '.')
        return (self.plot)

    def __repr__ (self):
        'representation'
        if self.viewer == None:
            return '\nRandomPlotGenerator\nThe plot is:\n{}\n'.format(self.plot)


pg = RandomPlotGenerator()
pg.generate()   
pg


class InteractivePlotGenerator(SimplePlotGenerator):
    'create a plot based on user selections'

    def __init__ (self, viewer = None):
        'initialize'
        self.viewer = viewer

    def selectWord(self, file, topic):
        'pick 5 random options and prompt user to select one'

        # create empty set to store options
        self.options = set()

        # open file and set range
        doc = open(file, 'r')  
        lst = list(doc.readlines())
        count = 0
        for i in lst:
            count += 1

        # pick random words until you have 5 in the set
        while len(self.options) < 5: 
            spot = random.randrange(0,count)
            word = lst[spot].strip('\n')
            self.options.add(word)

        doc.close()

        # ask user to select 1 word 

        if self.viewer == None:
            print('Using the Generator i/o')
            self.selection = self.userSelect(topic)
            
        else:
            pv = self.viewer
            print('Using the Viewer i/o')
            self.selection = pv.userSelect(self.options, topic)

        self.selection = self.selection - 1
        self.options = list(self.options)
        word = self.options[self.selection]

        return word
 
    def userSelect(self, topic):
        'prompts the user to pick a word and returns index'

        print('\nInteractive Plot Generator:\n')

        count = 1
        print('Your options for ' + topic + ' are:')
        for i in self.options:
            print(count,')',i)
            count += 1

        num = -1
        while num == -1: 
            choice = input('Enter the number for your choice: ')
            try:
                val = int(choice)
                if val > 0 and val <= 5:
                    num = int(choice)
                else: 
                    print('Please enter a number between 1-5')
            except ValueError:
                print('Enter an integer.')

        return num 

    def generate(self):
        'generate a plot based on user selections'
        name = self.selectWord('plot_names.txt', 'hero\'s name')
        adjective = self.selectWord('plot_adjectives.txt', 'hero\'s adjective')
        profesion = self.selectWord('plot_profesions.txt', 'hero\'s profession')
        verb = self.selectWord('plot_verbs.txt', 'verb')
        adjective_evil = self.selectWord('plot_adjectives_evil.txt', 'evil adjective')
        villain_job = self.selectWord('plot_villian_job.txt', 'villain\'s job')
        villain = self.selectWord('plot_villains.txt', 'villain\'s name')
        self.plot = (name + ' a ' + adjective + ' ' + profesion + ' must ' + verb + ' the ' + adjective_evil + ' ' + villain_job + ' ' + villain + '.')
        return (self.plot)

    def __repr__ (self):
        'representation'
        if self.viewer == None:
            return '\nInteractivePlotGenerator\nThe plot is:\n{}\n'.format(self.plot)


pg = InteractivePlotGenerator()
pg.generate()   
pg

