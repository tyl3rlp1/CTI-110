# Tyler Pittman
# 03-27-2025
# P3HW1
# This assignment debugs a errant version of P2HW2 and adds output of a letter grade.

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

print('\n----------Results----------')
print(f'Lowest grade: \t{min(grades)}')
print(f'Highest grade:\t{max(grades)}')
print(f'Sum of grades:\t{sum(grades)}')
print(f'Average:\t{sum(grades) / len(grades):.2f}')
print('---------------------------')
# determine letter grade for average

average = sum(grades) / len(grades)

if average >= 90:
    print('Your grade is: A')
elif average >= 80:
    print('Your grade is: B')
elif average >= 70:
    print('Your grade is: C')
elif average >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')
# TO DO: finish this





