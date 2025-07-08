import random
import time
from classes import BORDER

def combat(player, enemy):
    while enemy.health > 0 and player.health > 0:
        time.sleep(0.5)
        print(f"{player.name}-- Health: {player.health} , {player.resource_type}: {player.resource} // {enemy.name}-- Health: {enemy.health} , {enemy.resource_type}: {enemy.resource}".center(100))
        print(f"What will {player.name} do?".center(100))
        selection = input(f"\n1) {player.attack1} - {player.attack1_description}.\n2) {player.attack2} - {player.attack2_description}.\n3) {player.heal1} - {player.heal1_description}\n")
        while selection != "1" and selection != "2" and selection != "3":
            print(f"Unrecognized selection. Please choose 1 to use {player.attack1}, 2 to use {player.attack2}, or 3 to use {player.heal1}\n")
            selection = input(f"Which action will {player.name} take?  {player.name} has {player.health} health.\n {enemy.name} has {enemy.health} health.\n\n 1) {player.attack1}\n 2) {player.attack2}\n 3) {player.heal1}")
        if selection == "1":
            attack = random.randint(0,10)
            if attack <= 9:
                player.attack1_method(enemy)
                if enemy.health > 0:
                    enemy.counterattack(player)
            else:
                print(BORDER)
                print(f"{player.name} missed".center(100))
                print(BORDER)
                if enemy.health > 0:
                    enemy.counterattack(player)
        elif selection == "2":
            attack = random.randint(0,10)
            if attack <= 9:
                player.attack2_method(enemy)
                if enemy.health > 0:
                    enemy.counterattack(player)   
            else:
                print(BORDER)
                print(f"{player.name} missed".center(100))
                print(BORDER)
                if enemy.health > 0:
                    enemy.counterattack(player)
        elif selection == "3":
            player.heal1_method()
            if enemy.health > 0:
                enemy.counterattack_method(player)
    else:
        return

