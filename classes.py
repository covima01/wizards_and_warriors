
class Mage: # Gandalf = Mage("Gandalf", 100, 20, 20)
    def __init__(self, name, health, intelligence, wisdom):
        self.name = name
        self.health = health
        self.intelligence = intelligence
        self.wisdom = wisdom
    def cast_fireball(self, target):
        damage = self.intelligence + (self.wisdom * 1.25)
        target.health -= damage
        print("======================================================================================================")
        print(f"{self.name} casts fireball dealing {damage} damage.")
        print("======================================================================================================")
        print(f"{target.name}'s health is now {target.health}.")
        print("======================================================================================================")
    def cast_lightning(self, target):
        damage = self.intelligence + (self.wisdom * 1.5)
        target.health -= damage
        print("======================================================================================================")
        print(f"{self.name} casts lightning dealing {damage} damage.")
        print("======================================================================================================")
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
        print(f"{target.name}'s health is now {target.health}.")
        print("======================================================================================================")


