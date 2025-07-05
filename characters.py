from classes import Wizard, Warrior, Gray_Knight, Gray_Scholar, Flame_Walker, Frozen_Sorcerer, Storm_Mage, Berserker, Paladin, Sellsword


# Wizards
Gandalf = Wizard("Gandalf", 225, 150, 20, 0, 1, 3)
Yennefer = Wizard("Yennefer", 200, 200, 19, 0, 1, 3)
Jaina = Wizard("Jaina", 250, 175, 22, 0, 1, 3)
Debius = Flame_Walker("Debius", 230, 160, 21, 0, 1, 3)
Kalnir = Frozen_Sorcerer("Kal'nir", 250, 150, 22, 0, 1, 3)
Shoon = Storm_Mage("Shoon", 200, 200, 26, 0, 1, 3)

# Warriors
Cloud = Warrior("Cloud", 350, 100, 22, 0, 1, 3)
Geralt = Warrior("Geralt", 300, 100, 24, 0, 1, 3)
Tidus = Warrior("Tidus", 400, 100, 20, 0, 1, 3)
Chokthun = Berserker("Chok'thun", 275, 80, 27, 0, 1, 3)
Reingard = Paladin("Reingard", 400, 150, 17, 0, 1, 3)
Kalsonin = Sellsword("Kal'sonin", 320, 100, 22, 0, 1, 3)

# Grays
Disgraced_Knight = Gray_Knight("Disgraced Knight", 300, 90, 22, 0, 1, 3)
Expelled_Scholar = Gray_Scholar("Expelled Scholar", 200, 170, 22, 0, 1, 3)


Characters = [Disgraced_Knight, Expelled_Scholar]
Wizards = [Debius, Kalnir, Shoon]
Warriors = [Chokthun, Reingard, Kalsonin]
