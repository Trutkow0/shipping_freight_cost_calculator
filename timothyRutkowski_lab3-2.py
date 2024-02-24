# Timothy Rutkowski 02/07/2024 timothyRutkowski_lab3-2.py

# This program will calculate the cost of shipping freight for 'Jim Bob's Pretty
# Good Freight' company. This program will accept weight in kilograms or pounds as 
# input by the user, calculate the shipping rate, calculate the sales tax, 
# and display each calulated value and the total charges.

# User inputs pounds or kilograms
weightInput = int(input("Will weight be in pounds or kilos? \nEnter 1 for pounds or 2 for kilos: "))

# User inputs weight
weight = float(input("Enter the weight of the package: "))

# Convert weight to kilograms if input is in pounds
if weightInput == 1:
    weightKg = weight / 2.2
elif weightInput == 2:
    weightKg = weight
else:
    # Print error message for invalid input and return
    print("Invalid input!")
    exit()

# Calculate the shipping charge based on weight
if weightKg <= 2:
    shippingCharge = 1.50 * weightKg
elif 2 < weightKg <= 6:
    shippingCharge = 3.00 * weightKg
elif 6 < weightKg <= 10:
    shippingCharge = 4.00 * weightKg
else:
    shippingCharge = 4.75 * weightKg

# Calculate sales tax based on shipping charge
salesTax = shippingCharge * 0.0685

# Calculate total charge including shipping charge and sales tax
totalCharge = shippingCharge + salesTax

# Display calculated shipping charge, sales tax, and total charge
print("\nShipping charge: ${:.2f}".format(shippingCharge))
print("Sales tax: ${:.2f}".format(salesTax))
print("Total Shipping charge: ${:.2f}".format(totalCharge))