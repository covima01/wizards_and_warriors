import random
from constants import BORDER
# Bosses
class Boss:
    def __init__(self, name, health, armor, strength, intelligence, level, xp):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
        self.armor = armor
        self.intelligence = intelligence
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
    def club_smash(self, target):
        damage = int(round(self.strength * (random.uniform(0.25, 0.5))))
        target.health -= damage
        if target.health <=0:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage}. {target.name} has perished.".center(100))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage} damage. {target.name}'s health is now {target.health}".center(100))
            print(BORDER)
    def ground_pound(self, target):
        damage = int(round(self.strength * (random.uniform(0.15, 0.25))))
        target.health -= damage
        if target.health <= 0:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(100))
        elif target.health >= 0:
            target.health -= damage
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(100))
            else:
                print(BORDER)
                print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name}'s health is now {target.health}.".center(100))
                print(BORDER)
    def calloused_skin(self):
            healing_amount = int(self.health * 0.15)
            self.health += healing_amount
            print(BORDER)
            print(f"{self.name} uses {self.heal1} for {healing_amount}. Health: {self.health}".center(100))
            print(BORDER)
    def counterattack(self, target):
            counterattacks = [self.attack1_method, self.attack2_method, self.heal1_method]
            chosen_counter = random.choice(counterattacks)
            attack = random.randint(0,10)
            if attack <= 9:
                if self.health > 0:
                    if chosen_counter == self.heal1_method:
                        chosen_counter()
                    else:
                        chosen_counter(target)
            else:
                print(BORDER)
                print(f"{self.name} missed.".center(100))
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
    def crystalline_breath(self, target):
        damage = int(round(self.intelligence * (random.uniform(0.25, 0.5))))
        target.health -= damage
        if target.health <=0:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage}. {target.name} has perished.".center(100))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage} damage. {target.name}'s health is now {target.health}".center(100))
            print(BORDER)
    def nosedive(self, target):
        damage = int(round(self.strength * (random.uniform(0.15, 0.25))))
        target.health -= damage
        if target.health <= 0:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(100))
        elif target.health >= 0:
            target.health -= damage
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(100))
            else:
                print(BORDER)
                print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name}'s health is now {target.health}.".center(100))
                print(BORDER)
    def regrowth(self):
            healing_amount = int(self.health * 0.15)
            self.health += healing_amount
            print(BORDER)
            print(f"{self.name} uses {self.heal1} for {healing_amount}. Health: {self.health}".center(100))
            print(BORDER)
    def counterattack(self, target):
            counterattacks = [self.attack1_method, self.attack2_method, self.heal1_method]
            chosen_counter = random.choice(counterattacks)
            attack = random.randint(0,10)
            if attack <= 9:
                if self.health > 0:
                    if chosen_counter == self.heal1_method:
                        chosen_counter()
                    else:
                        chosen_counter(target)
            else:
                print(BORDER)
                print(f"{self.name} missed.".center(100))
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
    def serpents_sting(self, target):
        damage = int(round(self.intelligence * (random.uniform(0.25, 0.5))))
        target.health -= damage
        if target.health <=0:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage}. {target.name} has perished.".center(100))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage} damage. {target.name}'s health is now {target.health}".center(100))
            print(BORDER)
    def fire_breath(self, target):
        damage = int(round(self.strength * (random.uniform(0.15, 0.25))))
        target.health -= damage
        if target.health <= 0:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(100))
        elif target.health >= 0:
            target.health -= damage
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(100))
            else:
                print(BORDER)
                print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name}'s health is now {target.health}.".center(100))
                print(BORDER)
    def prideful_roar(self):
            healing_amount = int(self.health * 0.15)
            self.health += healing_amount
            print(BORDER)
            print(f"{self.name} uses {self.heal1} for {healing_amount}. Health: {self.health}".center(100))
            print(BORDER)
    def counterattack(self, target):
            counterattacks = [self.attack1_method, self.attack2_method, self.heal1_method]
            chosen_counter = random.choice(counterattacks)
            attack = random.randint(0,10)
            if attack <= 9:
                if self.health > 0:
                    if chosen_counter == self.heal1_method:
                        chosen_counter()
                    else:
                        chosen_counter(target)
            else:
                print(BORDER)
                print(f"{self.name} missed.".center(100))
                print(BORDER)
