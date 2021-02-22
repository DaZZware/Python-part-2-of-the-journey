# Trust Fund Buddy Bad
# Demonstrates a logical error

print(
"""
            Trus Fund Buddy

Totals your Monthly spending so that your trust fund doesn't run out
(and you're forced to get a real job).

Please Enter the requested, nonthly costs. Since you're rich, ignore pennies
and use only the dollar amounts.

"""
)

car = input("Lamborghini Tune-Ups: ")
rent = input("Manhattan Apartment: ")
jet = input("Private Jet Rental: ")
gifts = input("Gifts: ")
food = input("Dining Out: ")
staff = input("Staff (butlers, chef, driver, assistant): ")
guru = input("Personal Gurur and Coach: ")
games = input("Computer Games: ")

total = car + rent + jet + gifts + food + staff + guru + games

print("Grant total = ", total)

input("\n\n Enter to Exit")
