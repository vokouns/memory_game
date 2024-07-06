import os
import string


user_ready = ""

# Clear the terminal screen
def term_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Dictionary to store the items for each letter
items_dict = {}

# Asks if ready
def ready():
    print("Let's play a memory game!")
    user_ready = input("Are you ready? (y)es or (n)o")
    if user_ready == "y":
        print("Great, here we go!")
    elif user_ready == "n":
        print("COME ON YOU WIMP LET'S GOOOOOOO")
    else:
        print("NO MAYBES ABOUT IT") 
        print("It's a (y)es or (n)o question!")

# Function to add items for a specific letter
def add_items_for_letter(letter):
    items = input(f"What is a food that starts with the letter '{letter}': ").split()
    items_dict[letter] = items

# Function to prompt the user to recall items for all letters from 'a' to the current letter
def recall_items():
    for letter in string.ascii_lowercase:
        if letter in items_dict:
            term_clear()
            recalled_items = input(f"What was the food that started with the letter {letter}: ").split()
            correct_items = items_dict.get(letter, [])
            if recalled_items == correct_items:
                print(f"Correct! You remembered {correct_items}.")
            else:
                print(f"Incorrect. The correct food item for the letter letter '{letter}' was: {correct_items}. Try again next time")
                print("GAME OVER")
                break
            input("Press Enter to continue...")


ready()
# Main loop to iterate through the alphabet
for letter in string.ascii_lowercase:
    add_items_for_letter(letter)

    recall_items()
    if letter == "z":
        break
print("Here are all your food items:\n")
for letter, items in items_dict.items():
    print(f"'Letter {letter}': {', 'join(items)}")