class Darkness(Boss):
    def __init__(self, name, health, armor, strength, intelligence, level, xp):
        super().__init__(name, health, armor, strength, intelligence, level, xp)
        self.attack1 = "Infection"
        self.attack1_method = self.infection
        self.attack2 = "Consuming Darkness"
        self.attack2_method = self.consuming_darkness
        self.heal1 = "Drain Life"
        self.heal1_method = self.drain_life
    def infection(self, target):
        damage = int(round(self.intelligence * (random.uniform(0.25, 0.5))))
        target.health -= damage
        if target.health <=0:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage}. {target.name} has perished.".center(100))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage} damage. {target.name}'s health is now {target.health}".center(100))
            print(BORDER)
    def consuming_darkness(self, target):
        damage = int(round(self.strength * (random.uniform(0.15, 0.25))))
        target.health -= damage
        if target.health <= 0:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(100))
        elif target.health >= 0:
            target.health -= damage
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(100))
            else:
                print(BORDER)
                print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name}'s health is now {target.health}.".center(100))
                print(BORDER)
    def drain_life(self):
            healing_amount = int(self.health * 0.15)
            self.health += healing_amount
            print(BORDER)
            print(f"{self.name} uses {self.heal1} for {healing_amount}. Health: {self.health}".center(100))
            print(BORDER)
    def counterattack(self, target):
            counterattacks = [self.attack1_method, self.attack2_method, self.heal1_method]
            chosen_counter = random.choice(counterattacks)
            attack = random.randint(0,10)
            if attack <= 9:
                if self.health > 0:
                    if chosen_counter == self.heal1_method:
                        chosen_counter()
                    else:
                        chosen_counter(target)
            else:
                print(BORDER)
                print(f"{self.name} missed.".center(100))
                print(BORDER)

