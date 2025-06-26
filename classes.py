import random
from constants import BOLD, END
border = "=" * 70

class Wizard: 
    def __init__(self, name, health, intelligence, wisdom):
        self.name = name
        self.health = health
        self.intelligence = intelligence
        self.wisdom = wisdom

    def cast_fireball(self, target):
        damage = int(round(self.intelligence + (self.wisdom * (random.uniform(1.0, 2.0)))))
        target.health -= damage
        if target.health <= 0:
            print(border)
            print(f"{self.name} casts fireball dealing {damage} damage.".center(70))
            print(border)
            print(f"{self.name} is victorious, {target.name} has perished in battle.\n".center(70))
            return
        else:
            print(border)
            print(f"{self.name} casts fireball dealing {damage} damage. {target.name}'s health is now {target.health}.".center(70))
            print(border)
            return
        

    def cast_lightning(self, target):
        damage = int(round(self.intelligence + (self.wisdom * (random.uniform(2.0, 3.0)))))
        target.health -= damage
        if target.health <= 0:
            print(border)
            print(f"{self.name} casts lightning dealing {damage} damage.".center(70))
            print(border)
            print(f"{self.name} is victorious, {target.name} has perished in battle.".center(70))
            return
        else:
            print(border)
            print(f"{self.name} casts lightning dealing {damage} damage. {target.name}'s health is now {target.health}.".center(70))
            print(border)
            return

    def healing_wave(self):
        healing_amount = int(round(self.intelligence + (self.wisdom * (random.uniform(1.0, 1.3)))))
        self.health += healing_amount
        print(border)
        print(f"{self.name} casts healing wave on himself for {healing_amount}. He now has {self.health} health.".center(70))
        print(border)

    def wizard_counterattack(self, target):
            counterattacks = [self.cast_fireball, self.cast_lightning, self.healing_wave]
            chosen_counter = random.choice(counterattacks)
            if chosen_counter == self.healing_wave:
                chosen_counter()
                return
            else:
                chosen_counter(target)

class Warrior:
    def __init__(self, name, health, strength, rage):
        self.name = name
        self.health = health
        self.strength = strength
        self.rage = rage

    def light_swing(self, target):
        damage = int(round(self.strength + (self.rage * (random.uniform(0.5, 1.0)))))
        target.health -= damage
        if target.health <= 0:
            print(border)
            print(f"\n{self.name}'s light swing deals {damage} damage.".center(70))
            print(border)
            print(f"{self.name} is victorious, {target.name} has perished in battle.\n".center(70))
            return
        else:
            print(border)
            print(f"{self.name}'s light swing deals {damage} damage. {target.name}'s health is now {target.health}.".center(70))
            print(border)
            return
        

    def heavy_swing(self, target):
        damage = int(round(self.strength + (self.rage * random.uniform(1.0, 2.0))))
        if target.health <= 0:
            print(border)
            print(f"\n{self.name}'s heavy swing deals {damage} damage.".center(70))
            print(border)
            print(f"{self.name} is victorious, {target.name} has perished in battle.\n".center(70))
            return
        else:
            print(border)
            print(f"{self.name}'s heavy swing deals {damage} damage. {target.name}'s health is now {target.health}.".center(70))
            print(border)
            return

    def meditate(self):
        healing_amount = int(round(self.strength + (self.rage * (random.uniform(0.4, 0.7)))))
        self.health += healing_amount
        print(border)
        print(f"{self.name} meditates, healing himself for {healing_amount}. He now has {self.health} health.".center(70))
        print(border)

    def warrior_counterattack(self, target):
            counterattacks = [self.light_swing, self.heavy_swing, self.meditate]
            chosen_counter = random.choice(counterattacks)
            if chosen_counter == self.meditate:
                chosen_counter()
            else:
                chosen_counter(target)
