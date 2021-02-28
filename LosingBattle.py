# Losing Battle
# Demonstrating correction on infinit loop

print("Your lone hero is surrounded by a massive army of trolls.")
print("Their decaying green bodies stretch out, melting into the horizon.")
print("Your hero unsheathes his sowrd for the last fight of his life.\n")

health = 10
trolls = 0
damage = 3

#while health != 0: # this was the original while loop creating the infinite loop, as health goes to minus and is never 0.
while health >= 0:
    trolls += 1
    health -= damage
    
    print("Your hero swings and defeats the evil troll, " \
        "but takes", damage, "damage points.\n")
    
input("\n\nPress the Enter key to exit.")
