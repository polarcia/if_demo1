income = float(input("Enter the annual income: "))

if income < 85_528:
     tax = income * 0.18 - 556.02 
else:
    tax =(income - 85_528) * 0.32 + 14_839.02


if tax < 0: tax = 0.0
tax = round(tax, 0)
print("The tax is:", tax, "thalers")
