from enemy_classes import *

# Bosses
Fetid_Brute = Giant_Ogre("Fetid Brute", 300, 100, 25, 25, 3, 50) # Rejection
Scalewing_Alpha = Dragon("Scalewing Alpha", 350, 125, 27, 28, 6, 125) # Existentialism
The_Myth = Chimera("The Myth", 420, 145, 30, 31, 9, 180) # Anhedonia
Unknown = Darkness("???", 600, 150, 33, 33, 10, 225) # Numbness

# Shadowed (self, name, health, strength, intelligence, level, xp)
Lost_Shadow = Shadowed("Lost Shadow", 20, 10, 10, 1, 5 ) # Desolate Place (1)
Shadowed_Seeker = Shadowed("Shadowed Seeker", 30, 12, 10, 1, 10) # Abandoned Sanctuary (2)
Dark_Mist = Shadowed("Dark Mist", 100, 7, 5, 1, 15) # Abandoned Sanctuary (2)

# Harpies (self, name, health, strength, intelligence, level, xp)
Harpy_Huntress = Harpy("Harpy Huntress", 30, 9, 11, 1, 5) # Desolate Place (1)
Harpy_Terror = Harpy("Harpy Terror", 45, 11, 13, 1, 10) # Southern Desert (3)
Harpy_Matriarch = Harpy("Harpy Matriarch", 80, 13, 15, 1, 15) # Southern Desert (3)

# Hyenas (self, name, health, strength, intelligence, level, xp)
Laughing_Hyena = Hyena("Laughing Hyena", 50, 12, 6, 1, 10) # Desolate Place (1)
Red_Eyed_Beast = Hyena("Red Eyed Beast", 75, 15, 7, 1, 20) # Abandoned Sanctuary (2)
Failing_Alpha = Hyena("Failing Alpha", 120, 17, 8, 1, 35) # Southern Desert (3)

# Ravenous (self, name, health, strength, intelligence, level, xp)
Ravenous_Stray = Ravenous("Ravenous Stray", 25, 12, 5, 1, 5) # Lostnorth Forest (5)
Ravenous_Mutt = Ravenous("Ravenous Mutt", 50, 18, 6, 1, 8) # Lostnorth Forest (5)
Ravenous_Mastiff = Ravenous("Ravenous Mastiff", 75, 20, 7, 1, 13) # Alenia Farmland (6)
Kingsguard_Hound = Ravenous("Kingsguard Hound", 100, 22, 8, 1, 15) # Mountain Cliffs (9)

# Abomination (self, name, health, strength, intelligence, level, xp)
Disturbing_Abomination = Abomination("Disturbing Abomination", 25, 12, 5, 1, 5) # Longways Aqueduct (4)
Disgusting_Abomination = Abomination("Disgusting Abomination", 50, 18, 6, 1, 8) # Longways Aqueduct (4)
Hulking_Abomination = Abomination("Hulking Abomination", 75, 20, 7, 1, 13) # Longways Aqueduct (4)

# Crazed (self, name, health, strength, intelligence, level, xp)
Crazed_Fanatic = Crazed("Crazed Fanatic", 25, 12, 5, 1, 5) # Longways Aqueduct (4)
Crazed_Sympathizer = Crazed("Crazed_Sympathizer", 50, 18, 6, 1, 8) # Lostnorth Forest (5)
Crazed_Leader = Crazed("Crazed Leader", 75, 20, 7, 1, 13) # Alenia Farmland (6)

# Claimant (self, name, health, strength, intelligence, level, xp)
Claimant_Follower = Claimant("Claimant Follower", 25, 12, 5, 1, 5) # Alenia Farmland (6)
Claimant_Guard = Claimant("Claimant Guard", 50, 18, 6, 1, 8) # Mountain Pass (7)
Claimant_Prophet = Claimant("Claimant Prophet", 75, 20, 7, 1, 13) # Mountain Pass (7)

# Forgotten (self, name, health, strength, intelligence, level, xp)
Forgotten_Bellkeep = Forgotten("Forgotten Bellkeep", 25, 12, 5, 1, 5) # Mountain Pass (7)
Forgotten_Highwayman = Forgotten("Forgotten Highwayman", 50, 18, 6, 1, 8) # Mountain Ascent (8)
Forgotten_Warrior = Forgotten("Forgotten Warrior", 75, 20, 7, 1, 13) # Mountain Ascent (8)

# Kingsguard (self, name, health, strength, intelligence, level, xp)
Kingsguard_Infantry = Kingsguard("Kingsguard Infantry", 25, 12, 5, 1, 5) # Mountain Ascent (8)
Kingsguard_Sentinel = Kingsguard("Kingsguard Sentinel", 50, 18, 6, 1, 8) # Mountain Cliffs (9)
Kingsguard_Captain = Kingsguard("Kingsguard Captain", 75, 20, 7, 1, 13) # Mountain Cliffs (9)
Royal_Guard = Kingsguard("Royal Guard", 100, 22, 8, 1, 15) # Mountain Peak (10)
Royal_Sword = Kingsguard("Royal Sword", 125, 23, 9, 1, 16) # Mountain Peak (10)
Shieldsworn = Kingsguard("Shieldsworn", 150, 19, 9, 1, 17) # Mountain Peak (10)


Desolate_Place_Enemies = [Shadowed.create_lost_shadow, Harpy.create_harpy_huntress, Hyena.create_laughing_hyena]
Abandoned_Sanctuary_Enemies = [Shadowed.create_shadowed_seeker, Shadowed.create_dark_mist, Hyena.create_red_eyed_beast]
Southern_Desert_Enemies = [Harpy.create_harpy_terror, Harpy.create_harpy_matriarch, Hyena.create_failing_alpha]
Longways_Aqueduct_Enemies = [Abomination.create_disturbing_abomination, Abomination.create_disgusting_abomination, Abomination.create_hulking_abomination, Crazed.create_crazed_fanatic]
Lostnorth_Forest_Enemies = [Ravenous.create_ravenous_stray, Ravenous.create_ravenous_mutt, Crazed.create_crazed_sympathizer]
Alenia_Farmland_Enemies = [Crazed.create_crazed_leader, Ravenous.create_ravenous_mastiff, Claimant.create_claimant_follower]
Mountain_Pass_Enemies = [Claimant.create_claimant_guard, Claimant.create_claimant_prophet, Forgotten.create_forgotten_bellkeep]
Mountain_Ascent_Enemies = [Forgotten.create_forgotten_highwayman, Forgotten.create_forgotten_warrior, Kingsguard.create_kingsguard_infantry]
Mountain_Cliffs_Enemies = [Ravenous.create_kingsguard_hound, Kingsguard.create_kingsguard_sentinel, Kingsguard.create_kingsguard_captain]
Mountain_Peak_Enemies = [Kingsguard.create_royal_guard, Kingsguard.create_royal_sword, Kingsguard.create_shieldsworn]

Enemy_Creation = [Shadowed.create_lost_shadow, Shadowed.create_shadowed_seeker, Shadowed.create_dark_mist, Harpy.create_harpy_huntress, 
                Harpy.create_harpy_terror, Harpy.create_harpy_matriarch, Hyena.create_laughing_hyena, Hyena.create_red_eyed_beast, Hyena.create_failing_alpha,
                Crazed.create_crazed_fanatic, Crazed.create_crazed_sympathizer, Crazed.create_crazed_leader]