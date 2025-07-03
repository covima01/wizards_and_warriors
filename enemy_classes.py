import random
from constants import BORDER



class Monster:
    def __init__(self, name, health, strength, intelligence, level, xp):
        self.name = name
        self.level = level
        self.health = health + (self.level * 10)
        self.strength = strength + (self.level * 10)
        self.intelligence = intelligence + (self.level * 10)
        self.xp = xp
class Goblin(Monster):
    def __init__(self, name, health, strength, intelligence, level, xp):
        super().__init__(name, health, strength,intelligence, level, xp)
        self.attack1 = "Backstab"
        self.attack1_method = self.backstab
        self.attack2 = "Double Shot"
        self.attack2_method = self.double_shot
        self.heal1 = "Healing Dust"
        self.heal1_method = self.healing_dust
    def backstab(self, target):
        damage = int(round(self.strength * (random.uniform(0.25, 0.5))))
        target.health -= damage
        if target.health <=0:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage}. {target.name} has perished.".center(70))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage} damage. {target.name}'s health is now {target.health}".center(70))
            print(BORDER)
    def double_shot(self, target):
        damage = int(round(self.strength * (random.uniform(0.15, 0.25))))
        target.health -= damage
        if target.health <= 0:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.")
        elif target.health >= 0:
            target.health -= damage
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.")
            else:
                print(BORDER)
                print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name}'s health is now {target.health}.")
                print(BORDER)
    def healing_dust(self):
            healing_amount = int(self.health * 0.15)
            self.health += healing_amount
            print(BORDER)
            print(f"{self.name} uses {self.heal1} for {healing_amount}. Health: {self.health}".center(70))
            print(BORDER)
    def counterattack(self, target):
            counterattacks = [self.attack1_method, self.attack2_method, self.heal1_method]
            chosen_counter = random.choice(counterattacks)
            attack = random.randint(0,8)
            if attack <= 7:
                if self.health > 0:
                    if chosen_counter == self.heal1_method:
                        chosen_counter()
                    else:
                        chosen_counter(target)
            else:
                print(BORDER)
                print(f"{self.name} missed.")
                print(BORDER)
    @staticmethod
    def create_goblin_trickster():
        return Goblin("Goblin Trickster", 20, 10, 10, 1, 5 )
    @staticmethod
    def create_goblin_bully():
        return Goblin("Goblin Bully", 30, 12, 10, 1, 10)
    @staticmethod
    def create_goblin_fat_cat():
        return Goblin("Goblin Fat-Cat", 100, 7, 5, 1, 15)
class Harpy(Monster):
    def __init__(self, name, health, strength, intelligence, level, xp):
        super().__init__(name, health, strength, intelligence, level, xp)
        self.attack1 = "Swooping Claw"
        self.attack1_method = self.swooping_claw
        self.attack2 = "Siren Song"
        self.attack2_method = self.siren_song
        self.heal1 = "Rejuvinating Cry"
        self.heal1_method = self.rejuvinating_cry
    def swooping_claw(self, target):
        damage = int(round(self.strength * (random.uniform(0.25, 0.5))))
        target.health -= damage
        if target.health <=0:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage}. {target.name} has perished.".center(70))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage} damage. {target.name}'s health is now {target.health}".center(70))
            print(BORDER)
    def siren_song(self, target):
        damage = int(round(self.intelligence * (random.uniform(0.15, 0.25))))
        target.health -= damage
        if target.health <= 0:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.")
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name}'s health is now {target.health}.")
            print(BORDER)
    def rejuvinating_cry(self):
            healing_amount = int(self.health * 0.15)
            self.health += healing_amount
            print(BORDER)
            print(f"{self.name} uses {self.heal1} for {healing_amount}. Health: {self.health}".center(70))
            print(BORDER)
    def counterattack(self, target):
            counterattacks = [self.attack1_method, self.attack2_method, self.heal1_method]
            chosen_counter = random.choice(counterattacks)
            attack = random.randint(0,8)
            if attack <= 7:
                if self.health > 0:
                    if chosen_counter == self.heal1_method:
                        chosen_counter()
                    else:
                        chosen_counter(target)
            else:
                print(BORDER)
                print(f"{self.name} missed.")
                print(BORDER)
    @staticmethod
    def create_harpy_huntress():
        return Harpy("Harpy Huntress", 30, 9, 11, 1, 5)
    @staticmethod
    def create_harpy_terror():
        return Harpy("Harpy Terror", 45, 11, 13, 1, 10)
    @staticmethod
    def create_harpy_matriarch():
        return Harpy("Harpy Matriarch", 80, 13, 15, 1, 15)
