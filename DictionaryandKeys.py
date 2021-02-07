# Dictionary's (like Lists)and keys

powers = {"The Pigeon": "flight", "Brainzar": "mind reader", "Cyborg": "controls machines"}
# powers = dictionary name, the key comes before the entry in this super hero name, entry/value are powers seperated with colon

print (powers["The Pigeon"]) # displays the value of pigeon
print()
powers["Laser girl"] = "shoots lasers" # adds to the dictionary
print()
# Dictionarys unlink lists dont list in particular order to list 0-2 etc
print(powers) # lists the dictionary including laser
print()
del powers["The Pigeon"] # deletes the pigeon from dictionay, can be selected anytime.
print()
powers["Brainzar"] = "seeing the future" # changes the value of brainzar
print(powers)
