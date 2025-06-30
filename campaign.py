import random
import time
from constants import BORDER
from classes import Wizard, Warrior
from characters import Gandalf, Cloud
from enemy_classes import Ogre
from enemies import Ogre_Grunt, Ogre_General, Ogre_Warlord


def one_enemy(player, enemy1):
    enemies = [Ogre_Grunt, Ogre_General, Ogre_Warlord]
    enemy1 = random.choice(enemies)
    if isinstance (player, Warrior) and isinstance (enemy1, Ogre):
        while player.health > 0 and enemy1.health > 0:
            time.sleep(0.5)
            print(f"{player.name}-- Health: {player.health} , Endurance: {player.endurance} // {enemy1.name}-- Health: {max(enemy1.health, 0)}".center(70))
            print(f"What will {player.name} do?".center(70))
            selection = input(f"\n1) Light Swing - deals moderate physical damage.\n2) Heavy Swing - deals heavy physical damage.\n3) Meditate - moderately restores your health.")
            while selection != "1" and selection != "2" and selection != "3":
                print("Unrecognized selection. Please choose 1) Light Swing or 2) Heavy Swing 3) Meditate")
                selection = input(f"Which action will {player.name} take?  {player.name} has {player.health} health. {enemy1.name} has {max(enemy1.health, 0)} health.\n\n 1) Light Swing\n 2) Heavy Swing\n 3) Meditate")
            if selection == "1":
                attack = random.randint(0,8)
                if attack <= 7:
                    player.light_swing(enemy1)
                    if enemy1.health > 0:
                        enemy1.ogre_counterattack(player)
                else:
                    print(BORDER)
                    print(f"{player.name} missed".center(70))
                    player.endurance -= 15
                    print(BORDER)
                    if enemy1.health > 0:
                        enemy1.ogre_counterattack(player)
            elif selection == "2":
                attack = random.randint(0,8)
                if attack <= 7:
                    player.heavy_swing(enemy1)
                    if enemy1.health > 0:
                        enemy1.ogre_counterattack(player)
                else:
                    print(BORDER)
                    print(f"{player.name} missed".center(70))
                    player.endurance -= 30
                    print(BORDER)
                    if enemy1.health > 0:
                        enemy1.ogre_counterattack(player)
            elif selection == "3":
                player.meditate()
                if enemy1.health > 0:
                    enemy1.ogre_counterattack(player)

