import time
import random
from constants import BORDER
from monster_rush import one_enemy, two_enemies, three_enemies
from enemies import Enemy_Creation, Fetid_Brute, Scalewing_Alpha, The_Myth
from bossfight import boss_fight
from story import fetid_brute_intro, fetid_brute_outro, scalewing_alpha_intro, scalewing_alpha_outro, the_myth_intro


def level_1(character):
    print(BORDER)
    print("Now entering a desolate place...".center(70))
    print(BORDER)
    Monster_Generator = Enemy_Creation
    enemy1 = random.choice(Monster_Generator)()
    one_enemy(character, enemy1)
    print("Desolate place has been cleared.".center(70))
def level_2(character):
    print(BORDER)
    print("Now entering an abandoned sanctuary...".center(70))
    Monster_Generator = Enemy_Creation
    enemy1 = random.choice(Monster_Generator)()
    enemy2 = random.choice(Monster_Generator)()
    two_enemies(character, enemy1, enemy2)
    print("Abandoned sanctuary has been cleared.".center(70))
def level_3(character):
    print(BORDER)
    print("Now entering the southern desert...".center(70))
    Monster_Generator = Enemy_Creation
    enemy1 = random.choice(Monster_Generator)()
    enemy2 = random.choice(Monster_Generator)()
    enemy3 = random.choice(Monster_Generator)()
    three_enemies(character, enemy1, enemy2, enemy3)
    print("Southern desert has been cleared.".center(70))
    time.sleep(3)
    fetid_brute_intro()
def level_4(character):
    print(BORDER)
    print("Now entering the longways aqueduct...".center(70))
    for i in range(0,2):
        Monster_Generator = Enemy_Creation
        enemy1 = random.choice(Monster_Generator)()
        enemy2 = random.choice(Monster_Generator)()
        enemy3 = random.choice(Monster_Generator)()
        three_enemies(character, enemy1, enemy2, enemy3)
        i+=1
    print("Longways aqueduct has been cleared.".center(70))
def level_5(character):
    print(BORDER)
    print("Now entering Lostnorth Forest...".center(70))
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
    print("Lostnorth Forest has been cleared.".center(70))
    scalewing_alpha_intro()
def level_6(character):
    print(BORDER)
    print("Now entering the Alenia farmland...".center(70))
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
    print("Alenia farmland has been cleared.".center(70))
def level_7(character):
    print(BORDER)
    print("Now entering eeries a mountain pass...".center(70))
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
    print("Eeries mountain pass cleared.".center(70))
def level_8(character):
    print(BORDER)
    print("Ascending this mountain...".center(70))
    for i in range(0,2):
        Monster_Generator = Enemy_Creation
        enemy1 = random.choice(Monster_Generator)()
        enemy2 = random.choice(Monster_Generator)()
        two_enemies(character, enemy1, enemy2)
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
    print("Mountain traversed.".center(70))
    the_myth_intro()


def new_pilgrimage():
    from inputs import character_selection
    from story import disgraced_knight_intro, expelled_scholar_intro
    character = character_selection("Choose your character-\n")
    if character.name == "Disgraced Knight":
        disgraced_knight_intro()
    elif character.name == "Expelled Scholar":
        expelled_scholar_intro()
    while character.health > 0:
        level_1(character)
        level_2(character)
        level_3(character)
        fetid_brute_intro()
        boss_fight(character, Fetid_Brute)
        fetid_brute_outro()
        level_4(character)
        level_5(character)
        scalewing_alpha_intro()
        boss_fight(character, Scalewing_Alpha)
        scalewing_alpha_outro()
        level_6(character)
        level_7(character)
        level_8(character)
        boss_fight(character, The_Myth)

if __name__ == "__main__":
    new_pilgrimage()