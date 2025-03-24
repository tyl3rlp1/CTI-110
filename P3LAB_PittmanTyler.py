#Tyler Pittman
#P3LAB
#03-23-2025
#This assignment demonstrates knowledge of if-else statements



amount = float(input('Enter the amount of money as a float: $ '))

cents = int(amount * 100)
#NO CHANGE
if cents == 0:
    print('No Change')
    
#DOLLARS MATH
dollars = cents // 100
cents = cents - (dollars * 100)
#QUARTERS MATH
quarters = cents // 25
cents = cents - (quarters * 25)
#DIMES MATH
dimes = cents // 10
cents = cents - (dimes * 10)
#NICKLES MATH
nickels = cents // 5
cents = cents - (nickels * 5)
#PENNIES MATH
pennies = cents


#SHOW DOLLARS
if dollars:
    print(f"{dollars} {'Dollar' if dollars == 1 else 'Dollars'}")
#SHOW QUARTERS    
if quarters:
    print(f"{quarters} {'Quarter' if quarters == 1 else 'Quarters'}")
#SHOW DIMES    
if dimes:
    print(f"{dimes} {'Dime' if dimes == 1 else 'Dimes'}")
#SHOW NICKLES    
if nickels:
    print(f"{nickels} {'Nickel' if nickels == 1 else 'Nickels'}")
#SHOW PENNIES    
if pennies:
    print(f"{pennies} {'Penny' if pennies == 1 else 'Pennies'}")
