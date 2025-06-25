import random
from constants import BOLD, END

class Wizard: # Gandalf = Wizard("Gandalf", 100, 20, 20)
    def __init__(self, name, health, intelligence, wisdom):
        self.name = name
        self.health = health
        self.intelligence = intelligence
        self.wisdom = wisdom

    def cast_fireball(self, target):
        damage = int(round(self.intelligence + (self.wisdom * (random.uniform(0.5, 0.75)))))
        target.health -= damage
        print("\n======================================================================================================")
        print(f"\n{BOLD}{self.name}{END} casts fireball dealing {damage} damage.")
        print("======================================================================================================\n")
        if target.health <= 0:
            print(f"{target.name} has perished in battle.\n\n{BOLD}{self.name}{END} is victorious!")
            return
        else:
            print(f"{target.name}'s health is now {target.health}.")
            print("======================================================================================================\n\n")
            return
        

    def cast_lightning(self, target):
        damage = int(round(self.intelligence + (self.wisdom * (random.uniform(0.75, 1.25)))))
        target.health -= damage
        print("\n======================================================================================================")
        print(f"\n{BOLD}{self.name}{END} casts lightning dealing {damage} damage.")
        print("======================================================================================================\n")
        if target.health <= 0:
            print(f"{target.name} has perished in battle.\n\n{BOLD}{self.name}{END} is victorious!")
            return
        else:
            print(f"{target.name}'s health is now {target.health}.")
            print("======================================================================================================\n\n")
            return

    def healing_wave(self):
        healing_amount = int(round(self.intelligence + (self.wisdom * (random.uniform(0.4, 0.7)))))
        self.health += healing_amount
        print("\n======================================================================================================")
        print(f"\n{BOLD}{self.name}{END} casts healing wave, healing himself for {healing_amount}")
        print("======================================================================================================\n")
        print(f"{BOLD}{self.name}{END} now has {self.health} health.")
        print("======================================================================================================\n")

    def wizard_counterattack(self, target):
        counterattacks = [self.cast_fireball, self.cast_lightning, self.healing_wave]
        chosen_counter = random.choice(counterattacks)
        if chosen_counter == self.healing_wave:
            chosen_counter()
        else:
            chosen_counter(target)



class Warrior: # Cloud = Fighter("Cloud", 125, 20, 20)
    def __init__(self, name, health, strength, rage):
        self.name = name
        self.health = health
        self.strength = strength
        self.rage = rage

    def light_swing(self, target):
        damage = int(round(self.strength + (self.rage * (random.uniform(0.5, .75)))))
        target.health -= damage
        print("\n======================================================================================================")
        print(f"\n{BOLD}{self.name}{END}'s light swing deals {damage} damage.")
        print("======================================================================================================\n")
        if target.health <= 0:
            print(f"{target.name} has perished in battle.\n\n{BOLD}{self.name}{END} is victorious!")
            return
        else:
            print(f"{target.name}'s health is now {target.health}.")
            print("======================================================================================================\n\n")
            return
        

    def heavy_swing(self, target):
        damage = int(round(self.strength + (self.rage * random.uniform(.75, 1.25))))
        target.health -= damage
        print("\n======================================================================================================")
        print(f"\n{BOLD}{self.name}{END}'s heavy swing deals {damage} damage.")
        print("======================================================================================================\n")
        if target.health <= 0:
            print(f"{target.name} has perished in battle.\n\n{BOLD}{self.name}{END} is victorious!")
            return
        else:
            print(f"{target.name}'s health is now {target.health}.")
            print("======================================================================================================\n\n")
            return

    def meditate(self):
        healing_amount = int(round(self.strength + (self.rage * (random.uniform(0.4, 0.7)))))
        self.health += healing_amount
        print("\ns======================================================================================================")
        print(f"\n{BOLD}{self.name}{END} meditates, healing himself for {healing_amount}")
        print("======================================================================================================\n\n")
        print(f"{BOLD}{self.name}{END} now has {self.health} health.")
        print("======================================================================================================\n")

    def warrior_counterattack(self, target):
        counterattacks = [self.light_swing, self.heavy_swing, self.meditate]
        chosen_counter = random.choice(counterattacks)
        if chosen_counter == self.meditate:
            chosen_counter()
        else:
            chosen_counter(target)
