# Name: Maggie Wolff
# Due Date: 01/22/2020
# Assignment0202_StemLeaf
# I have not given or received any unauthorized assistance on this assignment.
# Video Link: https://youtu.be/Xz6QHBRuLcE 

def main():
    #runs the intro and the rest of the functions
    #they are separated like this so the intro doesn't repeat 
    greeting()
    functions()

def functions():
    #this includes all of the functions that are needed to pick a file, read it, create the plot, display it
    #and then prompt the user if they want to repeat 
    file = pickfile()
    list1 = readfile(file)
    stemleafplot = createplot(list1)
    display(stemleafplot)
    repeat()

def greeting():
    #explain the program to the user
    print('This program will: ')
    print('1. Read a list of numbers from a file.')
    print('2. Create and display a stem and leaf plot from those numbers.')
    print('3. Repeat until you are done. Have fun.','\n')

def repeat():
    #prompt the user if they want to repeat
    again = input('Do you want to try again? Y/N')
    if (again[0] == 'Y') or (again[0] == 'y'):
        functions()
    else:
        print('Goodbye.')

def pickfile(): 
    #prompt the user to select a file
    file = 0
    while file == 0:
        n = input('Which file would you like to use? Enter 1 or 2 or 3: ')
        if n == '1':
            file = 1
        elif n == '2':
            file = 2
        elif n == '3':
            file = 3
        else:
            file = 0
            print('Incorrect input. Try again.')
    return file

def readfile(file):
    #read in the file number that the user selected 
    if file == 1:
        filename = ('C:/Users/mwolff/source/repos/Assignment0202_StemLeaf/StemAndLeaf1.txt')
    elif file == 2:
        filename = ('C:/Users/mwolff/source/repos/Assignment0202_StemLeaf/StemAndLeaf2.txt')
    elif file == 3: 
        filename = ('C:/Users/mwolff/source/repos/Assignment0202_StemLeaf/StemAndLeaf3.txt')
    else:
        print('You did not pick a file correctly. File 1 will be used.')
        filename = ('C:/Users/mwolff/source/repos/Assignment0202_StemLeaf/StemAndLeaf1.txt')
    infile = open(filename,'r')
    list1 = infile.readlines()
    infile.close()
    min = int(list1[0])
    max = int(list1[0])
    count = 1
    for i in range (1,len(list1)):
        count += 1
        if int(list1[i]) < min:
            min = int(list1[i])
        elif int(list1[i]) > max:
            max = int(list1[i])
    print('There are',count,'numbers in File',file,'ranging from',min,'to', max,'\n')
    return list1

def createplot(list1):
    #determine the best size for the split, sort the numbers into a stem & leaf plot
    uniquestems, stems, leaves = splitnumbers(list1)
    stefleafdict = sortedlist(uniquestems, stems, leaves)
    return stefleafdict

def splitnumbers(list1):
    #determine the best size for the split and split the numbers into stem & leaf lists 
    n = size(list1)
    uniquestems, stems, leaves = splitlist(n, list1)
    return uniquestems, stems, leaves
    
def size(list1): 
    #determine best size to split into stems & leaves

    max = int(list1[0])
    for i in range (1,len(list1)):
        if int(list1[i]) > max:
            max = int(list1[i])
    strmax = str(max)

    if len(strmax) == 1:
        print('The largest number is only 1 digit, cannot split into stem & leaf')
        n = 0
    elif len(strmax) == 2:
        print('The largest number is 2 digits, leaves will be 1 digit')
        n = 1

    #if the largest number is 3 digits or longer, determine the optimal size for the stem & leaf plot 
    elif len(strmax) == 3:
        check1 = check(list1,1)
        check2 = check(list1,2)
        if check1 < check2:
            n = 1
        else:
            n = 2
    elif len(strmax) == 4:
        check1 = check(list1,1)
        check2 = check(list1,2)
        check3 = check(list1,3)
        if check1 < check2 and check1 < check3:
            n = 1
        elif check2 < check1 and check2 < check3:
            n = 2
        else:
            n = 3
    print('The optimal leaf size is',n,'\n')
    return n

def check(list1,x): 
    #to check for the optimal split
    #create list of stems if X numbers are removed, determine the average leaf size
    #calculate the ratio of leaves to stems, closest to 1 is most proportional  
    #return ratio value to compare with other splits 

    #create list of stems
    templist1 = []
    countall1 = 0
    for i in range (0, len(list1)):
        s = list1[i].strip()
        strs = str(s)
        if len(strs) <= x:
            stem1 = 0
        else:
            stem1 = int(s[:-x])
        templist1.append(stem1)
        countall1 += 1
    
    #filter, sort, and count unique values in stem list
    uniqueset1 = set(templist1) 
    uniquestems1 = (list(uniqueset1))
    uniquestems1.sort()
    countstems1 = 0
    for i in uniquestems1: 
        countstems1 += 1
    
    #calculate how many leaves there will be per stem on average
    avgleaf = countall1 // countstems1
    print('If the leaves are',x,'digit(s): There will be',countstems1,'stems with an average of',avgleaf,'leaves per stem')

    #calcuate the leaf to stem ratio. this will be compared with other splits to determine the optimal split. 
    ratio = avgleaf / countstems1
    #closest to 1 is the most proportional stem & leaf plot, so find the absolute value of 1 minus the value of the ratio. 
    #whichever scenario has the lowest score will be chosen as the best number for splitting. 
    score = abs(1-ratio)
    return score

def splitlist(n, list1): 
    #based on best size, split each number into a stem and a leaf 

    #create list of stems to sort, and lists of each stem and each leaf by index
    sortedstems = []
    stems = []
    leaves = []
    for i in range (0, len(list1)):
        s = list1[i].strip()
        strs = str(s)
        if len(strs) <= n:
            stem = 0
            leaf = s
        else:
            stem = int(s[:-n])
            leaf = int(s[-n])
        sortedstems.append(stem)
        stems.append(stem)
        leaves.append(leaf)
    
    #filter, sort, and count unique values in sortedstems list
    uniqueset = set(sortedstems)
    uniquestems = (list(uniqueset))
    uniquestems.sort()

    return uniquestems, stems, leaves

def sortedlist(uniquestems, stems, leaves): 
    #create the list of leaves associated to each stem 

    stemleafdict = {}
    for i in range(0, len(uniquestems)):
        u = uniquestems[i]
        leaflist = []
        for x in range (0,len(stems)):
            s = stems[x]
            if s == u:
                leaflist.append(leaves[x])
        stemleafdict[u] = leaflist

    return stemleafdict

def display(stemleafdict):
    #display the sorted stem & leaf plot 
    print('Stem | Leaves')
    for d in stemleafdict:
        print('{:>3}'.format(d), ' |',stemleafdict[d])

main()

