import random
import time
from classes import border, Wizard, Warrior
from characters import Gandalf
from enemy_classes import Ogre


def campaign(player, *enemies):
    num_enemies = random.randint(1, 3)
    enemies = [Ogre(f"Ogre{i+1}", 100, 20) for i in range(num_enemies)]
    print(player)
    for enemy in enemies:
        print(enemy)

campaign(Gandalf, Ogre)
