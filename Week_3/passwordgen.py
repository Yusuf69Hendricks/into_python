# Password 
# Name: Yusuf Hendricks 
# Date: 22nd May 2020

import random


lowerchars = ['a','b','c','d','e','f','g']
upperchars = ['A','B','C','D','E','F','G']
specialchars = ['&','!','*','$','@']
numericchars = ['1','2','3','4','5','6','7']

password = random.choice(lowerchars) + random.choice(upperchars) + random.choice(specialchars) + random.choice(numericchars)

password = password + password + password

print(password)
