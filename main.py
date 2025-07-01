import random
from classes import *
from constants import BORDER
from characters import *
from inputs import character_selection, game_mode


def main():
    from campaign import campaign
    game_type = game_mode("Which mode do you want to play?")
    if game_type == "Combat":
        print("You've selected Hero Battle.")
        character = character_selection("Choose your character-\n")
        opponent = character_selection("Choose your opponent-\n")
        print(f"{character.name} vs {opponent.name}")
        print(BORDER)
        from combat import combat
        combat(character, opponent)
    elif game_type == "Campaign":
        print("You've selected Campaign")
        campaign()



if __name__ == "__main__":
    main()