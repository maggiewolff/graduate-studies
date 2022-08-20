# Name: Maggie Wolff
# Due Date: 3/20/20
# Assignment 10-02 Survival Island
# I have not given or received any unauthorized assistance on this assignment.

import numpy as np
import pandas as pd
import matplotlib
import os 
import csv

from matplotlib import pyplot as plt
from matplotlib import colors


rain = island_df['Prev Day Rainfall']
rain.plot()
plt.xlabel('Day')  
plt.ylabel('Rainfall')  
plt.title('Previous Day\'s Rainfall')  
plt.show()


berries = island_df['Berry Count']
berries.plot()
plt.xlabel('Day')  
plt.ylabel('Berry Count')  
plt.title('Count of Total Berries on Island By Day')  
plt.show()


rats = island_df['Rat Count']
rats.plot()
plt.xlabel('Day')  
plt.ylabel('Rat Count')  
plt.title('Count of Total Rats on Island By Day')  
plt.show()


cats = island_df['Cat Count']
cats.plot()
plt.xlabel('Day')  
plt.ylabel('Cat Count')  
plt.title('Count of Total Cats on Island By Day')  
plt.show()