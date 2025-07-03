from classes import *
from constants import BORDER
from characters import *
from inputs import character_selection, game_mode


def main():
    from monster_rush import monster_rush
    game_type = game_mode("Which mode do you want to play?(Enter a number)")
    if game_type == "1":
        print("You've selected Hero Battle.")
        character = character_selection("Choose your character-\n")
        opponent = character_selection("Choose your opponent-\n")
        print(f"{character.name} vs {opponent.name}")
        print(BORDER)
        from combat import combat
        combat(character, opponent)
    elif game_type == "2":
        print("You've selected Monster Rush")
        monster_rush()
    elif game_type == "3":
        from adventure import adventure
        print("You've selection Adventure.")
        adventure()



if __name__ == "__main__":
    main()