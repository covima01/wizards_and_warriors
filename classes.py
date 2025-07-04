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
                print(f"{self.name} uses {self.attack1} dealing {damage} damage.".center(70))
                print(BORDER)
                print(f"{self.name} is victorious, {target.name} has perished in battle.".center(70))
                print(BORDER)
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
            print(BORDER)
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
        if self.resource >= self.attack2_cost:
            damage = int(round(self.intelligence * (random.uniform(2.0, 3.0))))
            target.health -= damage
            self.resource -= self.attack2_cost
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack2} dealing {damage} damage.".center(70))
                print(BORDER)
                print(f"{self.name} is victorious, {target.name} has perished in battle.".center(70))
                print(BORDER)
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
            self.resource -= self.heal1_cost
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
        self.description = (f"{self.name}: a mysterious caster. Removed from Astern Academy for reasons unknown.")
        self.attack1, self.attack1_description, self.attack1_combined, self.attack1_cost = "Shock", "electrocutes your enemy...", "1) Shock - electrocutes your enemy.", 5
        self.attack2, self.attack2_description, self.attack2_combined, self.attack2_cost = "Combust", "engulfs your target in flame...", "2) Combust - engulds your target in flame.", 10
        self.heal1, self.heal1_description, self.heal1_combined, self.heal1_cost = "Regen", "restores your life...", "3) Regen - restores your life.", 10
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
                print(f"{self.name} uses {self.attack1} dealing {damage} damage.".center(70))
                print(BORDER)
                print(f"{self.name} is victorious, {target.name} has perished in battle.".center(70))
                print(BORDER)               
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
            print(BORDER)
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)".center(70))
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
    def combust(self, target):
        if self.resource >= self.attack2_cost:
            damage = int(round(self.intelligence * (random.uniform(2.0, 3.0))))
            target.health -= damage
            self.resource -= self.attack2_cost
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack2} dealing {damage} damage.".center(70))
                print(BORDER)
                print(f"{self.name} is victorious, {target.name} has perished in battle.".center(70))
                print(BORDER)
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
    def regen(self):
        if self.resource >= 20:
            healing_amount = int(round(self.intelligence * (random.uniform(1.0, 1.3))))
            self.health += healing_amount
            self.resource -= self.heal1_cost
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

