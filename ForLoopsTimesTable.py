# for loops use, with nested loop in between


print()
print()
table = int(input("Please enter a times table: ")) 
for x in range(0,13):
    print(x, "x", table, "=", x*table) # Creates time taples 0to12 times the whole number input
    for y in range(1,5):
        print("Bloop") # Nested Loop prints this 4 times inbetwwen each x loop line with Bzzt as closer
    print("Bzzt")
input()

