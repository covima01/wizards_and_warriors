import random
from classes import *
from constants import BORDER
from characters import *
from inputs import character_selection


def main():
    character = character_selection("Choose your character-\n")
    opponent = character_selection("Choose your opponent-\n")
    print(f"{character.name} vs {opponent.name}")
    print(BORDER)
    from combat import combat
    combat(character, opponent)


if __name__ == "__main__":
    main()