class Flame_Walker(Wizard):
    def __init__(self, name, health, mana, intelligence, xp, level, potions):
        super().__init__(name, health, mana, intelligence, xp, level, potions)
        self.description = (f"{self.name}: a mysterious flame walker from the southern desert of Astanir. Nobody knows how old he is.")
        self.attack1, self.attack1_description, self.attack1_combined, self.attack1_cost = "Fireball", "deals moderate fire damage...", "1) Fireball - deals moderate fire damage.", 5
        self.attack2, self.attack2_description, self.attack2_combined, self.attack2_cost = "Meteor Rain", "deals heave fire damage...", "2) Meteor Rain - deals heavy fire damage.", 10
        self.heal1, self.heal1_description, self.heal1_combined, self.heal1_cost = "Consume Flame", "restores a moderate amount of health...", "3) Consume Flame - restores a moderate amount of health.", 10
        self.attack1_method, self.attack2_method, self.heal1_method, self.counterattack_method = self.fireball, self.meteor_rain, self.consume_flame, self.counterattack
        self.stats = ["Health", "Mana", "Intelligence", "Potions"]
        self.attacks = [self.attack1_combined, self.attack2_combined, self.heal1_combined]
    def fireball(self, target):
        if self.resource >= self.attack1_cost:
            damage = int(round(self.intelligence * (random.uniform(1.0, 2.0))))
            target.health -= damage
            self.resource -= self.attack1_cost
            if target.health <= 0:               
                print(BORDER)
                print(f"{self.name} uses {self.attack1} dealing {damage} damage.".center(70))
                print(BORDER)
                print(f"{self.name} is victorious, {target.name} has perished in battle.".center(70))
                print(BORDER)               
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
            print(BORDER)
            while selection != "y" and selection != "n":
                print("Unrecognized selection. Please enter y (yes) or n (no)".center(70))
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
    def meteor_rain(self, target):
        if self.resource >= self.attack2_cost:
            damage = int(round(self.intelligence * (random.uniform(2.0, 3.0))))
            target.health -= damage
            self.resource -= self.attack2_cost
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack2} dealing {damage} damage.".center(70))
                print(BORDER)
                print(f"{self.name} is victorious, {target.name} has perished in battle.".center(70))
                print(BORDER)
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
    def consume_flame(self):
        if self.resource >= 20:
            healing_amount = int(round(self.intelligence * (random.uniform(1.0, 1.3))))
            self.health += healing_amount
            self.resource -= self.heal1_cost
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
class Frozen_Sorcerer(Wizard):
    def __init__(self, name, health, mana, intelligence, xp, level, potions):
        super().__init__(name, health, mana, intelligence, xp, level, potions)
        self.description = (f"{self.name}: frost mage, and quick witted advisor to the king of Parth. Wise and dangerous.")
        self.attack1, self.attack1_description, self.attack1_combined, self.attack1_cost = "Ice Needle", "deals moderate ice damage...", "1) Ice Needle - deals moderate ice damage.", 5
        self.attack2, self.attack2_description, self.attack2_combined, self.attack2_cost = "Iceberg Down", "deals heavy ice damage...", "2) Iceberg Down - deals heavy ice damage", 10
        self.heal1, self.heal1_description, self.heal1_combined, self.heal1_cost = "Frozen Hibernation", "restores a moderate amount of health...", "3) Frozen Hibernation - restores a moderate amount of health.", 10
        self.attack1_method, self.attack2_method, self.heal1_method, self.counterattack_method = self.ice_needle, self.iceberg_down, self.frozen_hibernation, self.counterattack
        self.stats = ["Health", "Mana", "Intelligence", "Potions"]
        self.attacks = [self.attack1_combined, self.attack2_combined, self.heal1_combined]
    def ice_needle(self, target):
        if self.resource >= self.attack1_cost:
            damage = int(round(self.intelligence * (random.uniform(1.0, 2.0))))
            target.health -= damage
            self.resource -= self.attack1_cost
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack1} dealing {damage} damage.".center(70))
                print(BORDER)
                print(f"{self.name} is victorious, {target.name} has perished in battle.".center(70))
                print(BORDER)
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
            print(BORDER)
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
    def iceberg_down(self, target):
        if self.resource >= self.attack2_cost:
            damage = int(round(self.intelligence * (random.uniform(2.0, 3.0))))
            target.health -= damage
            self.resource -= self.attack2_cost
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack2} dealing {damage} damage.".center(70))
                print(BORDER)
                print(f"{self.name} is victorious, {target.name} has perished in battle.".center(70))
                print(BORDER)
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
    def frozen_hibernation(self):
        if self.resource >= 20:
            healing_amount = int(round(self.intelligence * (random.uniform(1.0, 1.3))))
            self.health += healing_amount
            self.resource -= self.heal1_cost
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
class Storm_Mage(Wizard):
    def __init__(self, name, health, mana, intelligence, xp, level, potions):
        super().__init__(name, health, mana, intelligence, xp, level, potions)
        self.description = (f"{self.name}: a reckless storm mage from the Enigma Isles. Once a hero, now an outcast.")
        self.attack1, self.attack1_description, self.attack1_combined, self.attack1_cost = "Lightning", "deals moderate lightning damage...", "1) Lightning - deals moderate lightning damage.", 5
        self.attack2, self.attack2_description, self.attack2_combined, self.attack2_cost = "Grand Tempest", "deals heavy lightning damage...", "2) Grand Temptest - deals heavy lightning damage.", 10
        self.heal1, self.heal1_description, self.heal1_combined, self.heal1_cost = "Life Shock", "restores a moderate amount of health...", "3) Life Shock - restores a moderate amount of health.", 10
        self.attack1_method, self.attack2_method, self.heal1_method, self.counterattack_method = self.lightning, self.grand_tempest, self.life_shock, self.counterattack
        self.stats = ["Health", "Mana", "Intelligence", "Potions"]
        self.attacks = [self.attack1_combined, self.attack2_combined, self.heal1_combined]
    def lightning(self, target):
        if self.resource >= self.attack1_cost:
            damage = int(round(self.intelligence * (random.uniform(1.0, 2.0))))
            target.health -= damage
            self.resource -= self.attack1_cost
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack1} dealing {damage} damage.".center(70))
                print(BORDER)
                print(f"{self.name} is victorious, {target.name} has perished in battle.".center(70))
                print(BORDER)
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
            print(BORDER)
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
    def grand_tempest(self, target):
        if self.resource >= self.attack2_cost:
            damage = int(round(self.intelligence * (random.uniform(2.0, 3.0))))
            target.health -= damage
            self.resource -= self.attack2_cost
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack2} dealing {damage} damage.".center(70))
                print(BORDER)
                print(f"{self.name} is victorious, {target.name} has perished in battle.".center(70))
                print(BORDER)
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
    def life_shock(self):
        if self.resource >= 20:
            healing_amount = int(round(self.intelligence * (random.uniform(1.0, 1.3))))
            self.health += healing_amount
            self.resource -= self.heal1_cost
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
        self.attack1 = "Light Swing"
        self.attack1_description = "deals moderate physical damage..."
        self.attack1_cost = 5
        self.attack2 = "Heavy Swing"
        self.attack2_description = "deals heavy physical damage..."
        self.attack2_cost = 10
        self.heal1 = "Meditate"
        self.heal1_description = "restores a moderate amount of health..."
        self.heal1_cost = 10
        self.attack1_method = self.light_swing        
        self.attack2_method = self.heavy_swing
        self.heal1_method = self.meditate
        self.stats = ["Health", "Endurance", "Strength", "Sacred Feathers"]
        self.attacks = [self.attack1, self.attack2, self.heal1]
    def light_swing(self, target):
        if self.resource >= self.attack1_cost:
            damage = int(round(self.strength * (random.uniform(0.75, 1.25))))
            target.health -= damage
            self.resource -= self.attack1_cost
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack1} dealing {damage} damage.".center(70))
                print(BORDER)
                print(f"{self.name} is victorious, {target.name} has perished in battle.\n".center(70))
                print(BORDER)
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
        if self.resource >= self.attack2_cost:
            damage = int(round(self.strength * random.uniform(1.5, 2.0)))
            target.health -= damage
            self.resource -= self.attack2_cost
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack2} dealing {damage} damage.".center(70))
                print(BORDER)
                print(f"{self.name} is victorious, {target.name} has perished in battle.\n".center(70))
                print(BORDER)
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
        if self.resource >= self.heal1_cost:
            healing_amount = int(round(self.strength * (random.uniform(0.4, 0.7))))
            self.health += healing_amount
            self.resource -= self.heal1_cost
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
                if self.resource < self.attack1_cost:
                    self.resource += 50
                    print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(70))
                    print(BORDER)  
                    return
                else:
                    chosen_counter(target)
            elif chosen_counter == self.attack2_method:
                if self.resource < self.attack2_cost:
                    self.resource += 50
                    print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(70))
                    print(BORDER)  
                else:
                    chosen_counter(target)
            elif chosen_counter == self.heal1_method:
                if self.resource < self.heal1_cost:
                    self.resource += 50
                    print(f"{self.name} consumed a {self.resource_gain_description}. {self.resource_type}: {self.resource}".center(70))
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
        self.attack1, self.attack1_description, self.attack1_combined, self.attack1_cost = "Strike", "a precise assult on your target...", "1) Strike - a precise assault on your target.", 5
        self.attack2, self.attack2_description, self.attack2_combined, self.attack2_cost = "Blunt Trauma", "a relentless attack on your enemy...", "2) Blunt Trauma - a relentless attack on your enemy.", 10
        self.heal1, self.heal1_description, self.heal1_combined, self.heal1_cost = "Reprieve", "restores your life...", "3) Reprieve - restores your life.", 10
        self.attack1_method, self.attack2_method, self.heal1_method, self.coutnerattack = self.strike, self.blunt_trauma, self.reprieve, self.counterattack
        self.stats = ["Health", "Endurance", "Strength", "Sacred Feathers"]
        self.attacks = [self.attack1_combined, self.attack2_combined, self.heal1_combined]
    def strike(self, target):
        if self.resource >= self.attack1_cost:
            damage = int(round(self.strength * (random.uniform(1.0, 2.0))))
            target.health -= damage
            self.resource -= self.attack1_cost
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack1} dealing {damage} damage.".center(70))
                print(BORDER)
                print(f"{self.name} is victorious, {target.name} has perished in battle.".center(70))
                print(BORDER)
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
            print(BORDER)
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
    def blunt_trauma(self, target):
        if self.resource >= self.attack2_cost:
            damage = int(round(self.strength * (random.uniform(2.0, 3.0))))
            target.health -= damage
            self.resource -= self.attack2_cost
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack2} dealing {damage} damage.".center(70))
                print(BORDER)
                print(f"{self.name} is victorious, {target.name} has perished in battle.".center(70))
                print(BORDER)
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
    def reprieve(self):
        if self.resource >= 20:
            healing_amount = int(round(self.strength * (random.uniform(1.0, 1.3))))
            self.health += healing_amount
            self.resource -= self.heal1_cost
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

