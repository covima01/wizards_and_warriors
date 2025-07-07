from enemy_classes import Shadowed, Harpy, Hyena, Crazed, Giant_Ogre, Dragon, Chimera

# Bosses
Fetid_Brute = Giant_Ogre("Fetid Brute", 300, 100, 25, 25, 3, 50) # Rejection
Scalewing_Alpha = Dragon("Scalewing Alpha", 350, 125, 27, 28, 6, 125) # Existentialism
The_Myth = Chimera("The Myth", 420, 145, 30, 31, 9, 180) # Anhedonia
Unknown = Crazed("???", 600, 33, 33, 10, 225) # Numbness


# Goblins (self, name, health, strength, intelligence, level, xp)
Lost_Shadow = Shadowed("Lost Shadow", 20, 10, 10, 1, 5 )
Shadowed_Seeker = Shadowed("Shadowed Seeker", 30, 12, 10, 1, 10)
Dark_Mist = Shadowed("Dark Mist", 100, 7, 5, 1, 15)

# Harpies (self, name, health, strength, intelligence, level, xp)
Harpy_Huntress = Harpy("Harpy Huntress", 30, 9, 11, 1, 5)
Harpy_Terror = Harpy("Harpy Terror", 45, 11, 13, 1, 10)
Harpy_Matriarch = Harpy("Harpy Matriarch", 80, 13, 15, 1, 15)

# Orcs (self, name, health, strength, intelligence, level, xp)
Laughing_Hyena = Hyena("Laughing Hyena", 50, 12, 6, 1, 10)
Red_Eyed_Beast = Hyena("Red Eyed Beast", 75, 15, 7, 1, 20)
Failing_Alpha = Hyena("Failing Alpha", 120, 17, 8, 1, 35)

# Ogres (self, name, health, strength, intelligence, level, xp)
Crazed_Fanatic = Crazed("Crazed Fanatic", 25, 12, 5, 1, 5)
Crazed_Sympathizer = Crazed("Crazed Sympathizer", 50, 18, 6, 1, 8)
Crazed_Leader = Crazed("Crazed Leader", 75, 20, 7, 1, 13)

Enemy_Creation = [Shadowed.create_lost_shadow, Shadowed.create_shadowed_seeker, Shadowed.create_dark_mist, Harpy.create_harpy_huntress, 
                Harpy.create_harpy_terror, Harpy.create_harpy_matriarch, Hyena.create_laughing_hyena, Hyena.create_red_eyed_beast, Hyena.create_failing_alpha,
                Crazed.create_crazed_fanatic, Crazed.create_crazed_sympathizer, Crazed.create_crazed_leader]