def two_enemies(player, enemy1, enemy2):
    enemies = [Ogre_Grunt, Ogre_General, Ogre_Warlord]
    enemy1 = random.choice(enemies)
    enemy2 = random.choice(enemies)
    if isinstance (player, Warrior) and isinstance (enemy1, Ogre) and isinstance (enemy2, Ogre):
        player.endurance = int(player.endurance * 1.5)
        while player.health > 0 and enemy1.health > 0 or enemy2.health > 0:
            time.sleep(0.5)
            print(BORDER)
            print(f"{player.name}-- Health: {player.health} , Endurance: {player.endurance} // {enemy1.name}-- Health: {max(enemy1.health, 0)} : {enemy2.name}-- {max(enemy2.health, 0)}".center(70))
            target = input(f"Who will {player.name} attack?\n 1) {enemy1.name} \n 2) {enemy2.name}")
            print(BORDER)
            while target != "1" and target != "2":
                print(f"Unrecognized selection. Please choose 1) To attack the first enemy ({enemy1.name}) or 2) To attack the second enemy: ({enemy2.name})")
                target = input(f"Who will {player.name} attack first?\n 1) {enemy1.name} \n 2) {enemy2.name}")
            if target == "1":
                print(BORDER)
                if enemy1.health > 0:
                    selection = input(f"How will you attack?\n1) Light Swing - deals moderate physical damage.\n2) Heavy Swing - deals heavy physical damage.\n3) Meditate - moderately restores your health.")
                    while selection != "1" and selection != "2" and selection != "3":
                        print("Unrecognized selection. Please choose 1) Light Swing or 2) Heavy Swing 3) Meditate")
                        selection = input(f"Which action will {player.name} take?  {player.name} has {player.health} health. {enemy1.name} has {max(enemy1.health, 0)} health.\n\n 1) Light Swing\n 2) Heavy Swing\n 3) Meditate")
                    if selection == "1":
                        attack = random.randint(0,8)
                        if attack <= 7:
                            player.light_swing(enemy1)
                            if enemy1.health > 0:
                                enemy1.ogre_counterattack(player)
                                enemy2.ogre_counterattack(player)
                        else:
                            print(BORDER)
                            print(f"{player.name} missed".center(70))
                            player.endurance -= 15
                            print(BORDER)
                            if enemy1.health > 0:
                                enemy1.ogre_counterattack(player)
                                enemy2.ogre_counterattack(player)
                    elif selection == "2":
                        attack = random.randint(0,8)
                        if attack <= 7:
                            player.heavy_swing(enemy1)
                            if enemy1.health > 0:
                                enemy1.ogre_counterattack(player)
                                enemy2.ogre_counterattack(player)
                        else:
                            print(BORDER)
                            print(f"{player.name} missed".center(70))
                            player.endurance -= 30
                            print(BORDER)
                            if enemy1.health > 0:
                                enemy1.ogre_counterattack(player)
                                enemy2.ogre_counterattack(player)
                    elif selection == "3":
                        player.meditate()
                        if enemy1.health > 0:
                            enemy1.ogre_counterattack(player)
                            enemy2.ogre_counterattack(player)
                else:
                    print(f"{enemy1.name} has perished. Try attacking another enemy.")
            if target == "2":
                if enemy2.health > 0:
                    print(BORDER)
                    selection = input(f"How will you attack?\n1) Light Swing - deals moderate physical damage.\n2) Heavy Swing - deals heavy physical damage.\n3) Meditate - moderately restores your health.")
                    while selection != "1" and selection != "2" and selection != "3":
                        print("Unrecognized selection. Please choose 1) Light Swing or 2) Heavy Swing 3) Meditate")
                        selection = input(f"Which action will {player.name} take?  {player.name} has {player.health} health. {enemy2.name} has {max(enemy2.health, 0)} health.\n\n 1) Light Swing\n 2) Heavy Swing\n 3) Meditate")
                    if selection == "1":
                        attack = random.randint(0,8)
                        if attack <= 7:
                            player.light_swing(enemy2)
                            if enemy2.health > 0:
                                enemy2.ogre_counterattack(player)
                                enemy1.ogre_counterattack(player)
                        else:
                            print(BORDER)
                            print(f"{player.name} missed".center(70))
                            player.endurance -= 15
                            print(BORDER)
                            if enemy2.health > 0:
                                enemy2.ogre_counterattack(player)
                                enemy1.ogre_counterattack(player)
                    elif selection == "2":
                        attack = random.randint(0,8)
                        if attack <= 7:
                            player.heavy_swing(enemy2)
                            if enemy2.health > 0:
                                enemy2.ogre_counterattack(player)
                                enemy1.ogre_counterattack(player)
                        else:
                            print(BORDER)
                            print(f"{player.name} missed".center(70))
                            player.endurance -= 30
                            print(BORDER)
                            if enemy2.health > 0:
                                enemy2.ogre_counterattack(player)
                                enemy1.ogre_counterattack(player)
                    elif selection == "3":
                        player.meditate()
                        if enemy2.health > 0:
                            enemy2.ogre_counterattack(player)
                            enemy1.ogre_counterattack(player)
                else:
                    print(f"{enemy2.name} has perished. Try attacking another enemy.")

