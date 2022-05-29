# Name: Maggie Wolff
# Due Date: 3/20/20
# Assignment 10-01 Island of Rats and Cats
# I have not given or received any unauthorized assistance on this assignment.
# Video: https://youtu.be/8lmaIWR1ocg


import numpy as np
import pandas as pd
import os 
import random
import csv


class Island:
    'Island with cats who eat rats who eat berries who rely on rain'

    def __init__ (self, island_size, rain_chance, rain_mean, rain_std):
        self.island_size = island_size
        self.rain_chance = rain_chance
        self.rain_mean = rain_mean
        self.rain_std = rain_std

    def rainfall(self):
        'determines if it will rain and if it does generates an amount of rain in mm'
        
        chance = np.random.uniform()

        if chance <= self.rain_chance:
            self.rainf = np.random.normal(loc=self.rain_mean, scale=self.rain_std)
        else:
            self.rainf = 0
    
        return self.rainf

    def getIslandSize(self):
        # return island size
        return self.island_size

class Berry:
    'Berries that grow on the island, dependant on rainfall, and are eaten by the rats'

    def __init__(self, berry_coefficient,berry_persist):
        #initialize berry coefficient
        self.berry_coef = berry_coefficient
        self.berry_persist = berry_persist
        self.berryList = []

    def generateBerries(self, rainf, area, day, rat_count):
        #generate count of new berries based on previous day's rainfall and area of island, appends current day to a list for number of new berries

        newBerryCount = int(rainf * area * self.berry_coef)

        for i in range(0,newBerryCount):
            self.berryList.append(day)

        # remove berries more than 10 days old 
        if day > self.berry_persist:
            age_alive = day - self.berry_persist
            self.berryList = [i for i in self.berryList if i >= age_alive]

        # remove berries eaten by rats
        if rat_count > 0:
            if len(self.berryList) > 0:
                if len(self.berryList) <= rat_count:
                    self.berryList = []
                else:
                    for i in range(rat_count):
                        self.berryList.pop(random.randrange(len(self.berryList))) 


        # count number of berries
        totalBerries = len(self.berryList)

        return totalBerries

class Animal:
    'create Animal class that Rats and Cats class will extend'

    def __init__(self,start_age,days_nofood,oldage,litter1,litters,litter_min,litter_max,animal_count,coefficient,bonus):
        # set values for animal parameters
        self.animalD = {}
        self.start_age = start_age
        self.days_nofood = days_nofood
        self.oldage = oldage
        self.litter1 = litter1
        self.litters = litters
        self.litter_min = litter_min
        self.litter_max = litter_max
        self.animal_count = animal_count
        self.coefficient = coefficient
        self.bonus = bonus

    def appendAnimal(self, age, day):
        # append rat to dictionary of animal values 
        self.animalD[self.animalID] = {'Age': age, 'Last Meal': day, 'Food Count': 0, 'Prev Litters': 0} 

    def generateAnimal(self, newAnimalCount, day):
        # generate new animals

        for i in range(newAnimalCount):
            self.animalID = str('animal' + str(day) + str(i))
            self.appendAnimal(0, day)

    def genInitialAnimals(self):
        # generates the initial set of animals at start of simulation 

        count = 1
        for i in range(self.animal_count):
            age = random.randint(1,self.start_age)
            self.animalID = str('animal' + str(age) + str(i) + str(count))
            self.appendAnimal(age, 0)
            count += 1

    def ageAnimals(self):
        # add a day to every rats age

        for key in self.animalD:
            self.animalD[key]['Age'] += 1

    def countAnimals(self):
        # count number of living rats
        return len(self.animalD)

    def returnAnimalD(self):
        # return rat dictionary
        return self.animalD

