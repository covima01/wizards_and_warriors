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

