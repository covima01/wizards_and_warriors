import random
from constants import BOLD, END
border = "=" * 70

class Wizard: 
    def __init__(self, name, health, mana, intelligence, potions):
        self.name = name
        self.health = health
        self.mana = mana
        self.intelligence = intelligence
        self.potions = potions

    def cast_fireball(self, target):
        if self.mana >= 15:
            damage = int(round(self.intelligence * (random.uniform(1.0, 2.0))))
            target.health -= damage
            self.mana -= 15
            if target.health <= 0:
                print(border)
                print(f"{self.name} casts fireball dealing {damage} damage.".center(70))
                print(border)
                print(f"{self.name} is victorious, {target.name} has perished in battle.".center(70))
                return
            else:
                print(border)
                print(f"{self.name} casts fireball dealing {damage} damage. {target.name}'s health is now {target.health}.".center(70))
                print(border)
                return
        else:
            print(border)
            print(f"{self.name} doesn't have enough mana. Use a mana potion? (y/n)".center(70))
            selection = input()
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)")
                selection = input()
            if selection == "y":
                if self.potions > 0:
                    self.mana += 50
                    self.potions -= 1
                    print(f"{self.name} consumed a mana potion. Mana: {self.mana}. {self.potions} potions remaining".center(70))
                    print(border)
                else:
                    print(border)
                    print("No potions left. Good luck!")
            else:
                print(border)
                print("Not enough mana. Skipping turn".center(70))
        

    def cast_lightning(self, target):
        if self.mana >= 25:
            damage = int(round(self.intelligence * (random.uniform(2.0, 3.0))))
            target.health -= damage
            self.mana -= 25
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
        else:
            print(border)
            print(f"{self.name} doesn't have enough mana. Use a mana potion? (y/n)".center(70))
            selection = input()
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)")
                selection = input()
            if selection == "y":
                if self.potions > 0:
                    self.potions -= 1
                    self.mana += 50
                    print(f"{self.name} consumed a mana potion. Mana: {self.mana}. {self.potions} potions remaining.".center(70))
                    print(border)
                else:
                    print(border)
                    print("No potions left. Good luck!".center(70))
            else:
                print(border)
                print("Not enough mana. Skipping turn".center(70))
    def __str__(self):
        return f"{self.name} (Health: {self.health}, Mana: {self.mana})"
        

    def healing_wave(self):
        if self.mana >= 20:
            healing_amount = int(round(self.intelligence * (random.uniform(1.0, 1.3))))
            self.health += healing_amount
            self.mana -= 20
            print(border)
            print(f"{self.name} casts healing wave on himself for {healing_amount}. He now has {self.health} health.".center(70))
            print(border)
        else:
            print(border)
            print(f"{self.name} doesn't have enough mana. Use a mana potion? (y/n)".center(70))
            selection = input()
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)")
                selection = input()
            if selection == "y":
                if self.potions > 0:
                    self.potions -= 1
                    self.mana += 50
                    print(f"{self.name} consumed a mana potion. Mana: {self.mana}. {self.potions} potions remaining.".center(70))
                    print(border)
                else:
                    print(border)
                    print("No potions left. Good luck!")
            else:
                print(border)
                print("Not enough mana. Skipping turn".center(70))

    def wizard_counterattack(self, target):
            counterattacks = [self.cast_fireball, self.cast_lightning, self.healing_wave]
            chosen_counter = random.choice(counterattacks)
            if chosen_counter == self.healing_wave:
                if self.mana < 20:
                    if self.potions > 0:
                        self.mana += 50
                        print(f"{self.name} consumed a mana potion. Mana: {self.mana}".center(70))
                        print(border)  
                        return
                    else:
                        print(border)
                        print(f"{self.name} has no potions left. Push the attack!".center(70))
                else:
                    chosen_counter()
            elif chosen_counter == self.cast_fireball:
                if self.mana < 15:
                    if self.potions > 0:
                        self.mana += 50
                        print(f"{self.name} consumed a mana potion. Mana: {self.mana}".center(70))
                        print(border)
                        return
                    else:
                        print(border)
                        print(f"{self.name} has no potions left. Push the attack!".center(70))  
                else:
                    chosen_counter(target)
            elif chosen_counter == self.cast_lightning:
                if self.mana < 25:
                    if self.potions > 0:
                        self.mana += 50
                        print(f"{self.name} consumed a mana potion. Mana: {self.mana}".center(70))
                        print(border)
                    else:
                        print(border)
                        print(f"{self.name} has no potions left. Push the attack!".center(70))  
                else:
                    chosen_counter(target)

