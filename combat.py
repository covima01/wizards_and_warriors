import random
import time
from classes import BORDER

def combat(player, enemy):
    while enemy.health > 0 and player.health > 0:
        time.sleep(0.5)
        print(f"{player.name}-- Health: {player.health} , {player.resource_type}: {player.resource} // {enemy.name}-- Health: {enemy.health} , {enemy.resource_type}: {enemy.resource}".center(70))
        print(f"What will {player.name} do?".center(70))
        selection = input(f"\n1) {player.attack1} - {player.attack1_description}.\n2) {player.attack2} - {player.attack2_description}.\n3) {player.heal1} - {player.heal1_description}\n")
        while selection != "1" and selection != "2" and selection != "3":
            print(f"Unrecognized selection. Please choose 1 to use {player.attack1}, 2 to use {player.attack2}, or 3 to use {player.heal1}\n")
            selection = input(f"Which action will {player.name} take?  {player.name} has {player.health} health.\n {enemy.name} has {enemy.health} health.\n\n 1) {player.attack1}\n 2) {player.attack2}\n 3) {player.heal1}")
        if selection == "1":
            attack = random.randint(0,8)
            if attack <= 7:
                player.attack1_method(enemy)
                if enemy.health > 0:
                    enemy.counterattack(player)
            else:
                print(BORDER)
                print(f"{player.name} missed".center(70))
                print(BORDER)
                if enemy.health > 0:
                    enemy.counterattack(player)
        elif selection == "2":
            attack = random.randint(0,8)
            if attack <= 7:
                player.attack2_method(enemy)
                if enemy.health > 0:
                    enemy.counterattack(player)   
            else:
                print(BORDER)
                print(f"{player.name} missed".center(70))
                print(BORDER)
                if enemy.health > 0:
                    enemy.counterattack(player)
        elif selection == "3":
            player.heal1_method()
            if enemy.health > 0:
                enemy.counterattack_method(player)
    else:
        return

