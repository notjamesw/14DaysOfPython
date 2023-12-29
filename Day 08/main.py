name = input("What is your name?")
place = input("Where do you live?")
color = input("What is your favourite colour?")
number = input("Pick a number between 1 and 10:")
number = int(number)
our_story = f"""Once upon a time {name} wanted to leave {place} in search of a
magic adventure! {name} wanted to collect {number} {color} crystals of hope. 
Soon {name} found {number} of {color} crystals but on the way home... alas...
one crystal fell out of our adventures bag and only {number - 1} {color} 
crytals made it back. 
"""

print(our_story)