class Rats(Animal):
    'create rats with life in days, track how many berries they eat, determine when they give birth and when they die'

    def __init__(self,start_age,days_nofood,oldage,litter1,litters,litter_min,litter_max,animal_count,coefficient=0,bonus=0):
        # set values for rat parameters
        self.animalD = {}
        self.start_age = start_age
        self.days_nofood = days_nofood
        self.oldage = oldage
        self.litter1 = litter1
        self.litters = litters
        self.litter_min = litter_min
        self.litter_max = litter_max
        self.animal_count = animal_count
        self.coefficient = coefficient
        self.bonus = bonus

    def ratsEat(self, berry_count, day):
        # feed the rats and update their Last Meal 

        if len(self.animalD) <= berry_count:
            for key in self.animalD:
                self.animalD[key]['Last Meal'] = day
                self.animalD[key]['Food Count'] += 1
        else: 
            count = 0
            while count < berry_count:
                x = random.choice(list(self.animalD.keys()))
                if self.animalD[x]['Last Meal'] < day:
                    self.animalD[x]['Last Meal'] = day
                    self.animalD[x]['Food Count'] += 1
                    count += 1
    
    def ratBirth(self, day):
        # determine which rats give birth and count their babies to generate new rats

        parents = 0
        babies = 0

        for key in self.animalD:
            if self.animalD[key]['Prev Litters'] == 0:
                if self.animalD[key]['Food Count'] == self.litter1:
                    parents += 1
                    self.animalD[key]['Food Count'] = 0
                    self.animalD[key]['Prev Litters'] = 1
            elif self.animalD[key]['Prev Litters'] > 0:
                if self.animalD[key]['Food Count'] == self.litters:
                    parents += 1
                    self.animalD[key]['Food Count'] = 0
                    self.animalD[key]['Prev Litters'] += 1

        for i in range(parents):
            offspring = random.randint(self.litter_min,self.litter_max)
            babies += offspring

        self.generateAnimal(babies, day)

    def removeDeadRats(self, day, cats_eating):
        # remove dead rats from ratD

        if (self.countAnimals() > 0) and (cats_eating > 0):

            # remove rats eaten by cats 
            d_list = set()

            for i in range(cats_eating):
                key = random.choice(list(self.animalD)) 
                d_list.add(key)

            for i in d_list:
                del self.animalD[i]

            if self.countAnimals() > 0:
                # remove cats who haven't eaten recently or are old
                d_list = []

                for key in self.animalD:

                    # check for rats who haven't eaten in X days
                    if day - self.animalD[key]['Last Meal'] > self.days_nofood:
                        d_list.append(key)

                    # compute probability of deaths for rats X+ days old
                    elif day - self.animalD[key]['Age'] >= self.oldage:
                        dayspast = (self.animalD[key]['Age']) - (self.oldage - 1)
                        p_death = dayspast * 0.05
                        chance = np.random.uniform()
                        if chance <= p_death:
                            d_list.append(key)

                for i in d_list:
                    del self.animalD[i]

class Cats(Animal):
    'create cats with life in days, track how many rats they eat, determine when they give birth and when they die'

    def __init__(self,start_age,days_nofood,oldage,litter1,litters,litter_min,litter_max,animal_count,coefficient,bonus):
        # set values for cat parameters
        self.animalD = {}
        self.start_age = start_age
        self.days_nofood = days_nofood
        self.oldage = oldage
        self.litter1 = litter1
        self.litters = litters
        self.litter_min = litter_min
        self.litter_max = litter_max
        self.animal_count = animal_count
        self.coefficient = coefficient
        self.bonus = bonus


    def catsEat(self, rat_count, day, island_size):
        # feed the cats and update their Last Meal 

        cats_eating = 0

        if rat_count > 0:
            for key in self.animalD:
                age_of_cat = self.animalD[key]['Age'] 
                b = (age_of_cat * self.bonus)
                if b > 1:
                    b = 1
                p_cat_percent = ((rat_count / island_size) * self.coefficient)  
                add_bonus = p_cat_percent + b
                p_cat = add_bonus / 100
                if p_cat > 1:
                    p_cat = 1
                catch = np.random.uniform()
                if catch <= p_cat: 
                    self.animalD[key]['Last Meal'] = day
                    self.animalD[key]['Food Count'] += 1
                    cats_eating += 1

        return cats_eating
    
    def catBirth(self, day):
        # determine which cats give birth and count their babies to generate new rats

        parents = 0
        babies = 0

        for key in self.animalD:
            if self.animalD[key]['Prev Litters'] == 0:
                if self.animalD[key]['Food Count'] == self.litter1:
                    parents += 1
                    self.animalD[key]['Food Count'] = 0
                    self.animalD[key]['Prev Litters'] = 1
            elif self.animalD[key]['Prev Litters'] > 0:
                if self.animalD[key]['Food Count'] == self.litters:
                    parents += 1
                    self.animalD[key]['Food Count'] = 0
                    self.animalD[key]['Prev Litters'] += 1

        for i in range(parents):
            offspring = random.randint(self.litter_min,self.litter_max)
            babies += offspring

        self.generateAnimal(babies, day)

    def removeDeadCats(self, day):
        # remove dead cats from catD

        d_list = []

        for key in self.animalD:

            # check for cats who haven't eaten in X days
            if day - self.animalD[key]['Last Meal'] >= self.days_nofood:
                d_list.append(key)

            # compute probability of deaths for cats X+ days old
            elif day - self.animalD[key]['Age'] >= self.oldage:
                dayspast = (self.animalD[key]['Age']) - (self.oldage - 1)
                p_death = 0.01 + (dayspast * 0.001)
                chance = np.random.uniform()
                if chance <= p_death:
                    d_list.append(key)

        for i in d_list:
            del self.animalD[i]

