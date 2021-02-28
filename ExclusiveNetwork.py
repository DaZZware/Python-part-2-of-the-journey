
# Exclusive Network
# Demonstrating logical operators and compount conditions

print("\tExclusive Computer Network")
print("\t\tMembers only!\n")

security = 0

username = ""
while not username: # if simply pressing enter this will loop to username request
    username = input("Username: ")
    
password = ""
while not password: # as with username no password woudl loop request for password
    password = input("Password: ")
    
if username == "M.Dawson" and password == "secret":
    print("Hi, Mike.")
    security = 5
elif username == "S.Meier" and password == "civilization":
    print("Hey, Sid")
    security = 3
elif username == "S.Myamoto" and password == "mariobros":
    print("What's up Shigeru?")
    security = 3
elif username == "W.Wright" and password == "thesims":
    print("How goes it, Will")
    security = 3
elif username == "guest" or password == "guest": # for guess this can be username + password correct or just one or other
    print("Welcome, guest")
    security = 1
else:
    print("Login failed. You're not so exclusive.\n")
    
input("Enter to Exit!")
