from constants import BORDER

def character_selection(prompt):
    from characters import Characters
    print(BORDER)
    print(prompt)
    for character in Characters:
        print(character.description)
    selection = input("\nEnter character name: ").strip().lower()
    print(BORDER)
    while selection not in [character.name.lower() for character in Characters]:
        print(BORDER)
        print("That's not a character. Please choose from the list above.")
        print("\n")
        selection = input().strip().lower()
    for character in Characters:
        if character.name.lower() == selection:
            return character

def game_mode(prompt):
    print(BORDER)
    types = ["\n", "1) Hero Battle - choose two heroes in a fight to the death.", "2) Monster Rush - battle waves of enemies, level up, and claim victory for the realm.", "3) Pilgrimage - combat your way through the lands to reach your destination."]
    mode_numbers = ["1", "2", "3"] # Prompt - Which game mode would you like to play?
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
