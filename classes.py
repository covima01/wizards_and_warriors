import random
from constants import BOLD, END, BORDER


class Wizard: 
    def __init__(self, name, health, mana, intelligence, xp, level, potions):
        self.name = name
        self.health = health
        self.resource = mana
        self.intelligence = intelligence
        self.xp = xp
        self.level = level
        self.resource_gain = potions
        self.resource_type = "Mana"
        self.resource_gain_description = "Mana Potion"
        self.attack1 = "Fireball"
        self.attack1_description = "deals moderate fire damage..."
        self.attack2 = "Lightning"
        self.attack2_description = "deals heavy lightning damage..."
        self.heal1 = "Healing Wave"
        self.heal1_description = "restores a moderate amount of health..."
        self.attack1_method = self.cast_fireball
        self.attack2_method = self.cast_lightning
        self.heal1_method = self.healing_wave
        self.counterattack_method = self.counterattack

    def cast_fireball(self, target):
        if self.resource >= 15:
            damage = int(round(self.intelligence * (random.uniform(1.0, 2.0))))
            target.health -= damage
            self.resource -= 15
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack1} dealing {damage} damage.".center(70))
                print(BORDER)
                print(f"{self.name} is victorious, {target.name} has perished in battle.".center(70))
                return
            else:
                print(BORDER)
                print(f"{self.name} uses {self.attack1} dealing {damage} damage. {target.name}'s health is now {target.health}.".center(70))
                print(BORDER)
                return
        else:
            print(BORDER)
            print(f"{self.name} doesn't have enough {self.resource_type}. Use a {self.resource_gain}? (y/n)".center(70))
            selection = input()
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)")
                selection = input()
            if selection == "y":
                if self.resource_gain > 0:
                    self.resource += 50
                    self.resource_gain -= 1
                    print(f"{self.name} consumed a {self.resource_gain}. {self.resource_type}: {self.resource}. {self.resource_gain} {self.resource_type} remaining".center(70))
                    print(BORDER)
                else:
                    print(BORDER)
                    print(f"No {self.resource_type}'s left. Good luck!")
            else:
                print(BORDER)
                print("Not enough mana. Skipping turn".center(70))
    def cast_lightning(self, target):
        if self.resource >= 25:
            damage = int(round(self.intelligence * (random.uniform(2.0, 3.0))))
            target.health -= damage
            self.resource -= 25
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack2} dealing {damage} damage.".center(70))
                print(BORDER)
                print(f"{self.name} is victorious, {target.name} has perished in battle.".center(70))
                return
            else:
                print(BORDER)
                print(f"{self.name} uses {self.attack2} dealing {damage} damage. {target.name}'s health is now {target.health}.".center(70))
                print(BORDER)
                return
        else:
            print(BORDER)
            print(f"{self.name} doesn't have enough {self.resource_type}. Use a {self.resource_gain_description}? (y/n)".center(70))
            selection = input()
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)")
                selection = input()
            if selection == "y":
                if self.resource_gain > 0:
                    self.resource_gain -= 1
                    self.resource += 50
                    print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}. {self.resource_gain} {self.resource_gain_description}'s remaining.".center(70))
                    print(BORDER)
                else:
                    print(BORDER)
                    print(f"No {self.resource_gain_description}'s left. Good luck!".center(70))
            else:
                print(BORDER)
                print(f"Not enough {self.resource_type}. Skipping turn".center(70))
    def __str__(self):
        return f"{self.name} (Health: {self.health}, {self.resource_type}: {self.resource})"
    def healing_wave(self):
        if self.resource >= 20:
            healing_amount = int(round(self.intelligence * (random.uniform(1.0, 1.3))))
            self.health += healing_amount
            self.resource -= 20
            print(BORDER)
            print(f"{self.name} uses {self.heal1} for {healing_amount}. Health: {self.health}".center(70))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name} doesn't have enough {self.resource_type}. Use a {self.resource_gain}? (y/n)".center(70))
            selection = input()
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)")
                selection = input()
            if selection == "y":
                if self.resource_gain > 0:
                    self.resource_gain -= 1
                    self.resource += 50
                    print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}. {self.resource_gain} {self.resource_gain_description}'s remaining.".center(70))
                    print(BORDER)
                else:
                    print(BORDER)
                    print(f"No {self.resource_type} left. Good luck!")
            else:
                print(BORDER)
                print(f"Not enough {self.resource_type}. Skipping turn".center(70))
    def counterattack(self, target):
            counterattacks = [self.attack1_method, self.attack2_method, self.heal1_method]
            chosen_counter = random.choice(counterattacks)
            if chosen_counter == self.heal1_method:
                if self.resource < 20:
                    if self.resource_gain > 0:
                        self.resource += 50
                        print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(70))
                        print(BORDER)  
                        return
                    else:
                        print(BORDER)
                        print(f"{self.name} has no {self.resource_gain_description}'s left. Push the attack!".center(70))
                else:
                    chosen_counter()
            elif chosen_counter == self.attack1_method:
                if self.resource < 15:
                    if self.resource_gain > 0:
                        self.resource += 50
                        print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(70))
                        print(BORDER)
                        return
                    else:
                        print(BORDER)
                        print(f"{self.name} has no {self.resource_gain_description}'s left. Push the attack!".center(70))  
                else:
                    chosen_counter(target)
            elif chosen_counter == self.attack2_method:
                if self.resource < 25:
                    if self.resource_gain > 0:
                        self.resource += 50
                        print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(70))
                        print(BORDER)
                    else:
                        print(BORDER)
                        print(f"{self.name} has no {self.resource_gain_description}'s left. Push the attack!".center(70))  
                else:
                    chosen_counter(target)

