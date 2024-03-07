# declare local variables
monthlySales = 0  # monthly sales amount
storeAmount = 0  # store bonus amount
empAmount = 0  # employee bonus amount
salesIncrease = 0  # percent of sales increase
prompt = "Enter monthly sales and sales increase percentage: "

# Getting monthly sales and sales increase
monthlySales = float(input("Enter the monthly sales: "))
salesIncrease = float(input("Enter the sales increase percentage (as a decimal): "))
salesIncrease /= 100  # Converting percentage to a decimal

# Calculating the store bonus
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

# Calculating the employee bonus
if salesIncrease >= 0.05:
    empAmount = 75
elif salesIncrease >= 0.04:
    empAmount = 50
elif salesIncrease >= 0.03:
    empAmount = 40
else:
    empAmount = 0

# Printing bonus information
print(f"The store bonus amount is ${storeAmount}")
print(f"The employee bonus amount is ${empAmount}")
if storeAmount == 6000 and empAmount >= 75:
    print("Congrats! You have reached the highest bonus amounts possible!")
