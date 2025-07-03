from constants import BORDER
from characters import Characters

def character_selection(prompt):
    print(prompt)
    for character in Characters:
        print(character.description)
    selection = input("\nEnter character name: ")
    while selection not in [character.name for character in Characters]:
        print("That's not a character. Please choose from the list above.")
        print("\n")
        selection = input()
    for character in Characters:
        if character.name == selection:
            print(BORDER)
            return character

def game_mode(prompt):
    modes = ["\n", "Hero Battle", "Campaign"] # Prompt - Which game mode would you like to play?
    print(prompt)
    for mode in modes:
        print(mode)
    selection = input("\nWhich game mode do you want to play?")
    while selection not in [mode for mode in modes]:
        print("That's not a mode. Please choose from the list above.")
        print("\n")
        selection = input()
    for mode in modes:
        if mode == selection:
            print(BORDER)
            return selection



