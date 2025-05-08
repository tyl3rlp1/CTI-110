total_over_pay = 0
total_reg_pay = 0
total_gross_pay = 0
num_employees = 0

#Constants
reg_hours = 40
over_rate = 1.5

while True:
    #Ask user for employee name
    name = input("Enter employee's name (or 'Done' to stop): ")
    
    #If 'Done', exit the loop
    if name == "Done":
        break
    
    #Get hours worked and pay rate
    hours_worked = float(input(f"Enter number of hours {name} worked: "))
    pay_rate = float(input(f"What is {name}'s pay rate: "))
    print('----------------------------')

    #Calculate regular and overtime pay
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

    #Update totals
    total_over_pay += over_pay
    total_reg_pay += reg_pay
    total_gross_pay += gross_pay
    num_employees += 1

    #Display results for current employee
    print('Employee name:', name)
    print()
    print('Hours Worked   Pay Rate       Overtime       Overtime Pay   RegHour Pay    Gross Pay')
    print(f'{hours_worked:<15.2f}{pay_rate:<15.2f}{over_hours:<15.2f}{over_pay:<15.2f}{reg_pay:<15.2f}{gross_pay:<15.2f}')
    print('----------------------------')

# Display total results after user exits
print("\n----------------------------")
print(f"Total number of employees entered: {num_employees}")
print(f"Total amount of overtime pay: ${total_over_pay:,.2f}")
print(f"Total amount of regular pay: ${total_reg_pay:,.2f}")
print(f"Total amount of gross pay: ${total_gross_pay:,.2f}")
