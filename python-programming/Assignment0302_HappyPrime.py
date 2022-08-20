#Name: Maggie Wolff
#Assignment0302_HappyPrime
#Due Date: 01/29/2020
#I have not given or received any unauthorized assistance on this assignment.
#Video Link: https://youtu.be/I_Kp4x04ZYQ

def main():
    #get an integer input from user
    #test if number is prime or not
    #test if number is "happy" or not
    #return both results in one statement
    #ask if repeat or end 
    again = 'yes'
    while again == 'yes':
        testN = getinteger()
        primeStatus = testprime(testN)
        happyStatus = testhappy(testN)
        print(testN,'is',happyStatus,primeStatus)
        again = repeatprompt()

def getinteger():
    #prompt the user for an integer to test 
    testN = abs(int(input('Enter a number to check if it is a happy or sad and prime or not:')))
    return testN

def testprime(testN):
    #test if the integer is prime
    nHalf = testN // 2
    primeStatus = 'prime'
    for i in range (2,nHalf+1,1):
        if testN % i == 0:
            primeStatus = 'not-prime'
    return primeStatus

def testhappy(testN):
    #test if the integer is happy or sad 
    #if the eventual sum of squaring each digit = 1, then happy
    #if the eventual sum repeats back to testN or to a number already found, then it's sad

    testN2 = str(testN)
    sum = 0
    checked = []
    #checked will store all the sums, if that number comes up again, we know the number is sad 

    while (sum !=1) and (sum != testN) and (testN2 not in checked):
        sum = 0
        for i in range(0,len(testN2)):
            sum += int(testN2[i])**2
        checked.append(testN2)
        testN2 = str(sum)
    if sum == 1:
        happyStatus = 'happy'
    elif sum == int(testN):
        happyStatus = 'sad'
    elif str(sum) in checked:
        happyStatus = 'sad'
    else:
        happyStatus = 'inconslusive'

    return happyStatus

def repeatprompt():
    #ask the user if they want to test again or end

    again = input('Would you like to test another number?')
    if (again[0] == 'Y') or (again[0] == 'y'):
        again = 'yes'
    else: 
        print('Goodbye.')

    return again

main()