class Berserker(Warrior):
    def __init__(self, name, health, endurance, strength, xp, level, sacred_feathers):
        super().__init__(name, health, endurance, strength, xp, level, sacred_feathers)
        self.description = (f"{self.name}: berserker warchief of the Chok'ele tribe. Unbeaten in battle.")
        self.attack1, self.attack1_description, self.attack1_combined, self.attack1_cost = "Impale", "deals moderate physical damage...", "1) Imaple - deals moderate physical damage.", 5
        self.attack2, self.attack2_description, self.attack2_combined, self.attack2_cost = "Whirlwind", "deals heavy physical damage...", "2) Whirlwind - deals heavy physical damage.", 10
        self.heal1, self.heal1_description, self.heal1_combined, self.heal1_cost = "Tireless Rage", "restores a moderate amoutn of health...", "3) Tireless Rage - restores a moderate amount of heal.", 10
        self.attack1_method, self.attack2_method, self.heal1_method, self.coutnerattack = self.impale, self.whirlwind, self.tireless_rage, self.counterattack
        self.stats = ["Health", "Endurance", "Strength", "Sacred Feathers"]
        self.attacks = [self.attack1_combined, self.attack2_combined, self.heal1_combined]
    def impale(self, target):
        if self.resource >= self.attack1_cost:
            damage = int(round(self.strength * (random.uniform(1.0, 2.0))))
            target.health -= damage
            self.resource -= self.attack1_cost
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack1} dealing {damage} damage.".center(70))
                print(BORDER)
                print(f"{self.name} is victorious, {target.name} has perished in battle.".center(70))
                print(BORDER)
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
            print(BORDER)
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
    def whirlwind(self, target):
        if self.resource >= self.attack2_cost:
            damage = int(round(self.strength * (random.uniform(2.0, 3.0))))
            target.health -= damage
            self.resource -= self.attack2_cost
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack2} dealing {damage} damage.".center(70))
                print(BORDER)
                print(f"{self.name} is victorious, {target.name} has perished in battle.".center(70))
                print(BORDER)
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
    def tireless_rage(self):
        if self.resource >= 20:
            healing_amount = int(round(self.strength * (random.uniform(1.0, 1.3))))
            self.health += healing_amount
            self.resource -= self.heal1_cost
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
class Paladin(Warrior):
    def __init__(self, name, health, endurance, strength, xp, level, sacred_feathers):
        super().__init__(name, health, endurance, strength, xp, level, sacred_feathers)
        self.description = (f"{self.name}: first paladin of the royal guard. Honorable and reliable.")
        self.attack1, self.attack1_description, self.attack1_combined, self.attack1_cost = "Righteous Swing", "deals moderate holy and physical damage...", "1) Righteous Swing - deals moderate holy and physical damage.", 5
        self.attack2, self.attack2_description, self.attack2_combined, self.attack2_cost = "Exercise Demons", "deals heavy holy damage...", "2) Exercise Demons - deals heavy holy damage.", 10
        self.heal1, self.heal1_description, self.heal1_combined, self.heal1_cost = "Holy Regeneration", "restores a moderate amount of health...", "3) Holy Regeneration - restores a moderate amoutn of health", 10
        self.attack1_method, self.attack2_method, self.heal1_method, self.counterattack_method = self.righteous_swing, self.exercise_demons, self.holy_regeneration, self.counterattack
        self.stats = ["Health", "Endurance", "Strength", "Sacred Feathers"]
        self.attacks = [self.attack1_combined, self.attack2_combined, self.heal1_combined]
    def righteous_swing(self, target):
        if self.resource >= self.attack1_cost:
            damage = int(round(self.strength * (random.uniform(1.0, 2.0))))
            target.health -= damage
            self.resource -= self.attack1_cost
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack1} dealing {damage} damage.".center(70))
                print(BORDER)
                print(f"{self.name} is victorious, {target.name} has perished in battle.".center(70))
                print(BORDER)
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
            print(BORDER)
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
    def exercise_demons(self, target):
        if self.resource >= self.attack2_cost:
            damage = int(round(self.strength * (random.uniform(2.0, 3.0))))
            target.health -= damage
            self.resource -= self.attack2_cost
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack2} dealing {damage} damage.".center(70))
                print(BORDER)
                print(f"{self.name} is victorious, {target.name} has perished in battle.".center(70))
                print(BORDER)
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
    def holy_regeneration(self):
        if self.resource >= 20:
            healing_amount = int(round(self.strength * (random.uniform(1.0, 1.3))))
            self.health += healing_amount
            self.resource -= self.heal1_cost
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
class Sellsword(Warrior):
    def __init__(self, name, health, endurance, strength, xp, level, sacred_feathers):
        super().__init__(name, health, endurance, strength, xp, level, sacred_feathers)
        self.description = (f"{self.name}: a former knight turned sellsword. Abandoned his unit in the Battle of the Bends.")
        self.attack1, self.attack1_description, self.attack1_combined, self.attack1_cost = "Quick Slash", "deals moderate phyiscal damage...", "1) Quick Slash - deals moderate physical damage.", 5
        self.attack2, self.attack2_description, self.attack2_combined, self.attack2_cost = "Twin Slice", "deals heavy phyiscal damage...", "2) Twin Slice - deals heavy physical damage...", 10
        self.heal1, self.heal1_description, self.heal1_combined, self.heal1_cost = "Bandage Wound", "restores a moderate amount of health...", "3) Banage Wound - restores a moderate amount of health.", 10
        self.attack1_method, self.attack2_method, self.heal1_method, self.counterattack_method = self.quick_slash, self.twin_slice, self.bandage_wound, self.counterattack
        self.stats = ["Health", "Endurance", "Strength", "Sacred Feathers"]
        self.attacks = [self.attack1_combined, self.attack2_combined, self.heal1_combined]
    def quick_slash(self, target):
        if self.resource >= self.attack1_cost:
            damage = int(round(self.strength * (random.uniform(1.0, 2.0))))
            target.health -= damage
            self.resource -= self.attack1_cost
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name} uses {self.attack1} dealing {damage} damage.".center(70))
                print(BORDER)
                print(f"{self.name} is victorious, {target.name} has perished in battle.".center(70))
                print(BORDER)
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
            print(BORDER)
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
    def twin_slice(self, target):
        for i in range(0,2):
            if self.resource >= self.attack2_cost:
                damage = int(round(self.strength * (random.uniform(0.75, 1.25))))
                target.health -= damage
                self.resource -= self.attack2_cost
                if target.health <= 0:
                    print(BORDER)
                    print(f"{self.name} uses {self.attack2} dealing {damage} damage.".center(70))
                    print(BORDER)
                    print(f"{self.name} is victorious, {target.name} has perished in battle.".center(70))
                    print(BORDER)
                    return
                else:
                    print(BORDER)
                    print(f"{self.name} uses {self.attack2} dealing {damage} damage. {target.name}'s health is now {target.health}.".center(70))
                    print(BORDER)
                    i += 1
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
                        return
                else:
                    print(BORDER)
                    print(f"Not enough {self.resource_type}. Skipping turn".center(70))
                    return
    def bandage_wound(self):
        if self.resource >= 20:
            healing_amount = int(round(self.strength * (random.uniform(1.0, 1.3))))
            self.health += healing_amount
            self.resource -= self.heal1_cost
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