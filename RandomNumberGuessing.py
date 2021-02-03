# Random Number guessing

import random

number = random.randint(1,20)

print("\n\n\n\n\n\n\n")
guess = int(input("I am thinking of a number between 1 and 20. What is it? "))
while guess != number:
    if guess < number:
        print("Your number is too low..")
    else:
        print("Your number is to high...")
    guess = int(input("Please try again...."))
print("Congradulations! Correct Answer!!")
input("Enter to Exit")
