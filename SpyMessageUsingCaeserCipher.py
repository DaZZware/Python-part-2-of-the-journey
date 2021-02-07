# Spy Message using Caeser Cipher
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ" 
# alphabet repreated just like a list starts 0 to index
print()
stringToEncrypt = input("Please input a message to encrypt: ")
stringToEncrypt = stringToEncrypt.upper() # turns any lower cast letters to upper so no error with alphabet
print()
shiftAmount = int(input("Please enter a whole number from 1 to 25 to be your key. "))
print()
encryptedString = "" # creates a blank string
for currentCharacter in stringToEncrypt: # for loop runs once every letter typed
    position = alphabet.find(currentCharacter) # find() searches the alphabet for fist appearance of current character
    newPosition = position + shiftAmount # shifts the amount in key
    if currentCharacter in alphabet:
        encryptedString = encryptedString + alphabet[newPosition] # looks for shifted letters and adds encrypted message
    else:
        encryptedString = encryptedString + currentCharacter # if character not in alphabet this will be added to encrypted message

print("Your encrypted message is", encryptedString)
