# Trust Fund Buddy working
# Demonstrates correct buffy

print(
"""
            Trus Fund Buddy

Totals your Monthly spending so that your trust fund doesn't run out
(and you're forced to get a real job).

Please Enter the requested, nonthly costs. Since you're rich, ignore pennies
and use only the dollar amounts.

"""
)

car =  int(input("Lamborghini Tune-Ups: "))
rent = int(input("Manhattan Apartment: "))
jet = int(input("Private Jet Rental: "))
gifts = int(input("Gifts: "))
food = int(input("Dining Out: "))
staff = int(input("Staff (butlers, chef, driver, assistant): "))
guru = int(input("Personal Gurur and Coach: "))
games = int(input("Computer Games: "))

total = car + rent + jet + gifts + food + staff + guru + games

print("Grant total = ", total)

input("\n\n Enter to Exit")
