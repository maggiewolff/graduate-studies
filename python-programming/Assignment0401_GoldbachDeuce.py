#Name: Maggie Wolff
#Due Date: 2/4/20
#Assignment0402_GoldbachDeuce
#I have not given or received any unauthorized assistance on this assignment.
#Video Link: https://youtu.be/O2gHrknwzK4

def main():
    repeat = 'y'
    while repeat == 'y':

        #ask user for i (num of integers) and n (sum)
        i, n = inputs()

        #create list of i random numbers between 0-100
        lst = createlist(i)

        #determine if two of those numbers sum to n
        if n > 200:
            print('Sum not possible.\n')
        else:
            result = findsum(lst, n)
            print(result)

        #ask if user would like to repeat 
        repeat = input('Would you like to try again?')
        if repeat[0] != 'y':
            print('Goodbye')

def inputs():
    #get inputs from user
    statusi = 'false'
    while statusi == 'false':
        i = input('How many random numbers do you want in the list? The numbers generated for the list will be between 0-100.')
        try:
            val = int(i)
            i = int(i)
            statusi = 'true'
        except: 
            print('Please enter an integer.')
    statusn = 'false'
    while statusn == 'false':
        n = input('What number do you want to be the total?')
        try:
            val = int(n)
            n = int(n)
            statusn = 'true'
        except: 
            print('Please enter an integer.')
    return i, n

def createlist(i):
    #create list of i random numbers
    import random 
    lst = []
    for x in range(i):
        num = random.randrange(0,101)
        lst.append(num)
    return lst

def findsum(lst, n):
    #determine if two numbers in the list can sum to n
    lst.sort()
    print('List has been sorted',lst)
    print('Looking for two numbers that sum to',n)

    result = 'No sum found'
    check = -1
    while (len(lst) > 1) and (check == -1):
        x = lst[0]
        if x <= n:                              # if X is the smallest number and bigger than N, no two numbers from list will work.
            y = n - x 
            if lst[1] <= y:                     # list is shrinking with each iteration, so make sure smallest number is still less than N.
                lst.pop(0)                      # remove first number in list, don't need to check it again in future iterations.
                if result == 'No sum found':
                    check = search(y,lst)    
                    if check > 0:
                        result = ('Found in the list: ') + str(x) + (' + ') + str(y) + (' = ') + str(n)
                else:
                    check = -2
        else:
            check = -2

    return result


def search(y, lst):
    # use a binary search to find if Y is in the list of remaining numbers
    spot = -1
    low = 0
    high = len(lst) - 1
    while (low <= high) and (spot == -1):  
        mid = (low + high)//2  
        item = lst[mid]
        if y == item:        
            spot = mid
        elif y < item:       
            high = mid - 1   
        elif y > item:
            low = mid + 1     
        else:
            print('Number not found')

    return spot


main()

