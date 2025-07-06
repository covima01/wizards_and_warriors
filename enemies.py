from enemy_classes import Goblin, Harpy, Orc, Ogre, Giant_Ogre, Dragon, Chimera

# Bosses
Fetid_Brute = Giant_Ogre("Fetid Brute", 300, 100, 25, 25, 3, 50)
Scalewing_Alpha = Dragon("Scalewing Alpha", 350, 125, 27, 28, 6, 125)
The_Myth = Chimera("The Myth", 420, 145, 30, 31, 9, 180) #     def __init__(self, name, health, armor, strength, intelligence, level, xp):


# Goblins (self, name, health, strength, intelligence, level, xp)
Goblin_Trickster = Goblin("Goblin Trickster", 20, 10, 10, 1, 5 )
Goblin_Bully = Goblin("Goblin Bully", 30, 12, 10, 1, 10)
Goblin_Fat_Cat = Goblin("Goblin Fat-Cat", 100, 7, 5, 1, 15)

# Harpies (self, name, health, strength, intelligence, level, xp)
Harpy_Huntress = Harpy("Harpy Huntress", 30, 9, 11, 1, 5)
Harpy_Terror = Harpy("Harpy Terror", 45, 11, 13, 1, 10)
Harpy_Matriarch = Harpy("Harpy Matriarch", 80, 13, 15, 1, 15)

# Orcs (self, name, health, strength, intelligence, level, xp)
Orc_Warrior = Orc("Orc Warrior", 50, 12, 6, 1, 10)
Orc_Captain = Orc("Orc Captain", 75, 15, 7, 1, 20)
Orc_Warmonger = Orc("Orc Warmonger", 120, 17, 8, 1, 35)

# Ogres (self, name, health, strength, intelligence, level, xp)
Ogre_Grunt = Ogre("Ogre Grunt", 25, 12, 5, 1, 5)
Ogre_General = Ogre("Ogre General", 50, 18, 6, 1, 8)
Ogre_Warlord = Ogre("Ogre Warlord", 75, 20, 7, 1, 13)

Enemy_Creation = [Goblin.create_goblin_trickster, Goblin.create_goblin_bully, Goblin.create_goblin_fat_cat, Harpy.create_harpy_huntress, 
                Harpy.create_harpy_terror, Harpy.create_harpy_matriarch, Orc.create_orc_warrior, Orc.create_orc_captain, Orc.create_orc_warmonger,
                Ogre.create_ogre_grunt, Ogre.create_ogre_general, Ogre.create_ogre_warlord]