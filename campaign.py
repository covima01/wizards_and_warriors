import random
import time
import copy
from constants import BORDER
from classes import Wizard, Warrior
from characters import Gandalf, Cloud
from enemy_classes import Ogre
from enemies import Ogres



def one_enemy(player, enemy1):
    while player.health > 0 and enemy1.health > 0:
        time.sleep(0.5)
        print(f"{player.name}-- Health: {player.health} , {player.resource_type}: {player.resource} // {enemy1.name}-- Health: {max(enemy1.health, 0)}".center(70))
        print(f"What will {player.name} do?".center(70))
        for attack in player.attacks:
            print(attack)
        selection = input()
        while selection != "1" and selection != "2" and selection != "3":
            print("Unrecognized selection.")
            for attack in player.attacks:
                print(attack)
            selection = input()
        if selection == "1":
            attack = random.randint(0,8)
            if attack <= 7:
                player.attack1_method(enemy1)
                if enemy1.health > 0:
                    enemy1.counterattack(player)
            else:
                print(BORDER)
                print(f"{player.name} missed".center(70))
                player.resource -= 15
                print(BORDER)
                if enemy1.health > 0:
                    enemy1.counterattack(player)
        elif selection == "2":
            attack = random.randint(0,8)
            if attack <= 7:
                player.attack2_method(enemy1)
                if enemy1.health > 0:
                    enemy1.counterattack(player)
            else:
                print(BORDER)
                print(f"{player.name} missed".center(70))
                player.resource -= 30
                print(BORDER)
                if enemy1.health > 0:
                    enemy1.counterattack(player)
        elif selection == "3":
            player.heal1_method()
            if enemy1.health > 0:
                enemy1.counterattack(player)
    player.xp += enemy1.xp
    player.level_up()
    player.health = player.max_health
    player.resource = player.max_resource
def two_enemies(player, enemy1, enemy2):
    while player.health > 0 and enemy1.health > 0 or enemy2.health > 0:
        time.sleep(0.5)
        print(BORDER)
        print(f"{player.name}-- Health: {player.health} , {player.resource_type}: {player.resource} // {enemy1.name}-- Health: {max(enemy1.health, 0)} : {enemy2.name}-- Health: {max(enemy2.health, 0)}".center(70))
        target = input(f"Who will {player.name} attack?\n 1) {enemy1.name} \n 2) {enemy2.name}")
        print(BORDER)
        while target != "1" and target != "2":
            print(f"Unrecognized selection. Please choose 1) To attack the first enemy ({enemy1.name}) or 2) To attack the second enemy: ({enemy2.name})")
            target = input(f"Who will {player.name} attack first?\n 1) {enemy1.name} \n 2) {enemy2.name}")
        if target == "1":
            print(BORDER)
            if enemy1.health > 0:
                print(f"What will {player.name} do?")
                for attack in player.attacks:
                    print(attack)
                selection = input()
                while selection != "1" and selection != "2" and selection != "3":
                    print("Unrecognized selection.")
                    print(f"What will {player.name} do?")
                    for attack in player.attacks:
                        print(attack)
                    selection = input()
                if selection == "1":
                    attack = random.randint(0,8)
                    if attack <= 7:
                        player.attack1_method(enemy1)
                        if enemy1.health > 0:
                            enemy1.counterattack(player)
                            enemy2.counterattack(player)
                    else:
                        print(BORDER)
                        print(f"{player.name} missed".center(70))
                        player.resource -= 15
                        print(BORDER)
                        if enemy1.health > 0:
                            enemy1.counterattack(player)
                            enemy2.counterattack(player)
                elif selection == "2":
                    attack = random.randint(0,8)
                    if attack <= 7:
                        player.attack2_method(enemy1)
                        if enemy1.health > 0:
                            enemy1.counterattack(player)
                            enemy2.counterattack(player)
                    else:
                        print(BORDER)
                        print(f"{player.name} missed".center(70))
                        player.resource -= 30
                        print(BORDER)
                        if enemy1.health > 0:
                            enemy1.counterattack(player)
                            enemy2.counterattack(player)
                elif selection == "3":
                    player.heal1()
                    if enemy1.health > 0:
                        enemy1.counterattack(player)
                        enemy2.counterattack(player)
            else:
                print(f"{enemy1.name} has perished. Try attacking another enemy.")
        if target == "2":
            if enemy2.health > 0:
                print(f"What will {player.name} do?")
                for attack in player.attacks:
                    print(attack)
                selection = input()
                while selection != "1" and selection != "2" and selection != "3":
                    print("Unrecognized selection.")
                    print(f"What will {player.name} do?")
                    for attack in player.attacks:
                        print(attack)
                    selection = input()
                if selection == "1":
                    attack = random.randint(0,8)
                    if attack <= 7:
                        player.attack1_method(enemy2)
                        if enemy2.health > 0:
                            enemy2.counterattack(player)
                            enemy1.counterattack(player)
                    else:
                        print(BORDER)
                        print(f"{player.name} missed".center(70))
                        player.resource -= 15
                        print(BORDER)
                        if enemy2.health > 0:
                            enemy2.counterattack(player)
                            enemy1.counterattack(player)
                elif selection == "2":
                    attack = random.randint(0,8)
                    if attack <= 7:
                        player.attack2_method(enemy2)
                        if enemy2.health > 0:
                            enemy2.counterattack(player)
                            enemy1.counterattack(player)
                    else:
                        print(BORDER)
                        print(f"{player.name} missed".center(70))
                        player.resource -= 30
                        print(BORDER)
                        if enemy2.health > 0:
                            enemy2.counterattack(player)
                            enemy1.counterattack(player)
                elif selection == "3":
                    player.heal1()
                    if enemy2.health > 0:
                        enemy2.counterattack(player)
                        enemy1.counterattack(player)
            else:
                print(f"{enemy2.name} has perished. Try attacking another enemy.")
    player.xp += enemy1.xp
    player.level_up()
    player.health = player.max_health
    player.resource = player.max_resource
