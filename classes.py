import random

class Wizard: # Gandalf = Wizard("Gandalf", 100, 20, 20)
    def __init__(self, name, health, intelligence, wisdom):
        self.name = name
        self.health = health
        self.intelligence = intelligence
        self.wisdom = wisdom

    def cast_fireball(self, target):
        damage = int(round(self.intelligence + (self.wisdom * (random.uniform(0.5, 0.75)))))
        target.health -= damage
        print("======================================================================================================")
        print(f"{self.name} casts fireball dealing {damage} damage.")
        print("======================================================================================================")
        if target.health <= 0:
            print(f"{target.name} has perished in battle.\n\n{self.name} is victorious!")
            return
        else:
            print(f"{target.name}'s health is now {target.health}.")
            print("======================================================================================================")
            return
        

    def cast_lightning(self, target):
        damage = int(round(self.intelligence + (self.wisdom * (random.uniform(0.75, 1.25)))))
        target.health -= damage
        print("======================================================================================================")
        print(f"{self.name} casts lightning dealing {damage} damage.")
        print("======================================================================================================")
        if target.health <= 0:
            print(f"{target.name} has perished in battle.\n\n{self.name} is victorious!")
            return
        else:
            print(f"{target.name}'s health is now {target.health}.")
            print("======================================================================================================")
            return

class Warrior: # Cloud = Fighter("Cloud", 125, 20, 20)
    def __init__(self, name, health, strength, rage):
        self.name = name
        self.health = health
        self.strength = strength
        self.rage = rage

    def light_swing(self, target):
        damage = int(round(self.strength + (self.rage * (random.uniform(0.5, .75)))))
        target.health -= damage
        print("======================================================================================================")
        print(f"{self.name}'s light swing deals {damage} damage.")
        print("======================================================================================================")
        if target.health <= 0:
            print(f"{target.name} has perished in battle.\n\n{self.name} is victorious!")
            return
        else:
            print(f"{target.name}'s health is now {target.health}.")
            print("======================================================================================================")
            return
        

    def heavy_swing(self, target):
        damage = int(round(self.strength + (self.rage * random.uniform(.75, 1.25))))
        target.health -= damage
        print("======================================================================================================")
        print(f"{self.name}'s heavy swing deals {damage} damage.")
        print("======================================================================================================")
        if target.health <= 0:
            print(f"{target.name} has perished in battle.\n\n{self.name} is victorious!")
            return
        else:
            print(f"{target.name}'s health is now {target.health}.")
            print("======================================================================================================")
            return

