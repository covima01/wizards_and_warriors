import random
from constants import BORDER

class Wizard: 
    def __init__(self, name, health, mana, intelligence, xp, level, potions):
        self.name = name
        self.health = health
        self.max_health = self.health
        self.resource = mana
        self.max_resource = self.resource
        self.intelligence = intelligence
        self.xp = xp
        self.level = level
        self.resource_gain = potions
        self.resource_type = "Mana"
        self.resource_gain_description = "Mana Potion"
    def cast_fireball(self, target):
        if self.resource >= self.attack1_cost:
            damage = int(round(self.intelligence * (random.uniform(1.0, 2.0))))
            target.health -= damage
            self.resource -= self.attack1_cost
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack1} dealing {damage} damage.".center(100))
                print(BORDER)
                print(f"{target.name} has perished.".center(100))
                print(BORDER)
                return
            else:
                print(BORDER)
                print(f"{self.name} uses {self.attack1} dealing {damage} damage. {target.name}'s health is now {target.health}.".center(100))
                print(BORDER)
                return
        else:
            print(BORDER)
            print(f"{self.name} doesn't have enough {self.resource_type}. Use a {self.resource_gain}? (y/n)".center(100))
            selection = input()
            print(BORDER)
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)".center(100))
                selection = input()
            if selection == "y":
                if self.resource_gain > 0:
                    self.resource += 50
                    self.resource_gain -= 1
                    print(f"{self.name} consumed a {self.resource_gain}. {self.resource_type}: {self.resource}. {self.resource_gain} {self.resource_type} remaining".center(100))
                    print(BORDER)
                else:
                    print(BORDER)
                    print(f"No {self.resource_type}'s left. Good luck!".center(100))
            else:
                print(BORDER)
                print("Not enough mana. Skipping turn".center(100))
    def cast_lightning(self, target):
        if self.resource >= self.attack2_cost:
            damage = int(round(self.intelligence * (random.uniform(2.0, 3.0))))
            target.health -= damage
            self.resource -= self.attack2_cost
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack2} dealing {damage} damage.".center(100))
                print(BORDER)
                print(f"{target.name} has perished.".center(100))
                print(BORDER)
                return
            else:
                print(BORDER)
                print(f"{self.name} uses {self.attack2} dealing {damage} damage. {target.name}'s health is now {target.health}.".center(100))
                print(BORDER)
                return
        else:
            print(BORDER)
            print(f"{self.name} doesn't have enough {self.resource_type}. Use a {self.resource_gain_description}? (y/n)".center(100))
            selection = input()
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)".center(100))
                selection = input()
            if selection == "y":
                if self.resource_gain > 0:
                    self.resource_gain -= 1
                    self.resource += 50
                    print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}. {self.resource_gain} {self.resource_gain_description}'s remaining.".center(100))
                    print(BORDER)
                else:
                    print(BORDER)
                    print(f"No {self.resource_gain_description}'s left. Good luck!".center(100))
            else:
                print(BORDER)
                print(f"Not enough {self.resource_type}. Skipping turn".center(100))
    def healing_wave(self):
        if self.resource >= 20:
            healing_amount = int(round(self.intelligence * (random.uniform(1.0, 1.3))))
            self.health += healing_amount
            self.resource -= self.heal1_cost
            print(BORDER)
            print(f"{self.name} uses {self.heal1} for {healing_amount}. Health: {self.health}".center(100))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name} doesn't have enough {self.resource_type}. Use a {self.resource_gain}? (y/n)".center(100))
            selection = input()
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)".center(100))
                selection = input()
            if selection == "y":
                if self.resource_gain > 0:
                    self.resource_gain -= 1
                    self.resource += 50
                    print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}. {self.resource_gain} {self.resource_gain_description}'s remaining.".center(100))
                    print(BORDER)
                else:
                    print(BORDER)
                    print(f"No {self.resource_type} left. Good luck!".center(100))
            else:
                print(BORDER)
                print(f"Not enough {self.resource_type}. Skipping turn".center(100))
    def counterattack(self, target):
            counterattacks = [self.attack1_method, self.attack2_method, self.heal1_method]
            chosen_counter = random.choice(counterattacks)
            if chosen_counter == self.heal1_method:
                if self.resource < 20:
                    if self.resource_gain > 0:
                        self.resource += 50
                        print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(100))
                        print(BORDER)  
                        return
                    else:
                        print(BORDER)
                        print(f"{self.name} has no {self.resource_gain_description}'s left. Push the attack!".center(100))
                else:
                    chosen_counter()
            elif chosen_counter == self.attack1_method:
                if self.resource < 15:
                    if self.resource_gain > 0:
                        self.resource += 50
                        print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(100))
                        print(BORDER)
                        return
                    else:
                        print(BORDER)
                        print(f"{self.name} has no {self.resource_gain_description}'s left. Push the attack!".center(100))  
                else:
                    chosen_counter(target)
            elif chosen_counter == self.attack2_method:
                if self.resource < 25:
                    if self.resource_gain > 0:
                        self.resource += 50
                        print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(100))
                        print(BORDER)
                    else:
                        print(BORDER)
                        print(f"{self.name} has no {self.resource_gain_description}'s left. Push the attack!".center(100))  
                else:
                    chosen_counter(target)
    def level_up(self):
        # Level 2
        if self.xp > 20:
            if self.level == 1:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 50")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
        # Level 3
        if self.xp > 50:
            if self.level == 2:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 90")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
        # Level 4
        if self.xp > 90:
            if self.level == 3:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 140")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
        # Level 5
        if self.xp > 140:
            if self.level == 4:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 200")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
        # Level 6
        if self.xp > 200:
            if self.level == 5:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 270")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
        # Level 7
        if self.xp > 270:
            if self.level == 6:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 350")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
        # Level 8
        if self.xp > 350:
            if self.level == 7:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 440")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
        # Level 9
        if self.xp > 440:
            if self.level == 8:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 540")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
        # Level 10
        if self.xp > 540:
            if self.level == 9:
                self.level += 1
                print(f"{self.name} has reached MAX level {self.level}!")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
    def skill_up(self, selection):
        if selection == "Health":
            self.max_health += 25
            print(BORDER)
            print(f"Health increased by 25!")
            print(BORDER)
        if selection == "Mana":
            self.max_resource += 25
            print(BORDER)
            print(f"Mana increased by 25!")
            print(BORDER)
        if selection == "Intelligence":
            self.intelligence += 5
            print(BORDER)
            print(f"Intelligence increased by 5!")
            print(BORDER)
        if selection == "Potions":
            self.resource_gain += 1
            print(BORDER)
            print(f"Max potions increased by 1!")
            print(BORDER)
