# Alien Password Game

Aliens = 2

password = 'ALIENS'

print("Quickly! Aliens are Invading.")
print("You need to activat the global defence platform.")
print("Hope you know the password, for Earth's sake.....")
print()
print("--------------------------------------------------")
print("      WELCOME TO THE GLOBAL DEFENCE NETWORK       ")
print("--------------------------------------------------")
print()

guess = input("Please enter the Password! ").upper # turns what ever is typed to upper case
while guess != password:
    print()
    print("INCORRECT PASSWORD!")
    print()
    Aliens = Aliens ** 2
    print("There are", Aliens,"aliens now on Earth try again!")
    if Aliens > 7400000000:
        break
    print()
    print("Password hint: the things that are attacking us.")
    print()
    guess = input("Quick! Please enter the password: ").upper
if Aliens > 7400000000:
    print("Nooooooooooooooooo! The aliens have out numbered us. All is lost.")
else:
    print("Hooray! We wont the fight and the worl is saved!")

input("Enter to close")