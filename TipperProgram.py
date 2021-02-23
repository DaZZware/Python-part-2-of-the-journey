# Tipper Program

# Work out total and give back 2 total tips back 15% and 20%

print("        The DaZZWare Cafe")
print("\n\n\nThank you for your custom. \nCan you confirm your order: \n")

chips = int(input("How many portions of chips did your table have? "))
coffee = int(input("And how many mugs of coffee(s) had been ordered? "))
tea = int(input("Total cups of Tea? "))
burger = int(input("And how many Burgers were ordered? "))
cake = int(input("Did you have Desert? if so how many cakes? "))

chips1 = chips * 2.65
coffee1 = coffee * 1.55
tea1 = tea * 1
burger1 = burger * 3
cake1 = cake * 2

total = chips1 + coffee1 + tea1 + burger1 + cake1

tip1 = total * 0.20
tip2 = total * 0.15

print("Your bill total is £",total)
print("If you would like to leave a tip of 15% this would be",tip2,"or 20% would be",tip1,"additional to the bill.")

input("Enter to exit")
