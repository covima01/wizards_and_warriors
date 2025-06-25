import random
import time
from constants import BOLD, END
from characters import Gandalf, Cloud


def combat(player, enemy):
    if player == Gandalf:
        while enemy.health > 0:
            time.sleep(0.5)
            selection = input("Which action will you take?\n\n 1) Cast Fireball - deals moderate fire damage.\n 2) Cast Lightning - deals heavy lightning damage.\n 3) Healing Wave = moderately replenishes your health.")
            while selection != "1" and selection != "2" and selection != "3":
                print("Unrecognized selection. Please choose 1 to Cast Fireball or 2 to Cast Lightning or 3 to Cast Healing Surge\n")
                selection = input("Which action will you take?\n\n 1) Cast Fireball\n 2) Cast Lightning\n\n 3) Healing Surge")
            if selection == "1":
                attack = random.randint(0,8)
                if attack <= 7:
                    player.cast_fireball(enemy)
                else:
                    print("======================================================================================================")
                    print(f"\n{BOLD}{player.name}{END} missed")
                    print("======================================================================================================\n")
            elif selection == "2":
                attack = random.randint(0,8)
                if attack <= 7:
                    player.cast_lightning(enemy)   
                else:
                    print("======================================================================================================")
                    print(f"\n{BOLD}{player.name}{END} missed")
                    print("======================================================================================================\n")
            elif selection == "3":
                player.healing_wave()
        else:
            return
    elif player == Cloud:
        while enemy.health > 0:
            time.sleep(0.5)
            selection = input("Which action will you take?\n\n 1) Light Swing - deals moderate physical damage.\n 2) Heavy Swing - deals heavy physical damage.\n 3) Meditate - moderately restores your health.")
            while selection != "1" and selection != "2" and selection != "3":
                print("Unrecognized selection. Please choose 1) Light Swing or 2) Heavy Swing\n 3) Meditate")
                selection = input("Which action will you take?\n\n 1) Light Swing\n 2) Heavy Swing\n\n 3) Meditate")
            if selection == "1":
                attack = random.randint(0,8)
                if attack <= 7:
                    player.light_swing(enemy)
                else:
                    print("======================================================================================================")
                    print(f"\n{BOLD}{player.name}{END} missed")
                    print("======================================================================================================\n")
            elif selection == "2":
                attack = random.randint(0,8)
                if attack <= 7:
                    player.heavy_swing(enemy)
                else:
                    print("======================================================================================================")
                    print(f"\n{BOLD}{player.name}{END} missed")
                    print("======================================================================================================\n")
            elif selection == "3":
                player.meditate()
            

