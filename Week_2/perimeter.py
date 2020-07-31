# Perimeter 
# Name: Yusuf Hendricks 
# Date: 15th May 2020

# width
# height
# price/meter

w1 = float(input("Enter the first width: "))
h1 = float(input("Enter the first height: "))
w2 = float(input("Enter the second width: "))
h2 = float(input("Enter the second height: "))
price = int(input("Enter the price per metre: "))
h3 = (h1-h2) / 2
# result = 2*(w1) + 2*(w2) + 1*(h1) + 1*(h1) + (h1 -h2)
result = (w1 + w2 + w1 + w2 + h1 + h2) + h3 + h3
tot_price = result * price

print()
print("Total Fence Required: %d" %result,"metres")
print("Total Price: R %d" %tot_price)

