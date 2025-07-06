import random
from constants import BORDER
# Bosses
class Boss:
    def __init__(self, name, health, armor, strength, intelligence, level, xp):
        self.name = name
        self.level = level
        self.health = health + (self.level * 10)
        self.strength = strength + (self.level * 10)
        self.armor = armor
        self.intelligence = intelligence + (self.level * 10)
        self.xp = xp
class Giant_Ogre(Boss):
    def __init__(self, name, health, armor, strength, intelligence, level, xp):
        super().__init__(name, health, armor, strength, intelligence, level, xp)
        self.attack1 = "Club Smash"
        self.attack1_method = self.club_smash
        self.attack2 = "Ground Pound"
        self.attack2_method = self.ground_pound
        self.heal1 = "Calloused Skin"
        self.heal1_method = self.calloused_skin
        self.intro = (f"The ground starts to shake. As you approach the Fairgold Mines, you see a {self.name} running toward you. Get ready to do battle.".center(70))
    def club_smash(self, target):
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
    def ground_pound(self, target):
        damage = int(round(self.strength * (random.uniform(0.15, 0.25))))
        target.health -= damage
        if target.health <= 0:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(70))
        elif target.health >= 0:
            target.health -= damage
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(70))
            else:
                print(BORDER)
                print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name}'s health is now {target.health}.".center(70))
                print(BORDER)
    def calloused_skin(self):
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
class Dragon(Boss):
    def __init__(self, name, health, armor, strength, intelligence, level, xp):
        super().__init__(name, health, armor, strength, intelligence, level, xp)
        self.attack1 = "Crystalline Breath"
        self.attack1_method = self.crystalline_breath
        self.attack2 = "Nosedive"
        self.attack2_method = self.nosedive
        self.heal1 = "Regrowth"
        self.heal1_method = self.regrowth
        self.intro = (f"You've awakened the {self.name}. A creature most thought had perished. It must have been sleeping for the last 1,000 years. He looks angry...".center(70))
    def crystalline_breath(self, target):
        damage = int(round(self.intelligence * (random.uniform(0.25, 0.5))))
        target.health -= damage
        if target.health <=0:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage}. {target.name} has perished.".center(70))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage} damage. {target.name}'s health is now {target.health}".center(70))
            print(BORDER)
    def nosedive(self, target):
        damage = int(round(self.strength * (random.uniform(0.15, 0.25))))
        target.health -= damage
        if target.health <= 0:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(70))
        elif target.health >= 0:
            target.health -= damage
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(70))
            else:
                print(BORDER)
                print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name}'s health is now {target.health}.".center(70))
                print(BORDER)
    def regrowth(self):
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
class Chimera(Boss):
    def __init__(self, name, health, armor, strength, intelligence, level, xp):
        super().__init__(name, health, armor, strength, intelligence, level, xp)
        self.attack1 = "Serpent's Sting"
        self.attack1_method = self.serpents_sting
        self.attack2 = "Fire Breath"
        self.attack2_method = self.fire_breath
        self.heal1 = "Prideful Roar"
        self.heal1_method = self.prideful_roar
        self.intro = (f"You've caught the attention of the {self.name}. Do not take this battle lightly adventurer. Many heroes of renown have fallen in battle to this monstrosity.".center(70))
    def serpents_sting(self, target):
        damage = int(round(self.intelligence * (random.uniform(0.25, 0.5))))
        target.health -= damage
        if target.health <=0:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage}. {target.name} has perished.".center(70))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage} damage. {target.name}'s health is now {target.health}".center(70))
            print(BORDER)
    def fire_breath(self, target):
        damage = int(round(self.strength * (random.uniform(0.15, 0.25))))
        target.health -= damage
        if target.health <= 0:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(70))
        elif target.health >= 0:
            target.health -= damage
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(70))
            else:
                print(BORDER)
                print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name}'s health is now {target.health}.".center(70))
                print(BORDER)
    def prideful_roar(self):
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
                print(f"{self.name} missed.".center(70))
                print(BORDER)

# Minor monsters
class Monster:
    def __init__(self, name, health, strength, intelligence, level, xp):
        self.name = name
        self.level = level
        self.health = health + (self.level * 10)
        self.strength = strength + (self.level * 10)
        self.intelligence = intelligence + (self.level * 10)
        self.xp = xp
    
class Shadowed(Monster):
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
    def create_lost_shadow():
        return Shadowed("Lost Shadow", 20, 10, 10, 1, 5 )
    @staticmethod
    def create_shadowed_seeker():
        return Shadowed("Shadowed Seeker", 30, 12, 10, 1, 10)
    @staticmethod
    def create_dark_mist():
        return Shadowed("Dark Mist", 100, 7, 5, 1, 15)
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
class Hyena(Monster):
    def __init__(self, name, health, strength, intelligence, level, xp):
        super().__init__(name, health, strength, intelligence, level, xp)
        self.attack1 = "Claw Dig"
        self.attack1_method = self.claw_dig
        self.attack2 = "Bite and Rip"
        self.attack2_method = self.bite_and_rip
        self.heal1 = "Howling Laugh"
        self.heal1_method = self.howling_laugh
    def claw_dig(self, target):
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
    def bite_and_rip(self, target):
        damage = int(round(self.strength * (random.uniform(0.30, 0.60))))
        target.health -= damage
        if target.health <= 0:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(70))
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name}'s health is now {target.health}.".center(70))
            print(BORDER)
    def howling_laugh(self):
            self.strength = int(self.strength * 1.5)
            print(f"{self.name}'s strength has increased to {self.strength}.".center(70))
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
                print(f"{self.name} missed.".center(70))
                print(BORDER)
    @staticmethod
    def create_laughing_hyena():
        return Hyena("Laughing Hyena", 50, 12, 6, 1, 10)
    @staticmethod
    def create_red_eyed_beast():
        return Hyena("Red Eyed Beast", 75, 15, 7, 1, 20)
    @staticmethod
    def create_failing_alpha():
        return Hyena("Failing alpha", 120, 17, 8, 1, 35)
class Crazed(Monster):
    def __init__(self, name, health, strength, intelligence, level, xp):
        super().__init__(name, health, strength, intelligence, level, xp)
        self.attack1 = "Limb Barrage"
        self.attack1_method = self.limb_barrage
        self.attack2 = "Sneak Attack"
        self.attack2_method = self.sneak_attack
        self.heal1 = "Unswayed Mind"
        self.heal1_method = self.unswayed_mind
    def limb_barrage(self, target):
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
    def sneak_attack(self, target):
        damage = int(round(self.strength * (random.uniform(0.30, 0.60))))
        target.health -= damage
        if target.health <= 0:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(70))
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name}'s health is now {target.health}.".center(70))
            print(BORDER)
    def unswayed_mind(self):
            self.strength = int(self.strength * 1.5)
            print(f"{self.name} uses {self.heal1}. It's strength has increased to {self.strength}.".center(70))
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
                print(f"{self.name} missed.".center(70))
                print(BORDER)
    @staticmethod
    def create_crazed_fanatic():
        return Crazed("Crazed Fanatic", 25, 12, 5, 1, 5)
    @staticmethod
    def create_crazed_sympathizer():
        return Crazed("Crazed Sympathizer", 50, 18, 6, 1, 8)
    @staticmethod
    def create_crazed_leader():
        return Crazed("Crazed Leader", 75, 20, 7, 1, 13)




