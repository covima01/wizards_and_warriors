import time
import random
from constants import BORDER
from monster_rush import one_enemy, two_enemies, three_enemies
from enemies import *
from bossfight import boss_fight
from story import *
from characters import Knight_Disgraced, Scholar_Expelled


def level_1(character):
    for i in range(0, 3)
        Monster_Generator = Desolate_Place_Enemies
        enemy1 = random.choice(Monster_Generator)()
        one_enemy(character, enemy1)
        print("...".center(100))
        i+=1
def level_2(character):
    for i in range(0, 2)
        Monster_Generator = Abandoned_Sanctuary_Enemies
        enemy1 = random.choice(Monster_Generator)()
        enemy2 = random.choice(Monster_Generator)()
        two_enemies(character, enemy1, enemy2)
        print("...".center(100))
        i+=1
def level_3(character):
    for i in range(0, 2)
        Monster_Generator = Southern_Desert_Enemies
        enemy1 = random.choice(Monster_Generator)()
        enemy2 = random.choice(Monster_Generator)()
        enemy3 = random.choice(Monster_Generator)()
        three_enemies(character, enemy1, enemy2, enemy3)
        print("...".center(100))
        time.sleep(3)
        i+=1
def level_4(character):
    for i in range(0,2):
        Monster_Generator = Longways_Aqueduct_Enemies
        enemy1 = random.choice(Monster_Generator)()
        enemy2 = random.choice(Monster_Generator)()
        enemy3 = random.choice(Monster_Generator)()
        three_enemies(character, enemy1, enemy2, enemy3)
        i+=1
    print("...".center(100))
def level_5(character):
    for i in range(0,2):
        Monster_Generator = Lostnorth_Forest_Enemies
        enemy1 = random.choice(Monster_Generator)()
        one_enemy(character, enemy1)
        i+=1
    Monster_Generator = Lostnorth_Forest_Enemies
    enemy1 = random.choice(Monster_Generator)()
    enemy2 = random.choice(Monster_Generator)()
    enemy3 = random.choice(Monster_Generator)()
    three_enemies(character, enemy1, enemy2, enemy3)
    for i in range(0,2):
        Monster_Generator = Lostnorth_Forest_Enemies
        enemy1 = random.choice(Monster_Generator)()
        enemy2 = random.choice(Monster_Generator)()
        two_enemies(character, enemy1, enemy2)
        i+=1
    print("...".center(100))
def level_6(character):
    for i in range(0,3):
        Monster_Generator = Alenia_Farmland_Enemies
        enemy1 = random.choice(Monster_Generator)()
        one_enemy(character, enemy1)
        i+=1
    Monster_Generator = Alenia_Farmland_Enemies
    enemy1 = random.choice(Monster_Generator)()
    enemy2 = random.choice(Monster_Generator)()
    enemy3 = random.choice(Monster_Generator)()
    three_enemies(character, enemy1, enemy2, enemy3)
    for i in range(0,2):
        Monster_Generator = Alenia_Farmland_Enemies
        enemy1 = random.choice(Monster_Generator)()
        enemy2 = random.choice(Monster_Generator)()
        two_enemies(character, enemy1, enemy2)
        i+=1
    print("...".center(100))
def level_7(character):
    for i in range(0,3):
        Monster_Generator = Mountain_Pass_Enemies
        enemy1 = random.choice(Monster_Generator)()
        one_enemy(character, enemy1)
        i+=1
    Monster_Generator = Mountain_Pass_Enemies
    enemy1 = random.choice(Monster_Generator)()
    enemy2 = random.choice(Monster_Generator)()
    enemy3 = random.choice(Monster_Generator)()
    three_enemies(character, enemy1, enemy2, enemy3)
    for i in range(0,3):
        Monster_Generator = Mountain_Pass_Enemies
        enemy1 = random.choice(Monster_Generator)()
        enemy2 = random.choice(Monster_Generator)()
        two_enemies(character, enemy1, enemy2)
        i+=1
    print("...".center(100))
