# Secret 2
# Name: Yusuf Hendricks 
# Date: 15th May 2020


secret_number = 69
guess = 0 	



while guess != secret_number:
  guess = eval(input("? "))
  if guess < secret_number:
     print ("Why is the secret number? %d" %guess)
     print("Thats way too low. Please try again.")
     print(guess)

  elif guess > secret_number:
     print ("Why is the secret number? %d" %guess)
     print("Thats way to high. PLease try again.")

  elif guess == secret_number:
     print ("Congratulations, you have guessed the secret number!") 

