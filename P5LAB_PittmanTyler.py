#Tyler Pittman
#04-20-2025
#P5LAB
#This assignment demonstrates the use of loops, functions and module import to complete assignments


import random

def disperse_change(change):
    # Convert dollars to cents
    cents = int(change * 100)

    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents


    if dollars:
        print(f"{dollars} {'Dollar' if dollars == 1 else 'Dollars'}")
    if quarters:
        print(f"{quarters} {'Quarter' if quarters == 1 else 'Quarters'}")
    if dimes:
        print(f"{dimes} {'Dime' if dimes == 1 else 'Dimes'}")
    if nickels:
        print(f"{nickels} {'Nickel' if nickels == 1 else 'Nickels'}")
    if pennies:
        print(f"{pennies} {'Penny' if pennies == 1 else 'Pennies'}")

def main():
    money_owed = float(f"{random.uniform(0.01, 100.00):.2f}")
    money_owed_cents = int(money_owed * 100)
    print(f"You owe ${money_owed_cents // 100}.{money_owed_cents % 100:02d}")

    money_payed = float(input("How much cash will you put in the self-checkout? "))
    money_payed_cents = int(money_payed * 100)

    while money_payed_cents < money_owed_cents:
        print("Insufficient funds. Please try again.")
        money_payed = float(input("How much cash will you put in the self-checkout? "))
        money_payed_cents = int(money_payed * 100)

    change_cents = money_payed_cents - money_owed_cents
    print(f"Change is: ${change_cents // 100}.{change_cents % 100:02d}\n")

    disperse_change(change_cents / 100)

main()