def simulation(filename):
    # simulate what happens over a certain number of days, return dataframe with daily values 

    # get parameter values 
    os.chdir('C:\\Users\\mwolff\\Documents\\DSC430\\week 10')

    file = open(filename, 'r')
    p_values = {}
    for line in file.readlines():
        line = line.split(',')
        parameter = str(line[0])
        value = float(line[1])
        p_values[parameter] = value

    island_size = p_values['island_size']
    rain_chance = p_values['rain_chance']
    rain_mean = p_values['rain_mean']
    rain_std = p_values['rain_std']
    berry_coefficient = p_values['berry_coefficient']
    berry_persist = p_values['berry_persist']
    rat_count = int(p_values['rat_count'])
    rat_start_age = p_values['rat_start_age']
    rat_days_nofood = p_values['rat_days_nofood']
    rat_oldage = p_values['rat_oldage']
    rat_litter1 = p_values['rat_litter1']
    rat_litters = p_values['rat_litters']
    rat_litter_min = p_values['rat_litter_min']
    rat_litter_max = p_values['rat_litter_max']
    cat_count = int(p_values['cat_count'])
    cat_start_age = p_values['cat_start_age']
    cat_days_nofood = p_values['cat_days_nofood']
    cat_coefficient = p_values['cat_coefficient']
    cat_bonus = p_values['cat_bonus']
    cat_oldage = p_values['cat_oldage']
    cat_litter1 = p_values['cat_litter1']
    cat_litters = p_values['cat_litters']
    cat_litter_min = p_values['cat_litter_min']
    cat_litter_max = p_values['cat_litter_max']
    simulation_days = int(p_values['simulation_days'])

    # create island, berries, rats, cats
    island = Island(island_size, rain_chance, rain_mean, rain_std)
    berry = Berry(berry_coefficient,berry_persist)
    rat = Rats(rat_start_age,rat_days_nofood,rat_oldage,rat_litter1,rat_litters,rat_litter_min,rat_litter_max,rat_count)
    cat = Cats(cat_start_age,cat_days_nofood,cat_oldage,cat_litter1,cat_litters,cat_litter_min,cat_litter_max,cat_count,cat_coefficient,cat_bonus)

    # create dataframe to store daily values
    island_df = pd.DataFrame({'Day':[], 'Prev Day Rainfall':[], 'Berry Count':[], 'Rat Count':[], 'Cat Count':[]})
    island_size = island.getIslandSize()

    # create initial animals 
    rat.genInitialAnimals()
    cat.genInitialAnimals()

    # run simulation 
    for i in range(1,simulation_days+1):
        # simulate all the activities of the island over X days
        print('start day:',i)

        rat_count = rat.countAnimals()
        cat_count = cat.countAnimals()

        # get yesterday's rainfall and generate berries 
        rainf = island.rainfall()
        totalBerries = berry.generateBerries(rainf,island_size,i,rat_count)

        # if there are no cats then there are no rats and there's nothing else to do
        if cat_count > 0:

            # the rats and the cats eat 
            rat.ratsEat(totalBerries, i)
            cats_eating = cat.catsEat(rat_count,i,island_size)

            # the circle of life continues 
            rat.ratBirth(i)
            cat.catBirth(i)
            rat.removeDeadRats(i,cats_eating)
            cat.removeDeadCats(i)

            # count the rats and cats 
            rat_count = rat.countAnimals()
            cat_count = cat.countAnimals()

            # and the rats and cats get a day older
            rat.ageAnimals()
            cat.ageAnimals()

        # append the day's totals 
        day = pd.DataFrame({'Day':[i], 'Prev Day Rainfall':[rainf], 'Berry Count':[totalBerries], 'Rat Count':[rat_count], 'Cat Count':[cat_count]})
        island_df = island_df.append(day, ignore_index = True)
        print('end day:',i)

    return island_df
    

filename = 'island_parameters.csv'
island_df = simulation(filename)
island_df

island_df.to_csv (r'island_dataframe.csv', index = False, header=True)



