# Author: Maggie Wolff
# Due Date: 01/15/2020
# I have not given or received any unauthorized assistance on this assignment
# Video link: https://youtu.be/GfqDwLs-EuM

# Function 'grade' will ask a series of questions regarding the assignment and return the calculated grade 
# If any of the must-have elements are missing, the questions will end and a grade of 0 points will be returned 

def grade(score = 1, Grade = 0):
    while score != 0:
        score = int(input('Did the author submit a single uncompressed .py file? Type 1 for yes, 0 for no'))
        if score == 0:
            break
        score = int(input('Did the author include their name and the date? Type 1 for yes, 0 for no'))
        if score == 0:
            break
        score = int(input('Did the author include an honor statement? Type 1 for yes, 0 for no'))
        if score == 0:
            break
        score = int(input('Did the author include a link to an unlisted video? Type 1 for yes, 0 for no'))
        if score == 0:
            break
        correct = int(input('Out of 10, how many points for correctness?'))
        elegance = int(input('Out of 10, how many points for elegance?'))
        hygiene = int(input('Out of 10, how many points for code hygiene?'))
        video = int(input('Out of 10, how many points for video quality?'))
        Grade = correct + elegance + hygiene + video
        break
    return Grade

# Run the function which will return the total points 
result = grade()

# Print the returned grade value 
print('The grade is ' + str(result) + ' out of 40 points')
