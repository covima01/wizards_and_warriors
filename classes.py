import random

class Mage: # Gandalf = Mage("Gandalf", 100, 20, 20)
    def __init__(self, name, health, intelligence, wisdom):
        self.name = name
        self.health = health
        self.intelligence = intelligence
        self.wisdom = wisdom
    def cast_fireball(self, target):
        damage = int(round(self.intelligence + (self.wisdom * (random.uniform(0.8, 1.2)))))
        target.health -= damage
        print("======================================================================================================")
        print(f"{self.name} casts fireball dealing {damage} damage.")
        print("======================================================================================================")
        if target.health <= 0:
            print(f"{target.name} is dead. Game over.")
            return
        else:
            print(f"{target.name}'s health is now {target.health}.")
    def cast_lightning(self, target):
        damage = int(round(self.intelligence + (self.wisdom * (random.uniform(0.9, 1.4)))))
        target.health -= damage
        print("======================================================================================================")
        print(f"{self.name} casts lightning dealing {damage} damage.")
        print("======================================================================================================")
        if target.health <= 0:
            print(f"{target.name} is dead. Game over.")
            return
        else:
            print(f"{target.name}'s health is now {target.health}.")

class Fighter: # Cloud = Fighter("Cloud", 125, 20, 20)
    def __init__(self, name, health, strength, rage):
        self.name = name
        self.health = health
        self.strength = strength
        self.rage = rage
    def swing_axe(self, target):
        damage = int(round(self.strength + (self.rage * (random.uniform(0.8, 1.2)))))
        target.health -= damage
        print("======================================================================================================")
        print(f"{self.name} swings his axe dealing {damage} damage.")
        print("======================================================================================================")
        if target.health <= 0:
            print(f"{target.name} is dead. Game over.")
            return
        else:
            print(f"{target.name}'s health is now {target.health}.")
    def heavy_swing(self, target):
        damage = int(round(self.strength + (self.rage * random.uniform(0.9, 1.4))))
        target.health -= damage
        print("======================================================================================================")
        print(f"{self.name}'s heavy swing deals {damage} damage.")
        print("======================================================================================================")
        if target.health <= 0:
            print(f"{target.name} is dead. Game over.")
            return
        else:
            print(f"{target.name}'s health is now {target.health}.")

