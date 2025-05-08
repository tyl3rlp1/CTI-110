#Tyler Pittman
#04-11-2025
#P4HW1
#Improve P2HW2 to use loops

def get_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

num_scores = int(input('How many scores would you like to enter? '))

#List to store grades
grades = [0] * num_scores

#Loop to collect grades
for i in range(num_scores):  
    while True:
        grade = float(input(f'Enter grade for Module {i + 1}: '))
        
        #Validate the grade
        if 0 <= grade <= 100:
            grades[i] = grade
            break  
        else:
            print("INVALID SCORE! TRY AGAIN!.")

        
#Display results
print('\n----------Results----------')

#Lowest grade
lowest_grade = min(grades)

#Remove the lowest grade
grades.remove(lowest_grade)


total = sum(grades)
average = total / len(grades)

# Print the results
print(f'Lowest grade (dropped): {lowest_grade}')
print(f'Highest grade: \t{max(grades)}')
print(f'Sum of grades: \t{total}')
print(f'Average: \t{average:.2f}')
print(f'Grade: \t{get_letter_grade(average)}')

print('---------------------------')
