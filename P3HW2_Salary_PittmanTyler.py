# Tyler Pittman
# 03-27-2025
# P3HW2
# This assignment displays information input by user for calculating regular and overimte pay.

#ask user for input
name = input("Enter employee's name: ")
hours_worked = float(input('Enter number of hours worked: '))
pay_rate = float(input("Enter employee's pay rate: "))
print('----------------------------')

#constants
reg_hours = 40
over_rate = 1.5

#calculating regular and overtime pay
if hours_worked > reg_hours:
    over_hours = hours_worked - reg_hours
    reg_pay = reg_hours * pay_rate
    over_pay = over_hours * (pay_rate * over_rate)
    gross_pay = reg_pay + over_pay
else:
    over_hours = 0
    reg_pay = hours_worked * pay_rate
    over_pay = 0
    gross_pay = reg_pay

#display results
print('Employee name: ', name)
print()

print('Hours Worked   Pay Rate       Overtime       Overtime Pay   RegHour Pay    Gross Pay')
print(f'{hours_worked:<15.2f}{pay_rate:<15.2f}{over_hours:<15.2f}{over_pay:<15.2f}{reg_pay:<15.2f}{gross_pay:<15.2f}')