def level_8(character):
    for i in range(0,2):
        Monster_Generator = Mountain_Ascent_Enemies
        enemy1 = random.choice(Monster_Generator)()
        enemy2 = random.choice(Monster_Generator)()
        two_enemies(character, enemy1, enemy2)
        i+=1
    for i in range(0, 2):
        Monster_Generator = Mountain_Ascent_Enemies
        enemy1 = random.choice(Monster_Generator)()
        enemy2 = random.choice(Monster_Generator)()
        enemy3 = random.choice(Monster_Generator)()
        three_enemies(character, enemy1, enemy2, enemy3)
        i+=1
    for i in range(0,2):
        Monster_Generator = Mountain_Ascent_Enemies
        enemy1 = random.choice(Monster_Generator)()
        enemy2 = random.choice(Monster_Generator)()
        two_enemies(character, enemy1, enemy2)
        i+=1
    print("The top is near.".center(100))
    time.sleep(6)
def level_9(character):
    time.sleep(3)
    for i in range(0,2):
        Monster_Generator = Mountain_Cliffs_Enemies
        enemy1 = random.choice(Monster_Generator)()
        enemy2 = random.choice(Monster_Generator)()
        two_enemies(character, enemy1, enemy2)
        i+=1
    for i in range(0, 2):
        Monster_Generator = Mountain_Cliffs_Enemies
        enemy1 = random.choice(Monster_Generator)()
        enemy2 = random.choice(Monster_Generator)()
        enemy3 = random.choice(Monster_Generator)()
        three_enemies(character, enemy1, enemy2, enemy3)
        i+=1
    for i in range(0,2):
        Monster_Generator = Mountain_Cliffs_Enemies
        enemy1 = random.choice(Monster_Generator)()
        enemy2 = random.choice(Monster_Generator)()
        two_enemies(character, enemy1, enemy2)
        i+=1
    print("Nearer still...".center(100))
    time.sleep(5)
def level_10(character):
    print(BORDER)
    if character.name == "Disgraced Knight":
        print("You've made it knight.".center(100))
        time.sleep(5)
    else:
        print("You've made it scholar.".center(100))
        time.sleep(5)
    for i in range(0,2):
        Monster_Generator = Mountain_Peak_Enemies
        enemy1 = random.choice(Monster_Generator)()
        enemy2 = random.choice(Monster_Generator)()
        two_enemies(character, enemy1, enemy2)
        i+=1
    for i in range(0, 2):
        Monster_Generator = Mountain_Peak_Enemies
        enemy1 = random.choice(Monster_Generator)()
        enemy2 = random.choice(Monster_Generator)()
        enemy3 = random.choice(Monster_Generator)()
        three_enemies(character, enemy1, enemy2, enemy3)
        i+=1
    for i in range(0,2):
        Monster_Generator = Mountain_Peak_Enemies
        enemy1 = random.choice(Monster_Generator)()
        enemy2 = random.choice(Monster_Generator)()
        two_enemies(character, enemy1, enemy2)
        i+=1
    print("good luck".center(100))


def new_pilgrimage():
    from combat import combat
    from inputs import character_selection
    from story import disgraced_knight_intro, expelled_scholar_intro
    character = character_selection("Choose your character-\n")
    if character.name == "Disgraced Knight":
        disgraced_knight_intro()
    elif character.name == "Expelled Scholar":
        expelled_scholar_intro()
    while character.health > 0:
        desolate_place_intro()
        level_1(character)
        abandoned_sanctuary_intro()
        level_2(character)
        southern_desert_intro()
        level_3(character)
        fetid_brute_intro()
        boss_fight(character, Fetid_Brute)
        fetid_brute_outro()
        longways_aqueduct_intro()
        level_4(character)
        lostnorth_forest_intro()
        level_5(character)
        scalewing_alpha_intro()
        boss_fight(character, Scalewing_Alpha)
        scalewing_alpha_outro()
        alenia_farmland_intro()
        level_6(character)
        mountain_pass_intro()
        level_7(character)
        mountain_ascent_intro
        level_8(character)
        the_myth_intro()
        boss_fight(character, The_Myth)
        the_myth_outro()
        mountain_cliffs_intro()
        level_9(character)
        level_10(character)
        unknown_intro()
        boss_fight(character, Unknown)
        unknown_outro
        if character.name == "Disgraced Knight":
            combat(character, Knight_Disgraced)
        else:
            combat(character, Scholar_Expelled) 

if __name__ == "__main__":
        new_pilgrimage()