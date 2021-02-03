# DragonSnax

import random
import time

exitChoice = "Nothing"

while exitChoice != "Exit":
    print("You are in a dark room in a mysterious castle")
    print("In front of you there are 4 doors, You must choose one.")
    time.sleep(1)
    playerChoice = input("Choose 1, 2, 3 or 4... ")

    if playerChoice == '1':
        print("The Room is full of Treasure. You're rish!!")
        print("Game Over, You win!")
    elif playerChoice == '2':
        print("The door opens and an angry Ogre hits you with his club/")
        print("Game Over. You Lose!")
    elif playerChoice == '3':
        print("You go into the room and find a sleeping dragon!")
        time.sleep(1)
        print("You can either:")
        time.sleep(.5)
        print("1) Try to Steal some of the dragons gold.")
        time.sleep(1)
        print("or")
        time.sleep(1)
        print("2) Try to sneak around the dragon to the exit.")
        dragonChoice = input("Type 1 or 2.. ")
        if dragonChoice == '1':
            print("The dragon wakes up and eats you. You are delicious!")
            print("Game Over! You Lose")
        elif dragonChoice == '2':
            print("You sneak around the dragon and escapt the castle, blicking in the sunshine.")
            print("Game Over. You Won!")
        else:
            print("Sorry, you didn't enter 1 or 2!")
    elif playerChoice == '4':
        print("You Enter a room with a sphinx.")
        print("It asks you to guess what number it is thinking of, between 1 and 10.")
        number = int(input("What Number do you Choose? "))
        if number == random.randint(1,10):
            print("The sphinx hisses in disappointment. You guessed correctly.")
            print("She must let you go free!")
            print("Game Over. You Win!")
        else:
            print("The sphinx tell syou that your guess is incorrect.")
            print("You are now her prisoner forever!")
            print("Game Over. You Lost!")
    else:
        print("Sorry, you didn't enter 1, 2, 3 or 4!")
        print("Run the game again to have another go!")
    exitChoice = input("Press return to play again, or type Exit to leave: ")
    