class Gray_Scholar(Wizard):
    def __init__(self, name, health, mana, intelligence, xp, level, potions):
        super().__init__(name, health, mana, intelligence, xp, level, potions)
        self.description = (f"{self.name}: a mysterious outcast. Unremarkable.")
        self.attack1, self.attack1_description, self.attack1_combined, self.attack1_cost = "Freeze", "deals moderate damage...", "1) Freeze - deals moderate damage.", 5
        self.attack2, self.attack2_description, self.attack2_combined, self.attack2_cost = "Combust", "deals heavy damage...", "2) Combust - deals heavy damage.", 10
        self.heal1, self.heal1_description, self.heal1_combined, self.heal1_cost = "Heal", "restores your life...", "3) Heal - restores your life.", 10
        self.attack1_method, self.attack2_method, self.heal1_method, self.counterattack_method = self.shock, self.combust, self.regen, self.counterattack
        self.stats = ["Health", "Mana", "Intelligence", "Potions"]
        self.attacks = [self.attack1_combined, self.attack2_combined, self.heal1_combined]
    def shock(self, target):
        if self.resource >= self.attack1_cost:
            damage = int(round(self.intelligence * (random.uniform(1.0, 2.0))))
            target.health -= damage
            self.resource -= self.attack1_cost
            if target.health <= 0:               
                print(BORDER)
                print(f"{self.name} uses {self.attack1} dealing {damage} damage.".center(100))
                print(BORDER)
                print(f"{target.name} has perished.".center(100))
                print(BORDER)               
                return
            else:                
                print(BORDER)
                print(f"{self.name} uses {self.attack1} dealing {damage} damage. {target.name}'s health is now {target.health}.".center(100))
                print(BORDER)               
                return
        else:            
            print(BORDER)
            print(f"{self.name} doesn't have enough {self.resource_type}. Use a {self.resource_gain}? (y/n)".center(100))
            selection = input()
            print(BORDER)
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)".center(100))
                selection = input()
            if selection == "y":
                if self.resource_gain > 0:
                    self.resource += 50
                    self.resource_gain -= 1
                    print(f"{self.name} consumed a {self.resource_gain}. {self.resource_type}: {self.resource}. {self.resource_gain} {self.resource_type} remaining".center(100))
                    print(BORDER)    
                else:
                    print(BORDER)
                    print(f"No {self.resource_type}'s left. Good luck!".center(100))  
            else:
                print(BORDER)
                print("Not enough mana. Skipping turn".center(100))
    def combust(self, target):
        if self.resource >= self.attack2_cost:
            damage = int(round(self.intelligence * (random.uniform(2.0, 3.0))))
            target.health -= damage
            self.resource -= self.attack2_cost
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack2} dealing {damage} damage.".center(100))
                print(BORDER)
                print(f"{target.name} has perished.".center(100))
                print(BORDER)
                return
            else:
                print(BORDER)
                print(f"{self.name} uses {self.attack2} dealing {damage} damage. {target.name}'s health is now {target.health}.".center(100))
                print(BORDER)
                return
        else:
            print(BORDER)
            print(f"{self.name} doesn't have enough {self.resource_type}. Use a {self.resource_gain_description}? (y/n)".center(100))
            selection = input()
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)")
                selection = input()
            if selection == "y":
                if self.resource_gain > 0:
                    self.resource_gain -= 1
                    self.resource += 50
                    print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}. {self.resource_gain} {self.resource_gain_description}'s remaining.".center(100))
                    print(BORDER)
                else:
                    print(BORDER)
                    print(f"No {self.resource_gain_description}'s left. Good luck!".center(100))   
            else:
                print(BORDER)
                print(f"Not enough {self.resource_type}. Skipping turn".center(100))
    def regen(self):
        if self.resource >= 20:
            healing_amount = int(round(self.intelligence * (random.uniform(1.0, 1.3))))
            self.health += healing_amount
            self.resource -= self.heal1_cost
            print(BORDER)
            print(f"{self.name} uses {self.heal1} for {healing_amount}. Health: {self.health}".center(100))
            print(BORDER) 
        else:
            print(BORDER)
            print(f"{self.name} doesn't have enough {self.resource_type}. Use a {self.resource_gain}? (y/n)".center(100))
            selection = input()
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)".center(100))
                selection = input()   
            if selection == "y":
                if self.resource_gain > 0:
                    self.resource_gain -= 1
                    self.resource += 50
                    print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}. {self.resource_gain} {self.resource_gain_description}'s remaining.".center(100))
                    print(BORDER)
                else:
                    print(BORDER)
                    print(f"No {self.resource_type} left. Good luck!".center(100))  
            else:
                print(BORDER)
                print(f"Not enough {self.resource_type}. Skipping turn".center(100))               
    def counterattack(self, target):
            counterattacks = [self.attack1_method, self.attack2_method, self.heal1_method]
            chosen_counter = random.choice(counterattacks)
            if chosen_counter == self.heal1_method:
                if self.resource < 20:
                    if self.resource_gain > 0:
                        self.resource += 50
                        print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(100))
                        print(BORDER)  
                        return
                    else:
                        print(BORDER)
                        print(f"{self.name} has no {self.resource_gain_description}'s left. Push the attack!".center(100))        
                else:
                    chosen_counter()
            elif chosen_counter == self.attack1_method:
                if self.resource < 15:
                    if self.resource_gain > 0:
                        self.resource += 50
                        print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(100))
                        print(BORDER)
                        return
                    else:
                        print(BORDER)
                        print(f"{self.name} has no {self.resource_gain_description}'s left. Push the attack!".center(100))          
                else:
                    chosen_counter(target)
            elif chosen_counter == self.attack2_method:
                if self.resource < 25:
                    if self.resource_gain > 0:
                        self.resource += 50
                        print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(100))
                        print(BORDER)
                    else:
                        print(BORDER)
                        print(f"{self.name} has no {self.resource_gain_description}'s left. Push the attack!".center(100))          
                else:
                    chosen_counter(target)