class Warrior:
    def __init__(self, name, health, endurance, strength, sacred_feathers):
        self.name = name
        self.health = health
        self.resource = endurance
        self.strength = strength
        self.resource_gain = sacred_feathers
        self.resource_type = "Endurance"
        self.resource_gain_description = "Sacred Feather"
        self.attack1 = "Light Swing"
        self.attack1_description = "deals moderate physical damage..."
        self.attack2 = "Heavy Swing"
        self.attack2_description = "deals heavy physical damage..."
        self.heal1 = "Meditate"
        self.heal1_description = "restores a moderate amount of health..."
        self.attack1_method = self.light_swing        
        self.attack2_method = self.heavy_swing
        self.heal1_method = self.meditate

    def light_swing(self, target):
        if self.resource >= 15:
            damage = int(round(self.strength * (random.uniform(0.75, 1.25))))
            target.health -= damage
            self.resource -= 15
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack1} dealing {damage} damage.".center(70))
                print(BORDER)
                print(f"{self.name} is victorious, {target.name} has perished in battle.\n".center(70))
                return
            else:
                print(BORDER)
                print(f"{self.name} uses {self.attack1} dealing {damage} damage. {target.name}'s health is now {target.health}.".center(70))
                print(BORDER)
                return
        else:
            print(BORDER)
            print(f"{self.name} doesn't have enough {self.resource}. Use a {self.resource_gain_description}? (y/n)".center(70))
            selection = input()
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)")
                selection = input()
            if selection == "y":
                self.resource += 50
                print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(70))
                print(BORDER)
            else:
                print(BORDER)
                print(f"Not enough {self.resource_type}. Skipping turn".center(70))
            
        

    def heavy_swing(self, target):
        if self.resource >= 30:
            damage = int(round(self.strength * random.uniform(1.5, 2.0)))
            target.health -= damage
            self.resource -= 30
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack2} dealing {damage} damage.".center(70))
                print(BORDER)
                print(f"{self.name} is victorious, {target.name} has perished in battle.\n".center(70))
                return
            else:
                print(BORDER)
                print(f"{self.name} uses {self.attack2} dealing {damage} damage. {target.name}'s health is now {target.health}.".center(70))
                print(BORDER)
                return
        else:
            print(BORDER)
            print(f"{self.name} doesn't have enough {self.resource_type}. Use a {self.resource_gain_description}? (y/n)".center(70))
            selection = input()
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)")
                selection = input()
            if selection == "y":
                self.resource += 50
                print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(70))
                print(BORDER)
            else:
                print(BORDER)
                print(f"Not enough {self.resource_type}. Skipping turn".center(70))


    def meditate(self):
        if self.resource >= 20:
            healing_amount = int(round(self.strength * (random.uniform(0.4, 0.7))))
            self.health += healing_amount
            self.resource -= 20
            print(BORDER)
            print(f"{self.name} uses {self.heal1} for {healing_amount}. Health: {self.health}".center(70))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name} doesn't have enough {self.resource_type}. Use a {self.resource_gain_description}? (y/n)".center(70))
            selection = input()
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)")
                selection = input()
            if selection == "y":
                self.resource += 50
                print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(70))
                print(BORDER)
            else:
                print(BORDER)
                print(f"Not enough {self.resource_type}. Skipping turn".center(70))

    def counterattack(self, target):
            counterattacks = [self.attack1_method, self.attack2_method, self.heal1_method]
            chosen_counter = random.choice(counterattacks)
            if chosen_counter == self.attack1_method:
                if self.resource < 15:
                    self.resource += 50
                    print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(70))
                    print(BORDER)  
                    return
                else:
                    chosen_counter(target)
            elif chosen_counter == self.attack2_method:
                if self.resource < 30:
                    self.resource += 50
                    print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(70))
                    print(BORDER)  
                else:
                    chosen_counter(target)
            elif chosen_counter == self.heal1_method:
                if self.resource < 20:
                    self.resource += 50
                    print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(70))
                    print(BORDER)  
                else:
                    chosen_counter()
