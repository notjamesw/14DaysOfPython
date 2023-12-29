print("""
You find yourself standing at the edge of a mysterious enchanted forest. 
The trees loom overhead, and the air is filled with a soft, magical glow.
As you take your first step into the forest, you notice two paths ahead.

1. Take the left path
2. Take the right path
      """)

path = input("Which path will you choose?")
path = int(path)

if path == 1:
    user_input = input("You see a cave do you enter the cave?\n(yes/no)")
    if user_input == "yes":
        print("You enter the cave. It's dark and you slip... Game Over.")
    elif user_input == "no":
        print("You avoid the cave and find a nice clearing, you find a bar of gold. You win!")
elif path == 2:
    print("As you take the right path, you realize that you are stuck in the forest's illusion. Game Over.")

