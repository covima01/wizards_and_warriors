import random
from constants import BORDER
from monster_rush import one_enemy, two_enemies, three_enemies
from enemies import Enemy_Creation


def level_1(character):
    print(BORDER)
    print("Now entering the Ravaged Wastes...")
    Monster_Generator = Enemy_Creation
    enemy1 = random.choice(Monster_Generator)()
    one_enemy(character, enemy1)
    print("Ravaged Wastes have been cleared.")
def level_2(character):
    print(BORDER)
    print("Now entering Gobline Hideout")
    Monster_Generator = Enemy_Creation
    enemy1 = random.choice(Monster_Generator)()
    enemy2 = random.choice(Monster_Generator)()
    two_enemies(character, enemy1, enemy2)
    print("Goblin Hideout has been cleared.")














def adventure():
    from inputs import character_selection
    character = character_selection("Choose your character-\n")
    print(BORDER)
    while character.health > 0:
        level_1(character)
        level_2(character)

if __name__ == "__main__":
    adventure()