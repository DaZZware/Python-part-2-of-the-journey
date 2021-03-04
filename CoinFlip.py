# Coin Flip
# 100 times, how many heads and tails


import random

heads = 0
tails = 0
total = 0

while total != 100:
    flip = random.randrange(2)
    if flip == 1:
        heads += 1
        total +=1
    else:
        tails += 1
        total += 1
        
print("Total coin Flips =",total,"Heads came up",heads,"Tails shown",tails)
input("Enter to Exit")

