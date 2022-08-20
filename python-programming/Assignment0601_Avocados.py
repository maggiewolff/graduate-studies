# Name: Maggie Wolff
# Due Date: 2\19\20
# Assignment0601_Avocados
# I have not given or received any unauthorized assistance with this assignment
# Video Link: https://youtu.be/-5ElUZTUtzE 

import statistics
import os

def readheader(filename):
    'reads in the first row of a file'

    os.chdir('C:\\Users\\mwolff\\source\\repos\\Assignment0601_Avocados\\Assignment0601_Avocados')
    infile = open(filename, 'r')
    head = infile.readline()
    head = head.split(',')
    infile.close

    return head, infile

def findindex(head, var):
    'finds the index of the variable'

    count = 0
    done = 'no'
    for i in head:
        if done == 'no':
            if i == var:
                target = var
                done = 'yes'
            else:
                count +=1

    return count

def createlist(count, infile):
    'creates of list of values for that variable'

    lst = []
    rowcount = 0
    for row in infile: 
        newline = row.split(',')
        vol = float(newline[count])
        lst.append(vol)
        rowcount += 1

    return lst, rowcount

def readAndComputeMean_SM(var):
    'computes the mean of that variable using the Statistics module'
    
    head, infile = readheader('avocado.csv')
    indx = findindex(head, var)
    vals, obs = createlist(indx, infile)
    mean_lst = statistics.mean(vals)
    return mean_lst

def readAndComputeSD_SM(var):
    'computes the standard deviation of that variable using the Statistics module'
    
    head, infile = readheader('avocado.csv')
    indx = findindex(head, var)
    vals, obs = createlist(indx, infile)
    sd_lst = statistics.pstdev(vals)
    return sd_lst

def readAndComputeMedian_SM(var):
    'computes the median of that variable using the Statistics module'
    
    head, infile = readheader('avocado.csv')
    indx = findindex(head, var)
    vals, obs = createlist(indx, infile)
    median_lst = statistics.median(vals)
    return median_lst

mean_SM = readAndComputeMean_SM('Total Volume')
sd_SM = readAndComputeSD_SM('Total Volume')
median_SM = readAndComputeMedian_SM('Total Volume')



def readAndComputeMean_HG(var):
    'calculates the mean of that variable'
    
    head, infile = readheader('avocado.csv')
    indx = findindex(head, var)
    vals, obs = createlist(indx, infile)
    totalsum = 0
    for i in vals:
        totalsum += i
    mean_hg = totalsum / obs

    return mean_hg


def readAndComputeSD_HG(var):
    'computes the standard deviation of that variable'
    
    head, infile = readheader('avocado.csv')
    indx = findindex(head, var)
    vals, obs = createlist(indx, infile)
    mean_hg = readAndComputeMean_HG(var)

    sumsq = 0
    for x in vals:
        sumsq += (x - mean_hg) ** 2

    import math
    sd_hg = math.sqrt(sumsq / obs)

    return sd_hg

def readAndComputeMedian_HG(var):
    'computes the median of that variable'
    
    head, infile = readheader('avocado.csv')
    indx = findindex(head, var)
    vals, obs = createlist(indx, infile)
    vals.sort()
    if (obs % 2) == 0:
        target1 = int((obs-1)/2)
        target2 = int(target1+1)
        median_hg = (vals[target1] + vals[target2]) / 2
    else: 
        target = int((obs+1)/2)
        median_hg = vals[target-1]

    return median_hg


mean_HG = readAndComputeMean_HG('Total Volume')
sd_HG = readAndComputeSD_HG('Total Volume')
median_HG = readAndComputeMedian_HG('Total Volume')


def readAndComputeMean_MML(var):
    'calculates the mean of that variable without storing more than one row of the file in memory'
    
    head, infile = readheader('avocado.csv')
    indx = findindex(head, var)

    rowcount = 0
    sum = 0
    for row in infile: 
        newline = row.split(',')
        sum += float(newline[indx])
        rowcount += 1

    mean_mml = sum / rowcount

    return mean_mml

