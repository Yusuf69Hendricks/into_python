# Triangle
# Name: Yusuf Hendricks 
# Date: 22nd May 2020

sum1 = float(input("Enter the first side: "))
sum2 = float(input("Enter the second side: "))
sum3 = float(input("Enter the third side: "))

import math 

r1 = (sum1 + sum2 + sum3) / 2

r2 = r1*(r1-sum1)*(r1-sum2)*(r1-sum3)


print("The Area of the triangle with sides of length", sum1, "and", sum2, "and", sum3, "is", (math.sqrt(r2)))
