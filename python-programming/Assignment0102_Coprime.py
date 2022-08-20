# Author: Maggie Wolff
# Due Date: 01/15/2020
# I have not given or received any unauthorized assistance on this assignment
# Video link: https://youtu.be/8oXCq1XCW0Q


# Function 'coprime' will check if two numbers are coprime and return 'are' for coprime and 'are not' if they aren't coprime

def coprime(a, b):
    status = 'are'
    # if a is not the smaller of the two numbers, switch their positions
    if b < a: 
        (a, b) = (b, a)
    # if b is divisible by a, then the numbers are no coprime
    if b % a == 0:
        print('These numbers are divisible by each other')
        status = 'are not'
    else:
        # for efficiency, we divide the smaller number by 2 so we don't test unecessary numbers 
        half = a // 2
        for i in range (2, half+1, 1):
            if a % i == 0:
                if b % i == 0:
                    print('Both numbers are divisible by ' + str(i))
                    status = 'are not'
                    break
    return status


# Function 'coprime_test_loop' will ask user for two numbers, run those numbers in function 'coprime' and can be repeated or ended

def coprime_test_loop():
    loop = int(input('Would you like to test two numbers to see if they are coprime? Enter 1 for yes or 0 for no'))
    while loop == 1:
        a = int(input('Enter the first number'))
        b = int(input('Enter the second number'))
        result = coprime(a, b)
        print('These numbers ' + result + ' coprime')
        loop = int(input('Would you like to test two numbers to see if they are coprime? Enter 1 for yes or 0 for no'))
    else:
        print('Goodbye')


# Run the function 'coprime_test_loop' to prompt for two numbers and then automatically run 'coprime' which returns whether or not the numbers are coprime

coprime_test_loop()

