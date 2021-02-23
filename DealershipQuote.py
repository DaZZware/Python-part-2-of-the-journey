# Dealership quote

print("   Rip you off while you wait Dealership")

carPrice = int(input("\n\n\n\nPlease input the base of the price of the car quoted by 'Honest' John: "))

mot = 300
dealer = 150
dropOff = 60

tax = carPrice * 0.25
insurance = carPrice * 0.30

total = carPrice + mot + dealer + dropOff + tax + insurance

print("\n\nThe total price is:",total,"\nThis includes MOT and service:",mot,
      "\nThe dealer release of ownership:",dealer,"\nThe home delivery fee:",dropOff,
      "\nThe 25% sales Tax:",tax,"\nAnd finally the 1 year parts insurance:",insurance)

input("Enter to Exit")
