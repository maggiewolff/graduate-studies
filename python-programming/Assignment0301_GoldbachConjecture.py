#Name: Maggie Wolff
#Assignment0301_GoldbachConjecture
#Due Date: 01/29/2020
#I have not given or received any unauthorized assistance on this assignment.
#Video Link: https://youtu.be/6giOGGqvL70

def main():
    #Create a list of prime numbers and then use those numbers to test if 
    #all even numbers between 4 - 100 can be expressed as the sum of two prime numbers
    primelist = primes()
    goldbach(primelist)

def primes():
    #Creates a list of prime numbers under 100
    primelist = []

    #iterate through list of numbers from 2 to 99
    for p in range(2,98,1):
        #check if prime
        status = checkprime(p)

        #append to primes list if prime
        if status == 'prime':
            primelist.append(p)

    return primelist

def checkprime(p):
    #check if number is prime and return status of 'prime' or 'not-prime'
    phalf = p // 2
    status = 'prime'
    count = 0
    for i in range(2,phalf+1,1):
        if count == 0:
            if p % i == 0:
                status = 'not prime'
                count += 1
 
    return status

def goldbach(primes): 
    #print a list of even numbers from 4 to 98 expressing each number as a sum of two prime numbers
    for i in range(4,99,2):
        count = 0
        for n1 in primes:
            for n2 in primes:
                if n1 + n2 == i:
                    if count == 0:
                        print(i,'=',n1,'+', n2)
                        count += 1

main()