class Warrior:
    def __init__(self, name, health, endurance, strength, sacred_feathers):
        self.name = name
        self.health = health
        self.endurance = endurance
        self.strength = strength
        self.sacred_feathers = sacred_feathers

    def light_swing(self, target):
        if self.endurance >= 15:
            damage = int(round(self.strength * (random.uniform(0.75, 1.25))))
            target.health -= damage
            self.endurance -= 15
            if target.health <= 0:
                print(border)
                print(f"{self.name}'s light swing deals {damage} damage.".center(70))
                print(border)
                print(f"{self.name} is victorious, {target.name} has perished in battle.\n".center(70))
                return
            else:
                print(border)
                print(f"{self.name}'s light swing deals {damage} damage. {target.name}'s health is now {target.health}.".center(70))
                print(border)
                return
        else:
            print(border)
            print(f"{self.name} doesn't have enough endurance. Use a sacred feather? (y/n)".center(70))
            selection = input()
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)")
                selection = input()
            if selection == "y":
                self.endurance += 50
                print(f"{self.name} consumed a sacred feather. Endurance: {self.endurance}".center(70))
                print(border)
            else:
                print(border)
                print("Not enough endurance. Skipping turn".center(70))
            
        

    def heavy_swing(self, target):
        if self.endurance >= 30:
            damage = int(round(self.strength * random.uniform(1.5, 2.0)))
            target.health -= damage
            self.endurance -= 30
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
        else:
            print(border)
            print(f"{self.name} doesn't have enough endurance. Use a sacred feather? (y/n)".center(70))
            selection = input()
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)")
                selection = input()
            if selection == "y":
                self.endurance += 50
                print(f"{self.name} consumed a sacred feather. Endurance: {self.endurance}".center(70))
                print(border)
            else:
                print(border)
                print("Not enough endurance. Skipping turn".center(70))


    def meditate(self):
        if self.endurance >= 20:
            healing_amount = int(round(self.strength * (random.uniform(0.4, 0.7))))
            self.health += healing_amount
            self.endurance -= 20
            print(border)
            print(f"{self.name} meditates, healing himself for {healing_amount}. He now has {self.health} health.".center(70))
            print(border)
        else:
            print(border)
            print(f"{self.name} doesn't have enough endurance. Use a sacred feather? (y/n)".center(70))
            selection = input()
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)")
                selection = input()
            if selection == "y":
                self.endurance += 50
                print(f"{self.name} consumed a sacred feather. Endurance: {self.endurance}".center(70))
                print(border)
            else:
                print(border)
                print("Not enough endurance. Skipping turn".center(70))

    def warrior_counterattack(self, target):
            counterattacks = [self.light_swing, self.heavy_swing, self.meditate]
            chosen_counter = random.choice(counterattacks)
            if chosen_counter == self.light_swing:
                if self.endurance < 15:
                    self.endurance += 50
                    print(f"{self.name} consumed a sacred feather. Endurance: {self.endurance}".center(70))
                    print(border)  
                    return
                else:
                    chosen_counter(target)
            elif chosen_counter == self.heavy_swing:
                if self.endurance < 30:
                    self.endurance += 50
                    print(f"{self.name} consumed a sacred feather. Endurance: {self.endurance}".center(70))
                    print(border)  
                else:
                    chosen_counter(target)
            elif chosen_counter == self.meditate:
                if self.endurance < 20:
                    self.endurance += 50
                    print(f"{self.name} consumed a sacred feather. Endurance: {self.endurance}".center(70))
                    print(border)  
                else:
                    chosen_counter()
