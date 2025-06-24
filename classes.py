import random

class Mage: # Gandalf = Mage("Gandalf", 100, 20, 20)
    def __init__(self, name, health, intelligence, wisdom):
        self.name = name
        self.health = health
        self.intelligence = intelligence
        self.wisdom = wisdom
    def cast_fireball(self, target):
        damage = self.intelligence + (self.wisdom * (random.uniform(0.8, 1.2)))
        target.health -= damage
        print("======================================================================================================")
        print(f"{self.name} casts fireball dealing {damage} damage.")
        print("======================================================================================================")
        if target.health <= 0:
            print(f"{target.name} is dead. Game over.")
            return
        else:
            print(f"{target.name}'s health is now {target.health}.")
            print("======================================================================================================")
    def cast_lightning(self, target):
        damage = self.intelligence + (self.wisdom * (random.uniform(0.9, 1.4)))
        target.health -= damage
        print("======================================================================================================")
        print(f"{self.name} casts lightning dealing {damage} damage.")
        print("======================================================================================================")
        if target.health <= 0:
            print(f"{target.name} is dead. Game over.")
            return
        else:
            print(f"{target.name}'s health is now {target.health}.")
            print("======================================================================================================")

class Fighter: # Cloud = Fighter("Cloud", 125, 20, 20)
    def __init__(self, name, health, strength, rage):
        self.name = name
        self.health = health
        self.strength = strength
        self.rage = rage
    def swing_axe(self, target):
        damage = self.strength + (self.rage * 1.25)
        target.health -= damage
        print("======================================================================================================")
        print(f"{self.name} swings his axe dealing {damage} damage.")
        print("======================================================================================================")
        if target.health <= 0:
            print(f"{target.name} is dead. Game over.")
            return
        else:
            print(f"{target.name}'s health is now {target.health}.")
            print("======================================================================================================")
    def heavy_swing(self, target):
        damage = self.strength + (self.rage * 1.5)
        target.health -= damage
        print("======================================================================================================")
        print(f"{self.name}'s heavy swing deals {damage} damage.")
        print("======================================================================================================")
        if target.health <= 0:
            print(f"{target.name} is dead. Game over.")
            return
        else:
            print(f"{target.name}'s health is now {target.health}.")
            print("======================================================================================================")

