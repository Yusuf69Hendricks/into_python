# Secret 1 
# Name: Yusuf Hendricks 
# Date: 15th May 2020


secret_number = 42
guess = 0 	   


while guess != secret_number:
  guess = eval(input("? "))
  
  if guess < secret_number:
     print ("low")

  elif guess > secret_number:
     print ("high")

  elif guess == secret_number:
     print ("Correct!") 
