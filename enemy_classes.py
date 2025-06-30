import random
from constants import BORDER

class Ogre:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        if self.health <= 0:
            self.health = 0
    def overhead_smash(self, target):
        damage = int(round(self.strength * (random.uniform(0.25, 0.5))))
        target.health -= damage
        if target.health <=0:
            print(BORDER)
            print(f"{self.name}'s overhead smash deals {damage}. {target.name} has perished.".center(70))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name}'s overhead smash deals {damage} damage. {target.name}'s health is now {target.health}".center(70))
            print(BORDER)
    def grip_of_death(self, target):
        damage = int(round(self.strength * (random.uniform(0.5, 1.0))))
        target.health -= damage
        if target.health <= 0:
            print(BORDER)
            print(f"{self.name}'s grip of death deals {damage}. {target.name} has perished.".center(70))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name}'s grip of death deals {damage} damage. {target.name}'s health is now {target.health}".center(70))
            print(BORDER)
    def ogre_counterattack(self, target):
            counterattacks = [self.overhead_smash, self.grip_of_death]
            chosen_counter = random.choice(counterattacks)
            chosen_counter(target)

