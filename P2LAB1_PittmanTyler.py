# Tyler Pittman
# 03-07-2025
# P2LAB1
# This assignment shows knowledge of how to write code that performs mathematical calculations and displays information to users

pi = 3.14159

radius = float(input('What is the radius of the circle? '))

diameter = radius * 2

circumference = 2 * pi * radius

area = pi * (radius ** 2)

print(f'The diameter of the circle is {diameter:.1f}')

print(f'The circumference of the circle is {circumference:.2f}')

print(f'The area of the circle is {area:.3f}')
