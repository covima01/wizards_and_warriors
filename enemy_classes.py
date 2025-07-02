import random
from constants import BORDER


class Monster:
    def __init__(self, name, health, strength, intelligence, level, xp)
        self.name = name
        self.level = level
        self.health = health + (self.level * 10)
        self.strength = strength + (self.level * 10)
        self.intelligence = intelligence + (self.level * 10)
        self.xp = xp
class Goblin(Monster):
    def __init__(self, name, health, strength, intelligence, xp)
        super().__init__(name, health, intelligence, level, xp)
        self.attack1 = self.backstab
        self.attack2 = self.double_shot
        self.heal1 = self.healing_dust
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
    def healing_dust(self)
            healing_amount = self.health * 0.15
            self.health += healing_amount
            print(BORDER)
            print(f"{self.name} uses {self.heal1} for {healing_amount}. Health: {self.health}".center(70))
            print(BORDER)
    def counterattack(self, target):
            counterattacks = [self.attack1, self.attack2, self.heal1]
            chosen_counter = random.choice(counterattacks)
            attack = random.randint(0,8)
            if attack <= 7:
                if self.health > 0:
                    chosen_counter(target)
            else:
                print(BORDER)
                print(f"{self.name} missed.")
                print(BORDER)
class Harpy(Monster):
    def __init__(self, name, health, strength, intelligence, xp)
        super().__init__(name, health, intelligence, level, xp)
        self.attack1 = self.swooping_claw
        self.attack1 = self.siren_song
        self.heal1 = self.rejuvinating_cry
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
    def rejuvinating_cry(self)
            healing_amount = self.health * 0.15
            self.health += healing_amount
            print(BORDER)
            print(f"{self.name} uses {self.heal1} for {healing_amount}. Health: {self.health}".center(70))
            print(BORDER)
    def counterattack(self, target):
            counterattacks = [self.attack1, self.attack2, self.heal1]
            chosen_counter = random.choice(counterattacks)
            attack = random.randint(0,8)
            if attack <= 7:
                if self.health > 0:
                    chosen_counter(target)
            else:
                print(BORDER)
                print(f"{self.name} missed.")
                print(BORDER)
class Orc(Monster):
        def __init__(self, name, health, strength, intelligence, xp)
        super().__init__(name, health, intelligence, level, xp)
            self.attack1 = self.cleave
            self.attack1 = self.devastating_strike
            self.heal1 = self.bloodlust
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
    def bloodlust(self)
            self.strength = self.strength * 1.5
            print(f"{self.name}'s strength has increased to {self.strength}.")
    def counterattack(self, target):
            counterattacks = [self.attack1, self.attack2, self.heal1]
            chosen_counter = random.choice(counterattacks)
            attack = random.randint(0,8)
            if attack <= 7:
                if self.health > 0:
                    chosen_counter(target)
            else:
                print(BORDER)
                print(f"{self.name} missed.")
                print(BORDER)

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




