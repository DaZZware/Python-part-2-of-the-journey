# Fortune Cookie
# Random fortune 5

import random

print("\n\n          Fortunet Time")
print("\n\nTime to get your fortune read from a cookie.\n")

fortune = random.randint(1, 5)

if fortune == 1:
    print("If you see a one eyed pussy cat with 3 legs, buy a lottery ticket.")
elif fortune == 2:
    print("Good friends will bring you happyness")
elif fortune == 3:
    print("Do not eat yellow snow")
elif fortune == 4:
    print("If you ate the chowmein I predict the toilet is your friend tomorrow.")
elif fortune == 5:
    print("Unlucky for you, you have to do the dishes to pay.")
else:
    print("This is Awkward")



    
    
input("\nEnter to Exit!")
