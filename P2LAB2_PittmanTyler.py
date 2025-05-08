car_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = car_mpg.keys()

print(keys)
print()
car_input = input("Enter a vehicle to see it's mpg: ")
print()
print(f"The", car_input, "gets", car_mpg[car_input], "mpg.")
print()
miles = int(input(f"How many miles will you drive the {car_input}?"))
print()
gallons = miles / car_mpg[car_input]
print(f'{gallons:.2f}', 'gallon(s) of gas are needed to drive the', car_input, miles, 'miles.')
