#Guessing number VS

import random

number = random.randint(1, 100)

print("         Welcome to 'Guess the Number' Vs the Computer!")
print("\n\n")
print("The Computer has selected number between 1 and 100.")
print("Try to guess it in as few attempts as possible. First to Guess Wins!! \n")
pNumber = int(input("Please type your selected number for the computer to guess between 1 and 100."))
guess = int(input("Type your first guess of the number: "))
tries = 1
compGuess = random.randint(1, 100)
cTries = 1
while compGuess != pNumber:
    if compGuess <= pNumber:
        compGuess = random.randint(compGuess, 100)
        cTries += 1
    else:
        compGuess = random.randint(1, compGuess)
        cTries += 1

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
    print("Bang on the money well done!\n It took you", tries,"guesses.\nThe computer took",cTries,"guesses")
    
input("Press Enter to exit")