class Orc(Monster):
    def __init__(self, name, health, strength, intelligence, level, xp):
        super().__init__(name, health, strength, intelligence, level, xp)
        self.attack1 = "Cleave"
        self.attack1_method = self.cleave
        self.attack2 = "Devastating Strike"
        self.attack2_method = self.devastating_strike
        self.heal1 = "Bloodlust"
        self.heal1_method = self.bloodlust
    def cleave(self, target):
        damage = int(round(self.strength * (random.uniform(0.25, 0.5))))
        target.health -= damage
        if target.health <=0:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage}. {target.name} has perished.".center(70))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage} damage. {target.name}'s health is now {target.health}".center(70))
            print(BORDER)
    def devastating_strike(self, target):
        damage = int(round(self.strength * (random.uniform(0.30, 0.60))))
        target.health -= damage
        if target.health <= 0:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.")
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name}'s health is now {target.health}.")
            print(BORDER)
    def bloodlust(self):
            self.strength = int(self.strength * 1.5)
            print(f"{self.name}'s strength has increased to {self.strength}.")
    def counterattack(self, target):
            counterattacks = [self.attack1_method, self.attack2_method, self.heal1_method]
            chosen_counter = random.choice(counterattacks)
            attack = random.randint(0,8)
            if attack <= 7:
                if self.health > 0:
                    if chosen_counter == self.heal1_method:
                        chosen_counter()
                    else:
                        chosen_counter(target)
            else:
                print(BORDER)
                print(f"{self.name} missed.")
                print(BORDER)
    @staticmethod
    def create_orc_warrior():
        return Orc("Orc Warrior", 50, 12, 6, 1, 10)
    @staticmethod
    def create_orc_captain():
        return Orc("Orc Captain", 75, 15, 7, 1, 20)
    @staticmethod
    def create_orc_warmonger():
        return Orc("Orc Warmonger", 120, 17, 8, 1, 35)
class Ogre:
    def __init__(self, name, health, strength, xp):
        self.name = name
        self.health = health
        self.strength = strength
        self.xp = xp
    def overhead_smash(self, target):
        damage = int(round(self.strength * (random.uniform(0.25, 0.5))))
        target.health -= damage
        if target.health <=0:
            print(BORDER)
            print(f"{self.name}'s overhead smash deals {damage}. {target.name} has perished.".center(70))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name}'s overhead smash deals {damage} damage. {target.name}'s health is now {target.health}".center(70))
            print(BORDER)
    def grip_of_death(self, target):
        damage = int(round(self.strength * (random.uniform(0.5, 1.0))))
        target.health -= damage
        if target.health <= 0:
            print(BORDER)
            print(f"{self.name}'s grip of death deals {damage}. {target.name} has perished.".center(70))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name}'s grip of death deals {damage} damage. {target.name}'s health is now {target.health}".center(70))
            print(BORDER)
    def counterattack(self, target):
            counterattacks = [self.overhead_smash, self.grip_of_death]
            chosen_counter = random.choice(counterattacks)
            attack = random.randint(0,8)
            if attack <= 7:
                if self.health > 0:
                    chosen_counter(target)
            else:
                print(BORDER)
                print(f"{self.name} missed.")
                print(BORDER)
    @staticmethod
    def create_ogre_grunt():
        return Ogre("Ogre Grunt", 25, 12, 5)
    @staticmethod
    def create_ogre_general():
        return Ogre("Ogre General", 50, 18, 10)
    @staticmethod
    def create_ogre_warlord():
        return Ogre("Ogre Warlord", 75, 20, 15)




