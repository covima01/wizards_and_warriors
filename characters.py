from classes import Mage, Fighter

Gandalf = Mage("Gandalf", 100, 20, 20)
Cloud = Fighter("Cloud", 125, 20, 20)

Gandalf.cast_fireball(Cloud)
Cloud.swing_axe(Gandalf)
Gandalf.cast_lightning(Cloud)