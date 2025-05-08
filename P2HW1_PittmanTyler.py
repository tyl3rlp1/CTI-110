# Tyler Pittman
# 03/13/2025
# P2HW1
# This code is a modified version of P1HW2 to accomodate the specifications outlined in P2HW1

#Ask the user to enter their budget and destination.
#Ask for the cost of fuel, hotel, and food.
#Subtract the cost of food, fuel, and hotel from the budget to produce a remaining budget.
#Display the results.

print('This program calculates and displays travel expenses\n')

budget = float(input('Enter budget: '))
print()

dest = input('Enter you travel destination: ')
print()

gas = float(input('How much will you spend on gas? '))
print()

hotel = float(input('Approximately, how much will you need for accomodation/hotel? '))
print()

food = float(input('Last, how much do you need for food? '))
print()

print('-----------Travel Expenses-----------')

print('Location:\t\t',dest)

print(f'Initial Budget:\t\t${budget:.2f}')

print(f'Fuel:\t\t\t${gas:.2f}')

print(f'Accommodation:\t\t${hotel:.2f}')

print(f'Food:\t\t\t${food:.2f}')

print('-------------------------------------')
balance = budget - gas - hotel - food
print(f'Remaining Balance:\t${balance:.2f}')