class Warrior:
    def __init__(self, name, health, endurance, strength, xp, level, sacred_feathers):
        self.name = name
        self.health = health
        self.max_health = health
        self.resource = endurance
        self.max_resource = self.resource
        self.strength = strength
        self.xp = xp
        self.level = level
        self.resource_gain = sacred_feathers
        self.resource_type = "Endurance"
        self.resource_gain_description = "Sacred Feather"
    def light_swing(self, target):
        if self.resource >= self.attack1_cost:
            damage = int(round(self.strength * (random.uniform(0.75, 1.25))))
            target.health -= damage
            self.resource -= self.attack1_cost
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack1} dealing {damage} damage.".center(100))
                print(BORDER)
                print(f"{target.name} has perished.".center(100))
                print(BORDER)
                return
            else:
                print(BORDER)
                print(f"{self.name} uses {self.attack1} dealing {damage} damage. {target.name}'s health is now {target.health}.".center(100))
                print(BORDER)
                return
        else:
            print(BORDER)
            print(f"{self.name} doesn't have enough {self.resource}. Use a {self.resource_gain_description}? (y/n)".center(100))
            selection = input()
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)")
                selection = input()
            if selection == "y":
                self.resource += 50
                print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(100))
                print(BORDER)
            else:
                print(BORDER)
                print(f"Not enough {self.resource_type}. Skipping turn".center(100))
    def heavy_swing(self, target):
        if self.resource >= self.attack2_cost:
            damage = int(round(self.strength * random.uniform(1.5, 2.0)))
            target.health -= damage
            self.resource -= self.attack2_cost
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack2} dealing {damage} damage.".center(100))
                print(BORDER)
                print(f"{target.name} has perished.".center(100))
                print(BORDER)
                return
            else:
                print(BORDER)
                print(f"{self.name} uses {self.attack2} dealing {damage} damage. {target.name}'s health is now {target.health}.".center(100))
                print(BORDER)
                return
        else:
            print(BORDER)
            print(f"{self.name} doesn't have enough {self.resource_type}. Use a {self.resource_gain_description}? (y/n)".center(100))
            selection = input()
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)")
                selection = input()
            if selection == "y":
                self.resource += 50
                print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(100))
                print(BORDER)
            else:
                print(BORDER)
                print(f"Not enough {self.resource_type}. Skipping turn".center(100))
    def meditate(self):
        if self.resource >= self.heal1_cost:
            healing_amount = int(round(self.strength * (random.uniform(0.4, 0.7))))
            self.health += healing_amount
            self.resource -= self.heal1_cost
            print(BORDER)
            print(f"{self.name} uses {self.heal1} for {healing_amount}. Health: {self.health}".center(100))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name} doesn't have enough {self.resource_type}. Use a {self.resource_gain_description}? (y/n)".center(100))
            selection = input()
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)")
                selection = input()
            if selection == "y":
                self.resource += 50
                print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(100))
                print(BORDER)
            else:
                print(BORDER)
                print(f"Not enough {self.resource_type}. Skipping turn".center(100))
    def counterattack(self, target):
            counterattacks = [self.attack1_method, self.attack2_method, self.heal1_method]
            chosen_counter = random.choice(counterattacks)
            if chosen_counter == self.attack1_method:
                if self.resource < self.attack1_cost:
                    self.resource += 50
                    print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(100))
                    print(BORDER)  
                    return
                else:
                    chosen_counter(target)
            elif chosen_counter == self.attack2_method:
                if self.resource < self.attack2_cost:
                    self.resource += 50
                    print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(100))
                    print(BORDER)  
                else:
                    chosen_counter(target)
            elif chosen_counter == self.heal1_method:
                if self.resource < self.heal1_cost:
                    self.resource += 50
                    print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(100))
                    print(BORDER)  
                else:
                    chosen_counter()
    def level_up(self):
        # Level 2
        if self.xp > 20:
            if self.level == 1:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 50")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)


        # Level 3
        if self.xp > 50:
            if self.level == 2:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 90")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
        # Level 4
        if self.xp > 90:
            if self.level == 3:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 140")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
        # Level 5
        if self.xp > 140:
            if self.level == 4:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 200")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
        # Level 6
        if self.xp > 200:
            if self.level == 5:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 270")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
        # Level 7
        if self.xp > 270:
            if self.level == 6:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 350")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
        # Level 8
        if self.xp > 350:
            if self.level == 7:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 440")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
        # Level 9
        if self.xp > 440:
            if self.level == 8:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 540")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
        # Level 10
        if self.xp > 540:
            if self.level == 9:
                self.level += 1
                print(f"{self.name} has reached MAX level {self.level}!")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
    def skill_up(self, selection):
        if selection == "Health":
            self.max_health += 25
            print(BORDER)
            print(f"Health is now {self.max_health}")
            print(BORDER)
        if selection == "Endurance":
            self.max_resource += 25
            print(BORDER)
            print(f"Endurance is now {self.max_resource}")
            print(BORDER)
        if selection == "Strength":
            self.strength += 5
            print(BORDER)
            print(f"Strength is now {self.strength}")
            print(BORDER)
        if selection == "Sacred Feathers":
            self.resource_gain += 1
            print(BORDER)
            print(f"You now have {self.resource_gain} {self.resource_gain_description}")
            print(BORDER)
