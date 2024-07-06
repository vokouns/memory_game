import os
import string
import sys

# Clear the terminal screen
def term_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Dictionary to store the items for each letter
items_dict = {}

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
                sys.exit(1)
            input("Press Enter to continue...")

# Main loop to iterate through the alphabet
for letter in string.ascii_lowercase:
    add_items_for_letter(letter)
    recall_items()