#################################################################################################################################################################
#######################################################   OLD   #################################################################################################
#################################################################################################################################################################

    # elif isinstance(player, Warrior) and isinstance(enemy, Wizard):  
    #    while enemy.health > 0 and player.health > 0:
     #       time.sleep(0.5)
      #      print(f"{player.name}-- Health: {player.health} , Endurance: {player.resource} // {enemy.name}-- Health: {enemy.health} , Mana: {enemy.resource}".center(70))
       #     print(f"What will {player.name} do?".center(70))
        #    selection = input(f"\n1) Light Swing - deals moderate physical damage.\n2) Heavy Swing - deals heavy physical damage.\n3) Meditate - moderately restores your health.")
         #   while selection != "1" and selection != "2" and selection != "3":
          #      print("Unrecognized selection. Please choose 1) Light Swing or 2) Heavy Swing 3) Meditate")
           #     selection = input(f"Which action will {player.name} take?  {player.name} has {player.health} health. {enemy.name} has {enemy.health} health.\n\n 1) Light Swing\n 2) Heavy Swing\n 3) Meditate")
            #if selection == "1":
             #   attack = random.randint(0,8)
              #  if attack <= 7:
               #     player.light_swing(enemy)
                #    if enemy.health > 0:
                 #       enemy.wizard_counterattack(player)
                #else:
                 #   print(BORDER)
                  #  print(f"{player.name} missed".center(70))
                   # print(BORDER)
                    #if enemy.health > 0:
                    #    enemy.wizard_counterattack(player)
            #elif selection == "2":
             #   attack = random.randint(0,8)
              #  if attack <= 7:
               #     player.heavy_swing(enemy)
                #    if enemy.health > 0:
                 #       enemy.wizard_counterattack(player)
                #else:
                 #   print(BORDER)
                  #  print(f"{player.name} missed".center(70))
                   # print(BORDER)
                    #if enemy.health > 0:
                     #   enemy.wizard_counterattack(player)
            #elif selection == "3":
             #   player.meditate()
              #  if enemy.health > 0:
               #     enemy.wizard_counterattack(player)
    #elif isinstance(player, Warrior) and isinstance(enemy, Warrior):  
     #   while enemy.health > 0 and player.health > 0:
      #      time.sleep(0.5)
       #     print(f"{player.name}-- Health: {player.health} , Endurance: {player.resource} // {enemy.name}-- Health: {enemy.health} , Endurance: {enemy.resource}".center(70))
        #    print(f"What will {player.name} do?".center(70))
         #   selection = input(f"\n1) Light Swing - deals moderate physical damage.\n2) Heavy Swing - deals heavy physical damage.\n3) Meditate - moderately restores your health.")
          #  while selection != "1" and selection != "2" and selection != "3":
           #     print("Unrecognized selection. Please choose 1) Light Swing or 2) Heavy Swing 3) Meditate")
            #    selection = input(f"Which action will {player.name} take?  {player.name} has {player.health} health. {enemy.name} has {enemy.health} health.\n\n 1) Light Swing\n 2) Heavy Swing\n 3) Meditate")
            #if selection == "1":
             #   attack = random.randint(0,8)
              #  if attack <= 7:
               #     player.light_swing(enemy)
                #    if enemy.health > 0:
                 #       enemy.warrior_counterattack(player)
                #else:
                 #   print(BORDER)
                  #  print(f"{player.name} missed".center(70))
                   # print(BORDER)
                    #if enemy.health > 0:
                     #   enemy.warrior_counterattack(player)
            #elif selection == "2":
             #   attack = random.randint(0,8)
              #  if attack <= 7:
               #     player.heavy_swing(enemy)
                #    if enemy.health > 0:
                 #       enemy.warrior_counterattack(player)
                #else:
                 #   print(BORDER)
                  #  print(f"{player.name} missed".center(70))
                   # print(BORDER)
                    #if enemy.health > 0:
                     #   enemy.warrior_counterattack(player)
            #elif selection == "3":
             #   player.meditate()
              #  if enemy.health > 0:
               #     enemy.warrior_counterattack(player)
    #elif isinstance(player, Wizard) and isinstance(enemy, Wizard):  
     #   while enemy.health > 0 and player.health > 0:
      #      time.sleep(0.5)
       #     print(f"{player.name}-- Health: {player.health} , Mana: {player.resource} // {enemy.name}-- Health: {enemy.health} , Mana: {enemy.resource}".center(70))
        #    print(f"What will {player.name} do?".center(70))
         #   selection = input(f"\n1) Cast Fireball - deals moderate fire damage.\n2) Cast Lightning - deals heavy lightning damage.\n3) Healing Wave = moderately replenishes your health.\n")
          #  while selection != "1" and selection != "2" and selection != "3":
           #     print("Unrecognized selection. Please choose 1 to Cast Fireball or 2 to Cast Lightning or 3 to Cast Healing Surge\n")
            #    selection = input(f"Which action will {player.name} take?  {player.name} has {player.health} health.\n {enemy.name} has {enemy.health} health.\n\n 1) Cast Fireball\n 2) Cast Lightning\n 3) Healing Surge")
            #if selection == "1":
             #   attack = random.randint(0,8)
              #  if attack <= 7:
               #     player.cast_fireball(enemy)
                #    if enemy.health > 0:
                 #       enemy.wizard_counterattack(player)
                #else:
                 #   print(BORDER)
                  #  print(f"{player.name} missed".center(70))
                   # print(BORDER)
                    #if enemy.health > 0:
                     #   enemy.wizard_counterattack(player)
           # elif selection == "2":
            #    attack = random.randint(0,8)
             #   if attack <= 7:
              #      player.cast_lightning(enemy)
               #     if enemy.health > 0:
                #        enemy.wizard_counterattack(player)
                #else:
                 #   print(BORDER)
                  #  print(f"{player.name} missed".center(70))
                   # print(BORDER)
                    #if enemy.health > 0:
                     #   enemy.wizard_counterattack(player)
           # elif selection == "3":
            #    player.healing_wave()
             #   if enemy.health > 0:
              #      enemy.wizard_counterattack(player)
            

