import random
from classes import Mage, Fighter
from inputs import character_select


def main():
    running = True
    Gandalf = Mage("Gandalf", 100, 20, 20)
    Cloud = Fighter("Cloud", 125, 20, 20)

    # Character selection
    selection = input("Choose your character: 1 = Gandalf, 2 = Cloud\n")
    while selection != "1" and selection != "2":
        print("Unrecognized selection. Please choose 1 for Gandalf or 2 for Cloud\n")
        selection = input("Choose your character: 1 = Gandalf, 2 = Cloud\n")
    if selection == "1":
        print("You've selected Gandalf.")
        input("Hit enter to continue")
    elif selection == "2":
        print("You've selected Cloud")
        input("Hit enter to continue")

    while running:
        # Playing as Gandalf
        if selection == "1":
            if Gandalf.health <= 0:
                print("Gandalf is dead. Game over.")
                return
            elif Cloud.health <= 0:
                print("Cloud is dead. Game over.")
                return
            else:
                attack = random.randint(0,2)
                if attack == 0:
                    Gandalf.cast_fireball(Cloud)
                    if Cloud.health <= 0:
                        return
                elif attack == 1:
                    Gandalf.cast_lightning(Cloud)
                    if Cloud.health <= 0:
                        return
                elif attack == 2:
                    print("Gandalf missed")
        # Playing as Cloud
        elif selection == "2":
            if Gandalf.health <= 0:
                return
            elif Cloud.health <= 0:
                return
            else:
                attack = random.randint(0,2)
                if attack == 0:
                    Cloud.swing_axe(Gandalf)
                elif attack == 1:
                    Cloud.heavy_swing(Gandalf)
                elif attack == 2:
                    print("Cloud missed")
                




main()