# Monsters - Creatures
class Monster:
    def __init__(self, name, health, strength, intelligence, level, xp):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
        self.intelligence = intelligence
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
            print(f"{self.name}'s {self.attack1} deals {damage}. {target.name} has perished.".center(100))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage} damage. {target.name}'s health is now {target.health}".center(100))
            print(BORDER)
    def double_shot(self, target):
        damage = int(round(self.strength * (random.uniform(0.15, 0.25))))
        target.health -= damage
        if target.health <= 0:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(100))
        elif target.health >= 0:
            target.health -= damage
            if target.health <= 0:
                print(BORDER)
                print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(100))
            else:
                print(BORDER)
                print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name}'s health is now {target.health}.".center(100))
                print(BORDER)
    def healing_dust(self):
            healing_amount = int(self.health * 0.15)
            self.health += healing_amount
            print(BORDER)
            print(f"{self.name} uses {self.heal1} for {healing_amount}. Health: {self.health}".center(100))
            print(BORDER)
    def counterattack(self, target):
            counterattacks = [self.attack1_method, self.attack2_method, self.heal1_method]
            chosen_counter = random.choice(counterattacks)
            attack = random.randint(0,10)
            if attack <= 9:
                if self.health > 0:
                    if chosen_counter == self.heal1_method:
                        chosen_counter()
                    else:
                        chosen_counter(target)
            else:
                print(BORDER)
                print(f"{self.name} missed.".center(100))
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
            print(f"{self.name}'s {self.attack1} deals {damage}. {target.name} has perished.".center(100))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage} damage. {target.name}'s health is now {target.health}".center(100))
            print(BORDER)
    def siren_song(self, target):
        damage = int(round(self.intelligence * (random.uniform(0.15, 0.25))))
        target.health -= damage
        if target.health <= 0:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(100))
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name}'s health is now {target.health}.".center(100))
            print(BORDER)
    def rejuvinating_cry(self):
            healing_amount = int(self.health * 0.15)
            self.health += healing_amount
            print(BORDER)
            print(f"{self.name} uses {self.heal1} for {healing_amount}. Health: {self.health}".center(100))
            print(BORDER)
    def counterattack(self, target):
            counterattacks = [self.attack1_method, self.attack2_method, self.heal1_method]
            chosen_counter = random.choice(counterattacks)
            attack = random.randint(0,10)
            if attack <= 9:
                if self.health > 0:
                    if chosen_counter == self.heal1_method:
                        chosen_counter()
                    else:
                        chosen_counter(target)
            else:
                print(BORDER)
                print(f"{self.name} missed.".center(100))
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
            print(f"{self.name}'s {self.attack1} deals {damage}. {target.name} has perished.".center(100))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage} damage. {target.name}'s health is now {target.health}".center(100))
            print(BORDER)
    def bite_and_rip(self, target):
        damage = int(round(self.strength * (random.uniform(0.30, 0.60))))
        target.health -= damage
        if target.health <= 0:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(100))
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name}'s health is now {target.health}.".center(100))
            print(BORDER)
    def howling_laugh(self):
            self.strength = int(self.strength * 1.5)
            print(f"{self.name}'s strength has increased to {self.strength}.".center(100))
    def counterattack(self, target):
            counterattacks = [self.attack1_method, self.attack2_method, self.heal1_method]
            chosen_counter = random.choice(counterattacks)
            attack = random.randint(0,10)
            if attack <= 9:
                if self.health > 0:
                    if chosen_counter == self.heal1_method:
                        chosen_counter()
                    else:
                        chosen_counter(target)
            else:
                print(BORDER)
                print(f"{self.name} missed.".center(100))
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
class Ravenous(Monster):
    def __init__(self, name, health, strength, intelligence, level, xp):
        super().__init__(name, health, strength, intelligence, level, xp)
        self.attack1 = "Penetrating Bite"
        self.attack1_method = self.penetrating_bite
        self.attack2 = "Go For The Throat"
        self.attack2_method = self.go_for_the_throat
        self.heal1 = "Lick Wound"
        self.heal1_method = self.lick_wound
    def penetrating_bite(self, target):
        damage = int(round(self.strength * (random.uniform(0.25, 0.5))))
        target.health -= damage
        if target.health <=0:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage}. {target.name} has perished.".center(100))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage} damage. {target.name}'s health is now {target.health}".center(100))
            print(BORDER)
    def go_for_the_throat(self, target):
        damage = int(round(self.strength * (random.uniform(0.30, 0.60))))
        target.health -= damage
        if target.health <= 0:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(100))
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name}'s health is now {target.health}.".center(100))
            print(BORDER)
    def lick_wound(self):
            healing_amount = int(self.health * 0.15)
            self.health += healing_amount
            print(BORDER)
            print(f"{self.name} uses {self.heal1} for {healing_amount}. Health: {self.health}".center(100))
            print(BORDER)
    def counterattack(self, target):
            counterattacks = [self.attack1_method, self.attack2_method, self.heal1_method]
            chosen_counter = random.choice(counterattacks)
            attack = random.randint(0,10)
            if attack <= 9:
                if self.health > 0:
                    if chosen_counter == self.heal1_method:
                        chosen_counter()
                    else:
                        chosen_counter(target)
            else:
                print(BORDER)
                print(f"{self.name} missed.".center(100))
                print(BORDER)
    @staticmethod
    def create_ravenous_stray():
        return Ravenous("Ravenous Stray", 25, 12, 5, 1, 5)
    @staticmethod
    def create_ravenous_mutt():
        return Ravenous("Ravenous Mutt", 50, 18, 6, 1, 8)
    @staticmethod
    def create_ravenous_mastiff():
        return Ravenous("Ravenous Mastiff", 75, 20, 7, 1, 13)
