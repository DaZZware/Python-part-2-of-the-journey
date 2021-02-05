# Using lists in basic, can be in more indepth see future ones

spaceList = ['Rocket','Stars','Moon','Planets','Asteroid','Alien']
#creating the list spaceList (Broken down Rocket is start at 0 if being called)

print(spaceList[1]) # printing list item 1 'Stars'
print()
for item in spaceList:
    print(item) # lists in order form 0 names in spaceList
print()
spaceList[0] = "Bumper Droid" # would replace 'Rocket' with 'Bumber Droid' / could be used in games where character name is changed by user ie Final Fantasy Games.
for item in spaceList:
    print(item)
print()
del spaceList[3] # would deleted Planets from list and if printed Astroid would be 3..
for item in spaceList:
    print(item)
print()
spaceList.append("Moon") # would list moon at the end of list
for item in spaceList:
    print(item)
print()
spaceList1 = ['Moon', 'Astroid']
spaceList2 = ['Rocket', 'Alien', 'Stars']
spacelist3 = spaceList1 + spaceList2 
for item in spacelist3:
    print(item) # would combine the 2 lists