def three_enemies(player, enemy1, enemy2, enemy3):
    while player.health > 0 and enemy1.health > 0 or enemy2.health > 0 or enemy3.health > 0:
        time.sleep(0.5)
        print(BORDER)
        print(f"{player.name}-- Health: {player.health} , {player.resource_type}: {player.resource} // {enemy1.name}-- Health: {max(enemy1.health, 0)} : {enemy2.name}-- Health: {max(enemy2.health, 0)} : {enemy3.name}-- Health: {max(enemy3.health, 0)}".center(70))
        target = input(f"Who will {player.name} attack?\n 1) {enemy1.name} \n 2) {enemy2.name} \n 3) {enemy3.name}")
        while target != "1" and target != "2" and target != "3":
            print(f"Unrecognized selection. Please choose 1) To attack the first enemy ({enemy1.name}), 2) To attack the second enemy: ({enemy2.name}), or 3) To attack the third enemy: ({enemy3.name})")
            target = input(f"Who will {player.name} attack first?\n 1) {enemy1.name} \n 2) {enemy2.name} \n 3) {enemy3.name}")
        if target == "1":
            print(BORDER)
            if enemy1.health > 0:
                print(f"What will {player.name} do?")
                for attack in player.attacks:
                    print(attack)
                selection = input()
                while selection != "1" and selection != "2" and selection != "3":
                    print("Unrecognized selection.")
                    print(f"What will {player.name} do?")
                    for attack in player.attacks:
                        print(attack)
                    selection = input()
                if selection == "1":
                    attack = random.randint(0,8)
                    if attack <= 7:
                        player.attack1_method(enemy1)
                        if enemy1.health > 0:
                            enemy1.counterattack(player)
                            enemy2.counterattack(player)
                            enemy3.counterattack(player)
                    else:
                        print(BORDER)
                        print(f"{player.name} missed".center(70))
                        player.resource -= 15
                        print(BORDER)
                        if enemy1.health > 0:
                            enemy1.counterattack(player)
                            enemy2.counterattack(player)
                            enemy3.counterattack(player)
                elif selection == "2":
                    attack = random.randint(0,8)
                    if attack <= 7:
                        player.attack2_method(enemy1)
                        if enemy1.health > 0:
                            enemy1.counterattack(player)
                            enemy2.counterattack(player)
                            enemy3.counterattack(player)
                    else:
                        print(BORDER)
                        print(f"{player.name} missed".center(70))
                        player.resource -= 30
                        print(BORDER)
                        if enemy1.health > 0:
                            enemy1.counterattack(player)
                            enemy2.counterattack(player)
                            enemy3.counterattack(player)
                elif selection == "3":
                    player.heal1_method()
                    if enemy1.health > 0:
                        enemy1.counterattack(player)
                        enemy2.counterattack(player)
                        enemy3.counterattack(player)
            else:
                print(f"{enemy1.name} has perished. Try attacking another enemy.")
        if target == "2":
            if enemy2.health > 0:
                print(BORDER)
                print(f"What will {player.name} do?")
                for attack in player.attacks:
                    print(attack)
                selection = input()
                while selection != "1" and selection != "2" and selection != "3":
                    print("Unrecognized selection.")
                    print(f"What will {player.name} do?")
                    for attack in player.attacks:
                        print(attack)
                    selection = input()
                if selection == "1":
                    attack = random.randint(0,8)
                    if attack <= 7:
                        player.attack1_method(enemy2)
                        if enemy2.health > 0:
                            enemy2.counterattack(player)
                            enemy3.counterattack(player)
                            enemy1.counterattack(player)
                    else:
                        print(BORDER)
                        print(f"{player.name} missed".center(70))
                        player.resource -= 15
                        print(BORDER)
                        if enemy2.health > 0:
                            enemy2.counterattack(player)
                            enemy3.counterattack(player)
                            enemy1.counterattack(player)
                elif selection == "2":
                    attack = random.randint(0,8)
                    if attack <= 7:
                        player.attack2_method(enemy2)
                        if enemy2.health > 0:
                            enemy2.counterattack(player)
                            enemy3.counterattack(player)
                            enemy1.counterattack(player)
                    else:
                        print(BORDER)
                        print(f"{player.name} missed".center(70))
                        player.resource -= 30
                        print(BORDER)
                        if enemy2.health > 0:
                            enemy2.counterattack(player)
                            enemy3.counterattack(player)
                            enemy1.counterattack(player)
                elif selection == "3":
                    player.heal1_method()
                    if enemy2.health > 0:
                        enemy2.counterattack(player)
                        enemy3.counterattack(player)
                        enemy1.counterattack(player)
            else:
                print(f"{enemy2.name} has perished. Try attacking another enemy.")
        if target == "3":
            if enemy3.health > 0:
                print(BORDER)
                print(f"What will {player.name} do?")
                for attack in player.attacks:
                    print(attack)
                selection = input()
                while selection != "1" and selection != "2" and selection != "3":
                    print("Unrecognized selection.")
                    print(f"What will {player.name} do?")
                    for attack in player.attacks:
                        print(attack)
                    selection = input()
                if selection == "1":
                    attack = random.randint(0,8)
                    if attack <= 7:
                        player.attack1_method(enemy3)
                        if enemy3.health > 0:
                            enemy3.counterattack(player)
                            enemy1.counterattack(player)
                            enemy2.counterattack(player)
                    else:
                        print(BORDER)
                        print(f"{player.name} missed".center(70))
                        player.resource -= 15
                        print(BORDER)
                        if enemy3.health > 0:
                            enemy3.counterattack(player)
                            enemy1.counterattack(player)
                            enemy2.counterattack(player)
                elif selection == "2":
                    attack = random.randint(0,8)
                    if attack <= 7:
                        player.attack2_method(enemy3)
                        if enemy3.health > 0:
                            enemy3.counterattack(player)
                            enemy1.counterattack(player)
                            enemy2.counterattack(player)
                    else:
                        print(BORDER)
                        print(f"{player.name} missed".center(70))
                        player.resource -= 30
                        print(BORDER)
                        if enemy3.health > 0:
                            enemy3.counterattack(player)
                            enemy1.counterattack(player)
                            enemy2.counterattack(player)
                elif selection == "3":
                    player.heal1_method()
                    if enemy3.health > 0:
                        enemy3.counterattack(player)
                        enemy1.counterattack(player)
                        enemy2.counterattack(player)
            else:
                print(f"{enemy3.name} has perished. Try attacking another enemy.")
    player.xp += enemy1.xp
    player.level_up()
    player.health = player.max_health
    player.resource = player.max_resource
def campaign():
    from inputs import character_selection
    character = character_selection("Choose your character-\n")
    while character.health > 0:
        Ogre_Generator = [Ogre.create_ogre_grunt, Ogre.create_ogre_general, Ogre.create_ogre_warlord]
        enemy_wave = [one_enemy, two_enemies, three_enemies]
        enemy_wave_selection = random.choice(enemy_wave)
        if enemy_wave_selection == one_enemy:
            enemy1 = random.choice(Ogre_Generator)()
            one_enemy(character, enemy1)
        elif enemy_wave_selection == two_enemies:
            enemy1 = random.choice(Ogre_Generator)()
            enemy2 = random.choice(Ogre_Generator)()
            two_enemies(character, enemy1, enemy2)
        elif enemy_wave_selection == three_enemies:
            enemy1 = random.choice(Ogre_Generator)()
            enemy2 = random.choice(Ogre_Generator)()
            enemy3 = random.choice(Ogre_Generator)()
            three_enemies(character, enemy1, enemy2, enemy3)
    print(f"\n{character.name} has fallen")


if __name__ == "__main__":
    campaign()