def readAndComputeSD_MML(var):
    'computes the standard deviation of that variable without storing more than one row in memory'
    
    head, infile = readheader('avocado.csv')
    indx = findindex(head, var)
    mean_mml = readAndComputeMean_MML(var)

    rowcount = 0
    sumsq = 0
    for x in infile:
        newline = x.split(',')
        sumsq += (float(newline[indx]) - mean_mml) ** 2
        rowcount += 1

    import math
    sd_mml = math.sqrt(sumsq / rowcount)

    return sd_mml



def binsof10(indx, infile):
    'sorts the numbers into 10 bins to find the median'

    c_above = c_below = 0

    # find the initial min, max and count of values
    min, max, rowcount = minmaxcount(indx, infile)

    # sort numbers into bins until the counts above and below are within 0 or 1 of each other
    if rowcount % 2 != 0:
        while ((abs(c_above-c_below) > 0) or (c_above == c_below == 0)):
            min, max, c_above, c_below = sortbins(min, max, rowcount, indx, infile, c_above, c_below)
    else:
        while ((abs(c_above-c_below) > 1) or (c_above == c_below == 0)):
            min, max, c_above, c_below = sortbins(min, max, rowcount, indx, infile, c_above, c_below)

    # the median should be within the range of the remaining bin
    median_mml = findmedian(infile, min, max, indx, c_above, c_below)

    return median_mml


def minmaxcount(indx, infile):
    'find the min, max, and count of values'

    infile.seek(0)
    head = infile.readline()

    newline = infile.readline()
    newline = newline.split(',')
    max = float(newline[indx])
    min = max
    rowcount = 1
    for row in infile: 
        newline = row.split(',')
        val = float(newline[indx])
        rowcount += 1
        if val > max:
            max = val
        elif val < min:
            min = val

    return min, max, rowcount

