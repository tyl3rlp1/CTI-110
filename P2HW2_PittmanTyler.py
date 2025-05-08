#Tyler Pittman
#03-14-2025
#P2HW2
#This assignment displays knowledge of using the contents of a list to produce outcomes.

##Ask user for module grades
##Display the lowest grade in the list
##Display the highest grade in the list
##Display the sum of the grades in the list
##Display the average grade of the list

mod1 = float(input('Enter grade for Module 1: '))
mod2 = float(input('Enter grade for Module 2: '))
mod3 = float(input('Enter grade for Module 3: '))
mod4 = float(input('Enter grade for Module 4: '))
mod5 = float(input('Enter grade for Module 5: '))
mod6 = float(input('Enter grade for Module 6: '))

grades  = [mod1, mod2, mod3, mod4, mod5, mod6]

print('\n----------Results----------')

print(f'Lowest grade: \t{min(grades)}')

print(f'Highest grade:\t{max(grades)}')

print(f'Sum of grades:\t{sum(grades)}')

print(f'Average:\t{sum(grades) / len(grades):.2f}')

print('---------------------------')
