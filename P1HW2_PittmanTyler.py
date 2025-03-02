# Tyler Pittman
# 02/26/2025
# P1HW2
# This code creates a program that does basic math on numbers that are entered.

#Ask the user to enter their budget and destination.
#Ask for the cost of fuel, hotel, and food.
#Subtract the cost of food, fuel, and hotel from the budget to produce a remaining budget.
#Display the results.

print('This program calculates and displays travel expenses\n')

print('Enter budget:', end=' ')
budget=int(input())
print()

print('Enter you travel destination:', end=' ')
dest=input()
print()

print('How much will you spend on gas?', end=' ')
gas=int(input())
print()

print('Approximately, how much will you need for accomodation/hotel?', end=' ')
hotel=int(input())
print()

print('Last, how much do you need for food?', end=' ')
food=int(input())
print()

print('-----------Travel Expenses-----------')

print('Location:', dest, '\nInitial Budget:', budget)
print()

print('Fuel:', gas, '\nAccomodation:', hotel, '\nFood:', food)
print()

print('Remaining Balance:', budget - gas - hotel - food)
