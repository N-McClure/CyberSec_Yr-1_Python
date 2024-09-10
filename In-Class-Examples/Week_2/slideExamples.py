# Slide 51 of 89:
# ---------------- #

# "Convert the Following Formulas to Python":

# 3 + 4x / 5
x = input("Enter a value for x: ")
ans = (3 + (4 * int(x))) / 5
print(ans)

# ((10 * (y-5)) * (a + b +c)) / x
a = input("Enter a value for a: ")
b = input("Enter a value for b: ")
c = input("Enter a value for c: ")
x = input("Enter a value for x: ")
y = input("Enter a value for y: ")
ans = ((10 * (int(y)-5)) * (int(a) + int(b) + int(c))) / int(x)
print(int(ans))

# "Evaluate the following expressions":

# First Box:
print(20-5/2+3)
print(20-5/(2+3))
print(10*(1+7*3))
print(15%3)
print(10+5%2)
print(10*5%2)

print()

# Second Box:
print(6.0//4.0)
print(20.0-5.0//2.0+3.0)
print(20.0-5.0//(2.0+3.0))
print((20.0-5.0)//(2.0+3.0))

print()

# Third Box:
print(10.0+15/2+4.3)
print(10.0+15.0/2+4.3)
print(3*6.0/4+6)
print(20.0-5/2+3.0)
print(3*4%6+6)

print()
print("****************************************************************")
print()

# ----------------------------------------- #

# Slide 52 of 89:
# ---------------- #

# "Prompt and read the name, age, and salary of the user, display them in a sentence":
name = input("Enter your Name: ")
age = input("Enter your Age: ")
salary = input("Enter your Salary: $")
print("Your name is " + name + ", you are " + age + " years old, and you make $" + salary + " per year.")

print()

# "Read original price and discount, print sale price":
ogPrice = input("Enter the original price: $")
discount = input("Enter the discount: %")
discountValue = int(discount)/100
salePrice = int(ogPrice) - (int(ogPrice) * discountValue)
print("Sale price = $" + str(salePrice))

print()
print("****************************************************************")
print()

# ----------------------------------------- #

# Slide 53 of 89:
# ---------------- #

# "Write a program to calculate the total payments of your order at a pizza store."

# User Name:
name = input("Enter your name: ")

# Small Pizzas:
smallPizzaAmount = input("Enter amount of small pizzas wanted ($9.50 each): ")
smallPizzaCost = int(smallPizzaAmount) * 9.5

# Large Pizzas:
largePizzaAmount = input("Enter amount of large pizzas wanted ($12.99 each): ")
largePizzaCost = int(largePizzaAmount) * 12.99

# Extra Toppings:
extraToppingAmount = input("Enter amount of extra toppings wanted ($1.49 each): ")
extraToppingCost = int(extraToppingAmount) * 1.49

# Drinks / Beverages:
drinkAmount = input("Enter amount of drinks and beverages wanted ($2.23 each): ")
drinkCost = int(drinkAmount) * 2.23

print()

# Total Cost Before Tax: 
totalCostNoTax = smallPizzaCost + largePizzaCost + extraToppingCost + drinkCost
print("Total Cost (Before Tax) = $" + str(totalCostNoTax))

# Total Cost After Tax:
totalCostWithTax = round(totalCostNoTax * 1.05, 2)
print(name + ", your total after tax comes to: $" + str(totalCostWithTax))

print()
print("****************************************************************")
print()

# ----------------------------------------- #

# Slide 54 of 89:
# ---------------- #

# "Write a program to compute the Area of a Circle":
    # --- Required Steps --- #
    # Prompt the user to enter an integer
    # Read the number and assigns it to a variable named radius
    # Calculate the diameter, circumference, and area of the circle with the radius
        # Use "Pi" with a value of 3.14159
    # Display the Results

radius = input("Enter an Integer for the Radius value: ")
diameter = int(radius) * 2
circumference = (2 * 3.14159) * int(radius)
area = (3.14159 * int(radius)) ** 2

print("The Area of a circle with a radius of " + str(radius) + " is " + str(round(int(area), 2)))
print("The Diameter of a circle with a radius of " + str(radius) + " is " + str(round(int(diameter), 2)))
print("The Circumference of a circle with a radius of " + str(radius) + " is " + str(round(int(circumference), 2)))

print()
print("****************************************************************")
print()

# ----------------------------------------- #

# Slide 55 of 89:
# ---------------- #

# "Write a program to calculate final velocity and the distance traversed":
u = input("Enter the initial velocity: ")
a = input("Enter the Acceleration: ")
t = input("Enter the time elapsed (seconds): ")

v = int(u) + (int(a) * int(t))
print("Calculated Final Velocity = " + str(round(int(v),2)) + "m/s")

s = (int(u) * int(t)) + (0.5 * (int(a)*int(t))**2)
print("Calculated Distance Traversed = " + str(round(int(s),2)) + "m/s")

print()
print("****************************************************************")
print()

# ----------------------------------------- #

# Slide 56 of 89:
# ---------------- #

# "Write a program to compute Average from 3 inputted numbers":

# Get 3 values from the User:
val1 = input("Enter a value with a decimal: ")
val2 = input("Enter another value with a decimal: ")
val3 = input("Enter a final value with a decimal: ")

average = (float(val1) + float(val2) + float(val3)) / 3
print("Average = " + str(round(float(average),2)))

print()

# Write a program to convert a temp from Fahrenheit to Celsius":
fTemp = input("Enter a temperature in Fahrenheit: ")
cTemp = ((5.0 / 9.0) * (float(fTemp) - 32.0))
print(str(fTemp) + " degrees Fahrenheight is " + str(round(float(cTemp),2)) + " degrees Celsius")

print()
print("****************************************************************")
print()

# ----------------------------------------- #

# Slide 57 of 89:
# ---------------- #

# "Write a tip calculator to display the bill, the tip percentage, and the total amount":

# Get the Bill amount: 
billAmount = input("Enter the Bill amount: $")

# Get the Tip percentage:
tipPercentage = input("Enter the Tip percentage: %")
tipValue = int(tipPercentage) / 100.0

# Calculate the total Bill Cost and Display everything:
totalCost = int(billAmount) + (float(billAmount) * tipValue)
print("Total Bill Cost = $" + str(float(totalCost)))

print()
print("****************************************************************")
print()
