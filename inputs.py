from classes import border, Wizard, Warrior
from characters import Characters, Gandalf


def character_selection(prompt):
    print(prompt)
    for character in Characters:
        print(character.name)
    selection = input("\nEnter character name: ")
    while selection not in [character.name for character in Characters]:
        print("That's not a character. Please choose from the list above.")
        print("\n")
        selection = input()
    for character in Characters:
        if character.name == selection:
            print(border)
            return character

def game_mode(prompt): # Prompt - Which game mode would you like to play?
    print(prompt)



