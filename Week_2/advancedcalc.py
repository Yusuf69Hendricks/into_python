# Building an advanced calculator 
# Name: Yusuf Hendricks 
# Date: 15th May 2020

print("Addition = +")
print("Subtraction = -")
print("Division = /")
print("Multiplication = *")

print()

# the float turns the input into a number
num1 = float(input("Enter first number: "))
opp = input("Enter operator: ")
num2 = float(input("Enter second number: "))



# Indentation is important with if statements

if opp == "+":
 print(num1 + num2)
elif opp == "-":
 print(num1 - num2)
elif opp == "/":
 print(num1 / num2)
elif opp == "*":
 print(num1 * num2)

else: 
  print("Please enter a valid operator")


