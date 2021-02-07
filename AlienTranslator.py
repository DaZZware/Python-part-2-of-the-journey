# Alien Translator - using dictionally to create translation code

alienDictionary = {"we": "vorag", "come": "thang", "in": "zon", "peace": "argh", "hello": "kodar", \
    "can": "zank", "i": "az", "borrow": "liftit", "some": "zum", "rocket": "upgoman", "fuel": "kakboom", \
        "please": "seplin", "don't": "baaaaaaaarn", "shoot": "flabil", "welcome": "unkip", "our": "mandig", "new": "brang", \
            "alien": "marangin", "overlords": "bap"}
englishPhrase = input("Please enter an English word or phrase to translate: ")
englishWords = englishPhrase.lower().split() # split turns string into list splitting at spaces

alienWords = [] # blank list created 
for word in englishWords: # runs as long as there is words
    if word in alienDictionary: 
        alienWords.append(alienDictionary[word]) # line 12 and 13 if work in alienDictionary to englist work key brinngs to alienword list
    else:
        alienWords.append(word) # this adds words not in list to untranslated
print ("In alien, says: ", " ".join(alienWords)) # displays the translation, join bringing the translated works to list