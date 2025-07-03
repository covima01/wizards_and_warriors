from constants import BORDER
from characters import Characters

def character_selection(prompt):
    print(BORDER)
    print(prompt)
    for character in Characters:
        print(character.description)
    selection = input("\nEnter character name: ")
    while selection not in [character.name for character in Characters]:
        print(BORDER)
        print("That's not a character. Please choose from the list above.")
        print("\n")
        selection = input()
    for character in Characters:
        if character.name == selection:
            return character

def game_mode(prompt):
    print(BORDER)
    types = ["\n", "1) Hero Battle - choose two heroes in a fight to the death.", "2) Monster Rush - battle waves of enemies, level up, and claim victory for the realm."]
    mode_numbers = ["1", "2"] # Prompt - Which game mode would you like to play?
    print(prompt)
    for type in types:
        print(type)
    print("\n")
    selection = input()
    while selection not in [number for number in mode_numbers]:
        print(BORDER)
        print("That's not a mode. Please choose a number from the list above.")
        print("\n")
        selection = input()
    for mode in mode_numbers:
        if mode == selection:
            print(BORDER)
            return selection



