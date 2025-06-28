from classes import border, Wizard, Warrior
from characters import Characters, Gandalf


def character_selection(prompt):
    from combat import combat
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

character = character_selection("Choose your character-\n")
opponent = character_selection("Choose your opponent-\n")
print(f"{character.name} vs {opponent.name}")
from combat import combat
combat(character, opponent)




