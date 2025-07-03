import random
from constants import BORDER
from monster_rush import one_enemy, two_enemies, three_enemies
from enemies import Enemy_Creation, Monstrous_Cyclops, Verdant_Dragon
from bossfight import boss_fight
from characters import Debius


def level_1(character):
    print(BORDER)
    print("Now entering the Ravaged Wastes...".center(70))
    print(BORDER)
    Monster_Generator = Enemy_Creation
    enemy1 = random.choice(Monster_Generator)()
    one_enemy(character, enemy1)
    print("Ravaged Wastes have been cleared.".center(70))
def level_2(character):
    print(BORDER)
    print("Now entering Goblin Hideout...".center(70))
    print(BORDER)
    Monster_Generator = Enemy_Creation
    enemy1 = random.choice(Monster_Generator)()
    enemy2 = random.choice(Monster_Generator)()
    two_enemies(character, enemy1, enemy2)
    print("Goblin Hideout has been cleared.".center(70))
def level_3(character):
    print(BORDER)
    print("Now entering the Parth Desert...".center(70))
    print(BORDER)
    Monster_Generator = Enemy_Creation
    enemy1 = random.choice(Monster_Generator)()
    enemy2 = random.choice(Monster_Generator)()
    enemy3 = random.choice(Monster_Generator)()
    three_enemies(character, enemy1, enemy2, enemy3)
    print("Parth Desert has been cleared.".center(70))
def level_4(character):
    print(BORDER)
    print("Now entering the Fairgold Mines...".center(70))
    print(BORDER)
    for i in range(0,2):
        Monster_Generator = Enemy_Creation
        enemy1 = random.choice(Monster_Generator)()
        enemy2 = random.choice(Monster_Generator)()
        enemy3 = random.choice(Monster_Generator)()
        three_enemies(character, enemy1, enemy2, enemy3)
        i+=1
    print("Fairgold mines have been cleared.")
def level_5(character):
    print(BORDER)
    print("Now entering Lostnorth Forest...")
    print(BORDER)
    for i in range(0,2):
        Monster_Generator = Enemy_Creation
        enemy1 = random.choice(Monster_Generator)()
        one_enemy(character, enemy1)
        i+=1
    Monster_Generator = Enemy_Creation
    enemy1 = random.choice(Monster_Generator)()
    enemy2 = random.choice(Monster_Generator)()
    enemy3 = random.choice(Monster_Generator)()
    three_enemies(character, enemy1, enemy2, enemy3)
    for i in range(0,2):
        Monster_Generator = Enemy_Creation
        enemy1 = random.choice(Monster_Generator)()
        enemy2 = random.choice(Monster_Generator)()
        two_enemies(character, enemy1, enemy2)
        i+=1



def adventure():
    from inputs import character_selection
    character = character_selection("Choose your character-\n")
    print(BORDER)
    while character.health > 0:
        level_1(character)
        level_2(character)
        level_3(character)
        boss_fight(character, Monstrous_Cyclops)
        level_4(character)
        level_5(character)
        boss_fight(character, Verdant_Dragon)

if __name__ == "__main__":
    adventure()