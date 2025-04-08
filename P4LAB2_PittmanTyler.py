#P4LAB2
#Tyler Pittman
#04-06-2025
#This program creates a multiplication table using while and for statements




prog_start = 0
integer_input = int(input('Enter an integer: '))


while prog_start == 0:
    if integer_input <= -1:
        print('This program does not handle negative numbers.')
        try_again = input('Would you like to run the program again? ')
        if 'yes' in try_again:
            integer_input = int(input('Enter an integer:'))
        elif 'no' in try_again:
            print('Exiting program...')
            exit()

    else:
        for i in range(1, 13):
            print(f'{integer_input} * {i} = {integer_input * i}')
        try_again = input('Would you like to run the program again? ')
        if 'yes' in try_again:
            integer_input = int(input('Enter an integer:'))
        elif 'no' in try_again:
            print('Exiting program...')
            exit()
