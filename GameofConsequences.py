# Game of Consequences
import random
# List to be chosen by random
woman = ["a Scientist","a Queen","a Pirate","a Giant Rabbit"]
man = ["a Police Officer","an Artist","Your Grandfather","a Killer Robot"]

place = ["on Pluto", "at the SuperMarket", "in a Spooky, Bat-filled Cave"]

sheWore = ["Scuba Diving Gear","Fairy Wings","a Paper Bag"]
heWore = ["a Purple suit","a Shark Costume","a Beach Towel"]

womanSays = ["'Who are You?'","'How many beans make five?'","'Why?'"]
manSays = ["'Beep Boop'","'Don't eat frogs!'","'What time do You call this?'"]

consequences = ["World Peace","Chaos","a giant foot squashed them","rainbows."]

worldSaid = ["'Errant Nonesense'","'Cheese is trending now'","'I'm melting!'"]

while True:
    print(random.choice(woman), "met", random.choice(man), random.choice(place)) # selecting random from list inside ()
    print("She was wearing", random.choice(sheWore))
    print("He was wearing", random.choice(heWore))
    print("She said,", random.choice(womanSays))
    print("He said,", random.choice(manSays))
    print("The consequence was", random.choice(consequences))
    print("The world said,", random.choice(worldSaid))
    print()
    input("Press Enter to play again.")
    print()