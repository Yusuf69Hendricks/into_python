# Exponent 
# Name: Yusuf Hendricks 
# Date: 15th May 2020

base_num = int(input("Enter a base number: "))
pow_num = int(input("Enter a power number: "))

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
      result = result * base_num
    return result 

print(raise_to_power(base_num, pow_num))