def three_enemies(player, enemy1, enemy2, enemy3):
    enemies = [Ogre_Grunt, Ogre_General, Ogre_Warlord]
    enemy1 = random.choice(enemies)
    enemy2 = random.choice(enemies)
    enemy3 = random.choice(enemies)
    if isinstance (player, Warrior) and isinstance (enemy1, Ogre) and isinstance (enemy2, Ogre) and isinstance(enemy3, Ogre):
        player.endurance = int(player.endurance * 2)
        while player.health > 0 and enemy1.health > 0 or enemy2.health > 0 or enemy3.health > 0:
            time.sleep(0.5)
            print(BORDER)
            print(f"{player.name}-- Health: {player.health} , Endurance: {player.endurance} // {enemy1.name}-- Health: {max(enemy1.health, 0)} : {enemy2.name}-- Health: {max(enemy2.health, 0)} : {enemy3.name}-- Health: {max(enemy3.health, 0)}".center(70))
            target = input(f"Who will {player.name} attack?\n 1) {enemy1.name} \n 2) {enemy2.name} \n 3) {enemy3.name}")
            while target != "1" and target != "2" and target != "3":
                print(f"Unrecognized selection. Please choose 1) To attack the first enemy ({enemy1.name}), 2) To attack the second enemy: ({enemy2.name}), or 3) To attack the third enemy: ({enemy3.name})")
                target = input(f"Who will {player.name} attack first?\n 1) {enemy1.name} \n 2) {enemy2.name} \n 3) {enemy3.name}")
            if target == "1":
                print(BORDER)
                if enemy1.health > 0:
                    selection = input(f"How will you attack?\n1) Light Swing - deals moderate physical damage.\n2) Heavy Swing - deals heavy physical damage.\n3) Meditate - moderately restores your health.")
                    while selection != "1" and selection != "2" and selection != "3":
                        print("Unrecognized selection. Please choose 1) Light Swing or 2) Heavy Swing 3) Meditate")
                        selection = input(f"Which action will {player.name} take?  {player.name} has {player.health} health. {enemy1.name} has {max(enemy1.health, 0)} health.\n\n 1) Light Swing\n 2) Heavy Swing\n 3) Meditate")
                    if selection == "1":
                        attack = random.randint(0,8)
                        if attack <= 7:
                            player.light_swing(enemy1)
                            if enemy1.health > 0:
                                enemy1.ogre_counterattack(player)
                                enemy2.ogre_counterattack(player)
                                enemy3.ogre_counterattack(player)
                        else:
                            print(BORDER)
                            print(f"{player.name} missed".center(70))
                            player.endurance -= 15
                            print(BORDER)
                            if enemy1.health > 0:
                                enemy1.ogre_counterattack(player)
                                enemy2.ogre_counterattack(player)
                                enemy3.ogre_counterattack(player)
                    elif selection == "2":
                        attack = random.randint(0,8)
                        if attack <= 7:
                            player.heavy_swing(enemy1)
                            if enemy1.health > 0:
                                enemy1.ogre_counterattack(player)
                                enemy2.ogre_counterattack(player)
                                enemy3.ogre_counterattack(player)
                        else:
                            print(BORDER)
                            print(f"{player.name} missed".center(70))
                            player.endurance -= 30
                            print(BORDER)
                            if enemy1.health > 0:
                                enemy1.ogre_counterattack(player)
                                enemy2.ogre_counterattack(player)
                                enemy3.ogre_counterattack(player)
                    elif selection == "3":
                        player.meditate()
                        if enemy1.health > 0:
                            enemy1.ogre_counterattack(player)
                            enemy2.ogre_counterattack(player)
                            enemy3.ogre_counterattack(player)
                else:
                    print(f"{enemy1.name} has perished. Try attacking another enemy.")
            if target == "2":
                if enemy2.health > 0:
                    print(BORDER)
                    selection = input(f"How will you attack?\n1) Light Swing - deals moderate physical damage.\n2) Heavy Swing - deals heavy physical damage.\n3) Meditate - moderately restores your health.")
                    while selection != "1" and selection != "2" and selection != "3":
                        print("Unrecognized selection. Please choose 1) Light Swing or 2) Heavy Swing 3) Meditate")
                        selection = input(f"Which action will {player.name} take?  {player.name} has {player.health} health. {enemy2.name} has {max(enemy2.health,0)} health.\n\n 1) Light Swing\n 2) Heavy Swing\n 3) Meditate")
                    if selection == "1":
                        attack = random.randint(0,8)
                        if attack <= 7:
                            player.light_swing(enemy2)
                            if enemy2.health > 0:
                                enemy2.ogre_counterattack(player)
                                enemy3.ogre_counterattack(player)
                                enemy1.ogre_counterattack(player)
                        else:
                            print(BORDER)
                            print(f"{player.name} missed".center(70))
                            player.endurance -= 15
                            print(BORDER)
                            if enemy2.health > 0:
                                enemy2.ogre_counterattack(player)
                                enemy3.ogre_counterattack(player)
                                enemy1.ogre_counterattack(player)
                    elif selection == "2":
                        attack = random.randint(0,8)
                        if attack <= 7:
                            player.heavy_swing(enemy2)
                            if enemy2.health > 0:
                                enemy2.ogre_counterattack(player)
                                enemy3.ogre_counterattack(player)
                                enemy1.ogre_counterattack(player)
                        else:
                            print(BORDER)
                            print(f"{player.name} missed".center(70))
                            player.endurance -= 30
                            print(BORDER)
                            if enemy2.health > 0:
                                enemy2.ogre_counterattack(player)
                                enemy3.ogre_counterattack(player)
                                enemy1.ogre_counterattack(player)
                    elif selection == "3":
                        player.meditate()
                        if enemy2.health > 0:
                            enemy2.ogre_counterattack(player)
                            enemy3.ogre_counterattack(player)
                            enemy1.ogre_counterattack(player)
                else:
                    print(f"{enemy2.name} has perished. Try attacking another enemy.")
            if target == "3":
                if enemy3.health > 0:
                    print(BORDER)
                    selection = input(f"How will you attack?\n1) Light Swing - deals moderate physical damage.\n2) Heavy Swing - deals heavy physical damage.\n3) Meditate - moderately restores your health.")
                    while selection != "1" and selection != "2" and selection != "3":
                        print("Unrecognized selection. Please choose 1) Light Swing or 2) Heavy Swing 3) Meditate")
                        selection = input(f"Which action will {player.name} take?  {player.name} has {player.health} health. {enemy3.name} has {max(enemy3.health, 0)} health.\n\n 1) Light Swing\n 2) Heavy Swing\n 3) Meditate")
                    if selection == "1":
                        attack = random.randint(0,8)
                        if attack <= 7:
                            player.light_swing(enemy3)
                            if enemy3.health > 0:
                                enemy3.ogre_counterattack(player)
                                enemy1.ogre_counterattack(player)
                                enemy2.ogre_counterattack(player)
                        else:
                            print(BORDER)
                            print(f"{player.name} missed".center(70))
                            player.endurance -= 15
                            print(BORDER)
                            if enemy3.health > 0:
                                enemy3.ogre_counterattack(player)
                                enemy1.ogre_counterattack(player)
                                enemy2.ogre_counterattack(player)
                    elif selection == "2":
                        attack = random.randint(0,8)
                        if attack <= 7:
                            player.heavy_swing(enemy3)
                            if enemy3.health > 0:
                                enemy3.ogre_counterattack(player)
                                enemy1.ogre_counterattack(player)
                                enemy2.ogre_counterattack(player)
                        else:
                            print(BORDER)
                            print(f"{player.name} missed".center(70))
                            player.endurance -= 30
                            print(BORDER)
                            if enemy3.health > 0:
                                enemy3.ogre_counterattack(player)
                                enemy1.ogre_counterattack(player)
                                enemy2.ogre_counterattack(player)
                    elif selection == "3":
                        player.meditate()
                        if enemy3.health > 0:
                            enemy3.ogre_counterattack(player)
                            enemy1.ogre_counterattack(player)
                            enemy2.ogre_counterattack(player)
                else:
                    print(f"{enemy3.name} has perished. Try attacking another enemy.")

if __name__ == "__main__":
    three_enemies(Cloud, None, None, None)


