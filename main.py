from classes import Mage, Fighter
from inputs import character_select


def main():
    running = True
    Gandalf = Mage("Gandalf", 100, 20, 20)
    Cloud = Fighter("Cloud", 125, 20, 20)
    character_select()
    while running:
        if Gandalf.health <= 0:
            print("Gandalf is dead. Game over.")
            return
        elif Cloud.health <= 0:
            print("Cloud is dead. Game over.")
            return
        else:
            Gandalf.cast_fireball(Cloud)



main()