class Gray_Knight(Warrior):
    def __init__(self, name, health, endurance, strength, xp, level, sacred_feathers):
        super().__init__(name, health, endurance, strength, xp, level, sacred_feathers)
        self.description = (f"{self.name}: an aged combatant wondering the lands. Searching for something.")
        self.attack1, self.attack1_description, self.attack1_combined, self.attack1_cost = "Light Swing", "deals moderate damage...", "1) Light Swing - deals moderate damage.", 5
        self.attack2, self.attack2_description, self.attack2_combined, self.attack2_cost = "Heavy Swing", "deals heavy damage...", "2) Heavy Swing - deals heavy damage.", 10
        self.heal1, self.heal1_description, self.heal1_combined, self.heal1_cost = "Bandage Wound", "restores your life...", "3) Bandage Wound - restores your life.", 10
        self.attack1_method, self.attack2_method, self.heal1_method, self.counterattack_method = self.light_swing, self.heavy_swing, self.bandage_wound, self.counterattack
        self.stats = ["Health", "Endurance", "Strength", "Sacred Feathers"]
        self.attacks = [self.attack1_combined, self.attack2_combined, self.heal1_combined]
    def light_swing(self, target):
        if self.resource >= self.attack1_cost:
            damage = int(round(self.strength * (random.uniform(1.0, 2.0))))
            target.health -= damage
            self.resource -= self.attack1_cost
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack1} dealing {damage} damage.".center(100))
                print(BORDER)
                print(f"{target.name} has perished.".center(100))
                print(BORDER)
                return
            else:
                print(BORDER)
                print(f"{self.name} uses {self.attack1} dealing {damage} damage. {target.name}'s health is now {target.health}.".center(100))
                print(BORDER)
                return
        else:
            print(BORDER)
            print(f"{self.name} doesn't have enough {self.resource_type}. Use a {self.resource_gain_description}? (y/n)".center(100))
            selection = input()
            print(BORDER)
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)".center(100))
                selection = input()
            if selection == "y":
                if self.resource_gain > 0:
                    self.resource += 50
                    self.resource_gain -= 1
                    print(f"{self.name} consumed a {self.resource_gain}. {self.resource_type}: {self.resource}. {self.resource_gain} {self.resource_type} remaining".center(100))
                    print(BORDER)
                else:
                    print(BORDER)
                    print(f"No {self.resource_type}'s left. Good luck!".center(100))
            else:
                print(BORDER)
                print("Not enough mana. Skipping turn".center(100))
    def heavy_swing(self, target):
        if self.resource >= self.attack2_cost:
            damage = int(round(self.strength * (random.uniform(2.0, 3.0))))
            target.health -= damage
            self.resource -= self.attack2_cost
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack2} dealing {damage} damage.".center(100))
                print(BORDER)
                print(f"{target.name} has perished.".center(100))
                print(BORDER)
                return
            else:
                print(BORDER)
                print(f"{self.name} uses {self.attack2} dealing {damage} damage. {target.name}'s health is now {target.health}.".center(100))
                print(BORDER)
                return
        else:
            print(BORDER)
            print(f"{self.name} doesn't have enough {self.resource_type}. Use a {self.resource_gain_description}? (y/n)".center(100))
            selection = input()
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)".center(100))
                selection = input()
            if selection == "y":
                if self.resource_gain > 0:
                    self.resource_gain -= 1
                    self.resource += 50
                    print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}. {self.resource_gain} {self.resource_gain_description}'s remaining.".center(100))
                    print(BORDER)
                else:
                    print(BORDER)
                    print(f"No {self.resource_gain_description}'s left. Good luck!".center(100))
            else:
                print(BORDER)
                print(f"Not enough {self.resource_type}. Skipping turn".center(100))
    def bandage_wound(self):
        if self.resource >= 20:
            healing_amount = int(round(self.strength * (random.uniform(1.0, 1.3))))
            self.health += healing_amount
            self.resource -= self.heal1_cost
            print(BORDER)
            print(f"{self.name} uses {self.heal1} for {healing_amount}. Health: {self.health}".center(100))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name} doesn't have enough {self.resource_type}. Use a {self.resource_gain}? (y/n)".center(100))
            selection = input()
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)".center(100))
                selection = input()
            if selection == "y":
                if self.resource_gain > 0:
                    self.resource_gain -= 1
                    self.resource += 50
                    print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}. {self.resource_gain} {self.resource_gain_description}'s remaining.".center(100))
                    print(BORDER)
                else:
                    print(BORDER)
                    print(f"No {self.resource_type} left. Good luck!".center(100))
            else:
                print(BORDER)
                print(f"Not enough {self.resource_type}. Skipping turn".center(100))
    def counterattack(self, target):
            counterattacks = [self.attack1_method, self.attack2_method, self.heal1_method]
            chosen_counter = random.choice(counterattacks)
            if chosen_counter == self.heal1_method:
                if self.resource < 20:
                    if self.resource_gain > 0:
                        self.resource += 50
                        print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(100))
                        print(BORDER)  
                        return
                    else:
                        print(BORDER)
                        print(f"{self.name} has no {self.resource_gain_description}'s left. Push the attack!".center(100))
                else:
                    chosen_counter()
            elif chosen_counter == self.attack1_method:
                if self.resource < 15:
                    if self.resource_gain > 0:
                        self.resource += 50
                        print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(100))
                        print(BORDER)
                        return
                    else:
                        print(BORDER)
                        print(f"{self.name} has no {self.resource_gain_description}'s left. Push the attack!".center(100))  
                else:
                    chosen_counter(target)
            elif chosen_counter == self.attack2_method:
                if self.resource < 25:
                    if self.resource_gain > 0:
                        self.resource += 50
                        print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(100))
                        print(BORDER)
                    else:
                        print(BORDER)
                        print(f"{self.name} has no {self.resource_gain_description}'s left. Push the attack!".center(100))  
                else:
                    chosen_counter(target)
    def level_up(self):
        # Level 2
        if self.xp > 20:
            if self.level == 1:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 50")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)                

        # Level 3
        if self.xp > 50:
            if self.level == 2:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 90")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
        # Level 4
        if self.xp > 90:
            if self.level == 3:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 140")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
        # Level 5
        if self.xp > 140:
            if self.level == 4:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 200")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
        # Level 6
        if self.xp > 200:
            if self.level == 5:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 270")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
        # Level 7
        if self.xp > 270:
            if self.level == 6:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 350")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
        # Level 8
        if self.xp > 350:
            if self.level == 7:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 440")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
        # Level 9
        if self.xp > 440:
            if self.level == 8:
                self.level += 1
                print(f"{self.name} reached level {self.level}. Total XP - {self.xp} / 540")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
        # Level 10
        if self.xp > 540:
            if self.level == 9:
                self.level += 1
                print(f"{self.name} has reached MAX level {self.level}!")
                print(BORDER)
                for stat in self.stats:
                    print(stat)
                selection = input("Which stat would you like to upgrade?")
                while selection not in [stat for stat in self.stats]:
                    print("Unrecognized answer. Please choose from the list above.")
                    print("\n")
                    selection = input()
                self.skill_up(selection)
    def skill_up(self, selection):
        if selection == "Health":
            self.max_health += 25
            print(BORDER)
            print(f"Health is now {self.max_health}")
            print(BORDER)
        if selection == "Endurance":
            self.max_resource += 25
            print(BORDER)
            print(f"Endurance is now {self.max_resource}")
            print(BORDER)
        if selection == "Strength":
            self.strength += 5
            print(BORDER)
            print(f"Strength is now {self.strength}")
            print(BORDER)
        if selection == "Sacred Feathers":
            self.resource_gain += 1
            print(BORDER)
            print(f"You now have {self.resource_gain} {self.resource_gain_description}")
            print(BORDER)