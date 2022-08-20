#Name: Maggie Wolff
#Assignment0401_Pyramid
#Due Date: 2/5/20
#Honor Statement: I have not given or received any unauthorized assistance on this assignment
#Video Link: https://youtu.be/aDLtHYUDmb0

def main():
    repeat = 'y'
    while repeat == 'y':

        #ask for the row, column to check
        rowcolumn = getinputs()
        row = int(rowcolumn[0])
        column = int(rowcolumn[1])

        #calculate the weight
        total = humanPyramid(row, column)

        #print the result
        print('The weight is', total,'\n')

        #ask if they'd like to repeat 
        repeat = input('Would you like to check another row, column?')
        repeat = repeat[0]
        if repeat[0] != 'y':
            print('Goodbye')


def getinputs():
    #ask for the row,column and validate that it is a spot on the pyramid
    #otherwise display an error and ask for a new input

    status = 'false'
    rcint = 'false'
    while status == 'false':
        while rcint == 'false':
            rowcolumn = input('What row, column would you like to check? Input as two numbers with no space between.')
            try:
                val = int(rowcolumn)
                rcint = 'true'
                row = int(rowcolumn[0])
                column = int(rowcolumn[1])
                if (row <= 4) and (column <= 4):
                    if row >= column:
                        status = 'true'  
                    else:
                        print('Not a valid spot on the pyramid.','\n')
                        rcint = 'false'
                else:
                    print('Row and/or column don\'t exist in the pyramid.','\n')
                    rcint = 'false'
            except ValueError:
                print('Input should be an integer.','\n')
    return rowcolumn


def humanPyramid(row,column):
    #calculate how much weight is on the back of the person in that spot
    if (row == 0) and (column == 0):
        return 0
    elif (column == 0): 
        return (humanPyramid(row-1,column))/2 + 64
    elif (row == column):
        return (humanPyramid(row-1,column-1))/2 + 64
    else:
        return (humanPyramid(row-1,column-1))/2 + humanPyramid(row-1,column)/2 + 128

    
main()
