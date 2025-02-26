# Tyler Pittman
# 02/25/2025
# P1HW1
# Assignment to showcase knowledge of how to write code that collects information, prossesses it, then displays results.

print('-----Calculating Exponents----\n')

print('Enter an integer as a base value:', end=' ') 
base=int(input())

print('Enter an integer as the exponent:', end=' ')
exp=int(input())
print()
result= base ** exp

print(base, 'raised to the power of', exp, 'is', result, '!!\n')

print('-----Addition and Subtraction----\n')

print('Enter a starting integer:', end=' ')
start=int(input())

print('Enter an integer to add:', end=' ')
add=int(input())

print('Enter an integer to subtract', end=' ')
sub=int(input())
print()
result2= start + add - sub

print(start, '+', add, '-', sub, 'is equal to', result2)
