from distutils.log import info
import sys
import random
import os
from player import Player
from monsters import Slime, Troll, Skeleton, Vampire, Dragon

# Going to switch GUI to Tkinter

# will implement file later just cleaning up code with classes 

player = Player(100,100,0)
player.update()

vamp = Vampire(50,20)

vamp.attack(player)

player.update()


# slime = 1, troll = 2, skeleton = 3, vampire = 4, dragon = 5
# will have to change monster_num if more monsters are added later
monster_num = 5


# function that creates a random monster based on rand import 
# health and damage must be params for difficulty scaling 
def enemy_selector(health, damage):
    choice = random.randrange(1,(monster_num + 1),1)
    if choice == 1:
        monster = Slime(health, damage)
    elif choice == 2:
        monster = Troll(health, damage)
    elif choice == 3:
        monster = Skeleton(health, damage)
    elif choice == 4:
        monster = Vampire(health, damage)
    elif choice == 5:
        monster = Dragon(health,damage)
    return monster

monster = enemy_selector(10, 2)
print(player.get_name())




def battle():
    print('You are fighting a ' + monster.get_name() + ' with ' + str(monster.life) + ' health left!')
    
    while(monster.life > 0 and player.life > 0):
        attack = input('What attck would you like to use? (stab, slash, excecute)')
        if attack == 'stab':
            monster.life_loss(3)
            player.mana_loss(3)
            print('Used ' + attack + '!\n')
            print('Did ' + str(3) + ' damage to the ' + monster.get_name() + '!\n')

        elif attack == 'slash':
            monster.life_loss(8)
            player.mana_loss(5)
            print('Used ' + attack + '!\n')
            print('Did ' + str(8) + ' damage to the ' + monster.get_name() + '!\n')

        elif attack == 'execute':
            monster.life_loss(15)
            player.mana_loss(10)
            print('Used ' + attack + '!\n')
            print('Did ' + str(15) + ' damage to the ' + monster.get_name() + '!\n')
        
        print(player.update())
        print(monster.update())
        
    if (monster.life <= 0):
        print(monster.get_name() + ' has died!\n')
    elif(player.life <= 0):
        print('You have died!\n')
    
    return None
        
            
battle() 
        
    