class Abomination(Monster):
    def __init__(self, name, health, strength, intelligence, level, xp):
        super().__init__(name, health, strength, intelligence, level, xp)
        self.attack1 = "Toxic Hook"
        self.attack1_method = self.toxic.hook
        self.attack2 = "Contamination"
        self.attack2_method = self.contamination
        self.heal1 = "Regrow Limbs"
        self.heal1_method = self.regrow_limbs
    def toxic_hook(self, target):
        damage = int(round(self.strength * (random.uniform(0.25, 0.5))))
        target.health -= damage
        if target.health <=0:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage}. {target.name} has perished.".center(100))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage} damage. {target.name}'s health is now {target.health}".center(100))
            print(BORDER)
    def contamination(self, target):
        damage = int(round(self.strength * (random.uniform(0.30, 0.60))))
        target.health -= damage
        if target.health <= 0:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(100))
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name}'s health is now {target.health}.".center(100))
            print(BORDER)
    def regrow_limbs(self):
            healing_amount = int(self.health * 0.15)
            self.health += healing_amount
            print(BORDER)
            print(f"{self.name} uses {self.heal1} for {healing_amount}. Health: {self.health}".center(100))
            print(BORDER)
    def counterattack(self, target):
            counterattacks = [self.attack1_method, self.attack2_method, self.heal1_method]
            chosen_counter = random.choice(counterattacks)
            attack = random.randint(0,10)
            if attack <= 9:
                if self.health > 0:
                    if chosen_counter == self.heal1_method:
                        chosen_counter()
                    else:
                        chosen_counter(target)
            else:
                print(BORDER)
                print(f"{self.name} missed.".center(100))
                print(BORDER)
    @staticmethod
    def create_disturbing_abomination():
        return Abomination("Disturbing Abomination", 25, 12, 5, 1, 5)
    @staticmethod
    def create_disgusting_abomination():
        return Abomination("Disgusting Abomination", 50, 18, 6, 1, 8)
    @staticmethod
    def create_hulking_abomination():
        return Abomination("Hulking Abomination", 75, 20, 7, 1, 13)

# Monsters - Humanoid
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
            print(f"{self.name}'s {self.attack1} deals {damage}. {target.name} has perished.".center(100))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage} damage. {target.name}'s health is now {target.health}".center(100))
            print(BORDER)
    def sneak_attack(self, target):
        damage = int(round(self.strength * (random.uniform(0.30, 0.60))))
        target.health -= damage
        if target.health <= 0:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(100))
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name}'s health is now {target.health}.".center(100))
            print(BORDER)
    def unswayed_mind(self):
            self.strength = int(self.strength * 1.5)
            print(f"{self.name} uses {self.heal1}. It's strength has increased to {self.strength}.".center(100))
    def counterattack(self, target):
            counterattacks = [self.attack1_method, self.attack2_method, self.heal1_method]
            chosen_counter = random.choice(counterattacks)
            attack = random.randint(0,10)
            if attack <= 9:
                if self.health > 0:
                    if chosen_counter == self.heal1_method:
                        chosen_counter()
                    else:
                        chosen_counter(target)
            else:
                print(BORDER)
                print(f"{self.name} missed.".center(100))
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
class Claimant(Monster):
    def __init__(self, name, health, strength, intelligence, level, xp):
        super().__init__(name, health, strength, intelligence, level, xp)
        self.attack1 = "Enflame"
        self.attack1_method = self.enflame
        self.attack2 = "Wildfire"
        self.attack2_method = self.wildfire
        self.heal1 = "Meditate"
        self.heal1_method = self.meditate
    def enflame(self, target):
        damage = int(round(self.strength * (random.uniform(0.25, 0.5))))
        target.health -= damage
        if target.health <=0:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage}. {target.name} has perished.".center(100))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage} damage. {target.name}'s health is now {target.health}".center(100))
            print(BORDER)
    def wildfire(self, target):
        damage = int(round(self.strength * (random.uniform(0.30, 0.60))))
        target.health -= damage
        if target.health <= 0:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(100))
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name}'s health is now {target.health}.".center(100))
            print(BORDER)
    def meditate(self):
            healing_amount = int(self.health * 0.15)
            self.health += healing_amount
            print(BORDER)
            print(f"{self.name} uses {self.heal1} for {healing_amount}. Health: {self.health}".center(100))
            print(BORDER)
    def counterattack(self, target):
            counterattacks = [self.attack1_method, self.attack2_method, self.heal1_method]
            chosen_counter = random.choice(counterattacks)
            attack = random.randint(0,10)
            if attack <= 9:
                if self.health > 0:
                    if chosen_counter == self.heal1_method:
                        chosen_counter()
                    else:
                        chosen_counter(target)
            else:
                print(BORDER)
                print(f"{self.name} missed.".center(100))
                print(BORDER)
    @staticmethod
    def create_claimant_follower():
        return Claimant("Claimant Follower", 25, 12, 5, 1, 5)
    @staticmethod
    def create_claimant_guard():
        return Claimant("Claimant Guard", 50, 18, 6, 1, 8)
    @staticmethod
    def create_claimant_prophet():
        return Claimant("Claimant Prophet", 75, 20, 7, 1, 13)