def sortbins(min, max, rowcount, indx, infile, c_above, c_below):
    'sort and count the values into bins'

    # create 10 equal sized bins
    binwidth = (max - min) / 10 
    bin1 = min + binwidth 
    bin2 = bin1 + binwidth
    bin3 = bin2 + binwidth
    bin4 = bin3 + binwidth
    bin5 = bin4 + binwidth
    bin6 = bin5 + binwidth
    bin7 = bin6 + binwidth
    bin8 = bin7 + binwidth
    bin9 = bin8 + binwidth

    # initilize the bin counts to 0
    c_bin1 = c_bin2 = c_bin3 = c_bin4 = c_bin5 = c_bin6 = c_bin7 = c_bin8 = c_bin9 = c_bin10 = 0

    infile.seek(0)
    head = infile.readline()

    # sort the values into bins and count how many are in each bin
    for x in infile:
        row = x.split(',')
        val = float(row[indx])
        if val < bin1:
            c_bin1 += 1
        elif val < bin2:
            c_bin2 += 1
        elif val < bin3:
            c_bin3 += 1
        elif val < bin4:
            c_bin4 += 1
        elif val < bin5:
            c_bin5 += 1
        elif val < bin6:
            c_bin6 += 1
        elif val < bin7:
            c_bin7 += 1
        elif val < bin8:
            c_bin8 += 1
        elif val < bin9:
            c_bin9 += 1
        else:
            c_bin10 += 1

    # calculate the percentiles of each bin
    b_min = c_below / rowcount
    pbin1 = c_bin1 / rowcount
    pbin2 = pbin1 + (c_bin2 / rowcount)
    pbin3 = pbin2 + (c_bin3 / rowcount)
    pbin4 = pbin3 + (c_bin4 / rowcount)
    pbin5 = pbin4 + (c_bin5 / rowcount)
    pbin6 = pbin5 + (c_bin6 / rowcount)
    pbin7 = pbin6 + (c_bin7 / rowcount)
    pbin8 = pbin7 + (c_bin8 / rowcount)
    pbin9 = pbin8 + (c_bin9 / rowcount)
    pbin10 = pbin9 + (c_bin10 / rowcount)
    a_max = c_above / rowcount

    # find range of bin that contains 50th percentile, reset min and max to that bin, count values above and below  
    if pbin1 >= 0.5:
        c_above = rowcount - c_bin1
        max = bin1
        count = c_bin1
    elif pbin2 >= 0.5:
        c_above = rowcount - (c_bin1+c_bin2)
        c_below = c_bin1
        min = bin1
        max = bin2
        count = c_bin2
    elif pbin3 >= 0.5:
        c_above = rowcount - (c_bin1+c_bin2_c_bin3)
        c_below = c_bin1+c_bin2
        min = bin2
        max = bin3
        count = c_bin3
    elif pbin4 >= 0.5:
        c_above = rowcount - (c_bin1+c_bin2+c_bin3+c_bin4)
        c_below = c_bin1+c_bin2+c_bin3
        min = bin3
        max = bin4
        count = c_bin4
    elif pbin5 >= 0.5:
        c_above = rowcount - (c_bin1+c_bin2+c_bin3+c_bin4+c_bin5)
        c_below = c_bin1+c_bin2+c_bin3+c_bin4
        min = bin4
        max = bin5
        count = c_bin5
    elif pbin6 >= 0.5:
        c_above = rowcount - (c_bin1+c_bin2+c_bin3+c_bin4+c_bin5+c_bin6)
        c_below = c_bin1+c_bin2+c_bin3+c_bin4+c_bin5
        min = bin5
        max = bin6
        count = c_bin6
    elif pbin7 >= 0.5:
        c_above = rowcount - (c_bin1+c_bin2+c_bin3+c_bin4+c_bin5+c_bin6+c_bin7)
        c_below = c_bin1+c_bin2+c_bin3+c_bin4+c_bin5+c_bin6
        min = bin6
        max = bin7
        count = c_bin7
    elif pbin8 >= 0.5:
        c_above = rowcount - (c_bin1+c_bin2+c_bin3+c_bin4+c_bin5+c_bin6+c_bin7+c_bin8)
        c_below = c_bin1+c_bin2+c_bin3+c_bin4+c_bin5+c_bin6+c_bin7
        min = bin7
        max = bin8
        count = c_bin8
    elif pbin9 >= 0.5:
        c_above = rowcount - (c_bin1+c_bin2+c_bin3+c_bin4+c_bin5+c_bin6+c_bin7+c_bin8+c_bin9)
        c_below = c_bin1+c_bin2+c_bin3+c_bin4+c_bin5+c_bin6+c_bin7+c_bin8
        min = bin8
        max = bin9
        count = c_bin9
    else:
        c_below = c_bin1+c_bin2+c_bin3+c_bin4+c_bin5+c_bin6+c_bin7+c_bin8+c_bin9
        min = bin9
        count = c_bin10

    return min, max, c_above, c_below


def findmedian(infile, min, max, indx, c_above, c_below):
    'iterate through list and find the value between the min and max'

    median_mml = 0

    infile.seek(0)
    head = infile.readline()

    if c_above == c_below:
        for x in infile:
            row = x.split(',')
            val = float(row[indx])
            if min <= val <= max:
                median_mml = val

    elif c_above != c_below:
        sum = 0
        for x in infile:
            row = x.split(',')
            val = float(row[indx])
            if min <= val <= max:
                sum += val
        median_mml = sum / 2

    return median_mml

def readAndComputeMedian_MML(var):
    'calculates the meadian of that variable without storing more than one row of the file in memory'
    
    head, infile = readheader('avocado.csv')
    indx = findindex(head, var)
    median_mml = binsof10(indx, infile)

    return median_mml



mean_MML = readAndComputeMean_MML('Total Volume')
sd_MML = readAndComputeSD_MML('Total Volume')
median_MML = readAndComputeMedian_MML('Total Volume')


print('Mean Volume:\nStats module:  ',mean_SM,'\nMy calculation:',mean_HG,'\nMemoryless:    ',mean_MML,'\n\nStandard Deviation:\nStats module:  ',sd_SM,'\nMy calculation:',sd_HG,'\nMemoryless:    ',sd_MML,'\n\nMedian Volume: \nStats module:  ',median_SM,'\nMy Calculation:',median_HG,'\nMemoryless:    ',median_MML)
