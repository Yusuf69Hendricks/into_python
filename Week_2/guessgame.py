# Guessing Game 
# Name: Yusuf Hendricks 
# Date: 15th May 2020

secret_word = "towel"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

print("You have 3 chances to guess the answer to this riddle:")
print("***ONLY ENTER ONE WORD ANSWERS!***")
print()
print("What gets wet, as it drys?")
print()

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter your Guess: ")
        guess_count += 1

    else: 
        out_of_guesses = True

if out_of_guesses:
    print("Unlucky, you`re out of guesses, You lose!")
else:
    print("You win!")

