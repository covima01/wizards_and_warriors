print("DEBUG: pilgrimage.py loaded")
import random
from constants import BORDER
from monster_rush import one_enemy, two_enemies, three_enemies
from enemies import Enemy_Creation, Monstrous_Cyclops, Verdant_Dragon, Ancient_Chimera
from bossfight import boss_fight
from story import disgraced_knight_intro, expelled_scholar_intro


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
def level_6(character):
    print(BORDER)
    print("Now entering the Swamp of Skulls...")
    print(BORDER)
    for i in range(0,3):
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
def level_7(character):
    for i in range(0,3):
        Monster_Generator = Enemy_Creation
        enemy1 = random.choice(Monster_Generator)()
        one_enemy(character, enemy1)
        i+=1
    Monster_Generator = Enemy_Creation
    enemy1 = random.choice(Monster_Generator)()
    enemy2 = random.choice(Monster_Generator)()
    enemy3 = random.choice(Monster_Generator)()
    three_enemies(character, enemy1, enemy2, enemy3)
    for i in range(0,3):
        Monster_Generator = Enemy_Creation
        enemy1 = random.choice(Monster_Generator)()
        enemy2 = random.choice(Monster_Generator)()
        two_enemies(character, enemy1, enemy2)
        i+=1
def level_8(character):
    for i in range(0,2):
        Monster_Generator = Enemy_Creation
        enemy1 = random.choice(Monster_Generator)()
        enemy2 = random.choice(Monster_Generator)()
        two_enemies(character, enemy1)
        i+=1
    for i in range(0, 2):
        Monster_Generator = Enemy_Creation
        enemy1 = random.choice(Monster_Generator)()
        enemy2 = random.choice(Monster_Generator)()
        enemy3 = random.choice(Monster_Generator)()
        three_enemies(character, enemy1, enemy2, enemy3)
        i+=1
    for i in range(0,2):
        Monster_Generator = Enemy_Creation
        enemy1 = random.choice(Monster_Generator)()
        enemy2 = random.choice(Monster_Generator)()
        two_enemies(character, enemy1, enemy2)
        i+=1




def pilgrimage():
    print("Pilgrimage called")
    from inputs import character_selection
    from story import disgraced_knight_intro, expelled_scholar_intro
    character = character_selection("Choose your character-\n")
    print(f"DEBUG: You selected {character.name!r}")
    if character.name == "Disgraced Knight":
        disgraced_knight_intro()
    elif character.name == "Expelled Scholar":
        expelled_scholar_intro()
    else:
        print("DEBUG: Unknown character selected!")
    while character.health > 0:
        level_1(character)
        level_2(character)
        level_3(character)
        boss_fight(character, Monstrous_Cyclops)
        level_4(character)
        level_5(character)
        boss_fight(character, Verdant_Dragon)
        level_6(character)
        level_7(character)
        level_8(character)
        boss_fight(character, Ancient_Chimera)

if __name__ == "__main__":
    pilgrimage()
