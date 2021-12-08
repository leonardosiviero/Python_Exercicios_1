income = float(input("Enter the annual income: ")) #income é renda em inglês

if income < 85528:
    tax = (income * 0.18) - 556.2
    if tax < 0:
        tax = 0
else:
    tax = ((income - 85528) * 0.32) + 14839.2

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