class Forgotten(Monster):
    def __init__(self, name, health, strength, intelligence, level, xp):
        super().__init__(name, health, strength, intelligence, level, xp)
        self.attack1 = "Bare Knuckle Swing"
        self.attack1_method = self.bare_knuckle_swing
        self.attack2 = "Give Up"
        self.attack2_method = self.give_up
        self.heal1 = "Pleasant Memories"
        self.heal1_method = self.pleasant_memories
    def bare_knuckle_swing(self, target):
        damage = int(round(self.strength * (random.uniform(0.25, 0.5))))
        target.health -= damage
        if target.health <=0:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage}. {target.name} has perished.".center(100))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage} damage. {target.name}'s health is now {target.health}".center(100))
            print(BORDER)
    def give_up(self, target):
        damage = 0
        target.health -= damage
        if target.health <= 0:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(100))
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name}'s health is now {target.health}.".center(100))
            print(BORDER)
    def pleasant_memories(self):
            healing_amount = int(self.health * 0.15)
            self.health += healing_amount
            print(BORDER)
            print(f"{self.name} uses {self.heal1} for {healing_amount}. Health: {self.health}".center(100))
            print(BORDER)
    def counterattack(self, target):
            counterattacks = [self.attack1_method, self.attack2_method, self.heal1_method]
            chosen_counter = random.choice(counterattacks)
            attack = random.randint(0,10)
            if attack <= 9:
                if self.health > 0:
                    if chosen_counter == self.heal1_method:
                        chosen_counter()
                    else:
                        chosen_counter(target)
            else:
                print(BORDER)
                print(f"{self.name} missed.".center(100))
                print(BORDER)
    @staticmethod
    def create_forgotten_bellkeep():
        return Forgotten("Forgotten Bellkeep", 25, 12, 5, 1, 5)
    @staticmethod
    def create_forgotten_highwayman():
        return Forgotten("Forgotten Highwayman", 50, 18, 6, 1, 8)
    @staticmethod
    def create_forgotten_warrior():
        return Forgotten("Forgotten Warrior", 75, 20, 7, 1, 13)
class Kingsguard(Monster):
    def __init__(self, name, health, strength, intelligence, level, xp):
        super().__init__(name, health, strength, intelligence, level, xp)
        self.attack1 = "Overhead Swing"
        self.attack1_method = self.overhead_swing
        self.attack2 = "Lance"
        self.attack2_method = self.lance
        self.heal1 = "Graylight"
        self.heal1_method = self.graylight
    def overhead_swing(self, target):
        damage = int(round(self.strength * (random.uniform(0.25, 0.5))))
        target.health -= damage
        if target.health <=0:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage}. {target.name} has perished.".center(100))
            print(BORDER)
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack1} deals {damage} damage. {target.name}'s health is now {target.health}".center(100))
            print(BORDER)
    def lance(self, target):
        damage = 0
        target.health -= damage
        if target.health <= 0:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name} has perished.".center(100))
        else:
            print(BORDER)
            print(f"{self.name}'s {self.attack2} deals {damage} damage. {target.name}'s health is now {target.health}.".center(100))
            print(BORDER)
    def graylight(self):
            healing_amount = int(self.health * 0.15)
            self.health += healing_amount
            print(BORDER)
            print(f"{self.name} uses {self.heal1} for {healing_amount}. Health: {self.health}".center(100))
            print(BORDER)
    def counterattack(self, target):
            counterattacks = [self.attack1_method, self.attack2_method, self.heal1_method]
            chosen_counter = random.choice(counterattacks)
            attack = random.randint(0,10)
            if attack <= 9:
                if self.health > 0:
                    if chosen_counter == self.heal1_method:
                        chosen_counter()
                    else:
                        chosen_counter(target)
            else:
                print(BORDER)
                print(f"{self.name} missed.".center(100))
                print(BORDER)
    @staticmethod
    def create_kingsguard_infantry():
        return Kingsguard("Kingsguard Infantry", 25, 12, 5, 1, 5)
    @staticmethod
    def create_kingsguard_sentinel():
        return Kingsguard("Kingsguard Sentinel", 50, 18, 6, 1, 8)
    @staticmethod
    def create_kingsguard_captain():
        return Kingsguard("Kingsguard Captain", 75, 20, 7, 1, 13)
