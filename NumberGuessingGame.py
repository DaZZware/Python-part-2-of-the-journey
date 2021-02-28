# Number Guessing game

import random

number = random.randint(1, 100)

print("         Welcome to 'Guess My Number'!")
print("\n\n")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible. \n")
guess = int(input("Type your first guess of the number: "))
tries = 1

while guess != number:
    print("Unlucky guess again")
    if guess <= number:
        print("Your Guess was to low.")
        guess = int(input("Type your next guess: "))
        tries += 1
    else:
        print("Your Guess was to high.")
        guess = int(input("Type your next guess: "))
        tries += 1
else:
    print("Bang on the money well done!\n It took you", tries,"guesses.")
    
input("Press Enter to exit")
