from distutils.log import info
import sys
import turtle
import random
import os

screen = turtle.getscreen()
WIDTH = 400
HEIGHT = 400
screen.setup(WIDTH, HEIGHT, 0, 0)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.delay(delay=0)
pointer = turtle.Turtle(visible=False)
screen.bgpic('br.gif')
screen.update()
pointer.up()




print("Before we get started, Please create a blank .txt file on your computer and type the following information inside of it in this format:")
print("Name" + '\n' + 'Age')

file = input('Enter this files location on your computer: ')
file_open = open(file, 'r')
name_age_list = []
for line in file_open:
    name_age_list.append(line)
file_open.close()
player_name = name_age_list[0].strip()

try:
    age = int(name_age_list[1])
except:
    sys.exit('Enter an actual number forhead')

print('\n' + 'Hello ' + player_name + '. Considering your age of ' + str(age))


if age <= 0:
    print('Okay so you are either a liar or lacking in the thought department')
elif age < 10:
    print('Are you even sure that you can use a computer?')
elif age >= 10 and age < 18:
    print('You should get some parent supervision before you start playing')
elif age >= 18 and age <= 100:
    print('Alright I think you can play')
else:
    print('You are not a real person')


print( '\n' + 'You start off with 100 life points which will be displayed in your life file. After an update happens in game you will have to reopen your life file to see it')


def life_points_calc(life_points,change):
    life_new = life_points + change
    return life_new

def mana_points_calc(mana_points,change):
    mana_new = mana_points + change
    return mana_new

def info_write(life_points,mana_points,):
    with open(file, 'w') as f:
        line1 = "Life:" + str(life_points) + '\n'
        line2 = "Mana:" + str(mana_points)
        
        f.writelines([line1,line2])
        
def life_info():
    return life_points

def mana_info():
    return mana_points

life_points = life_points_calc(100, 0)
mana_points = mana_points_calc(50, 0)
info_write(life_points,mana_points)

points_question = input('check your file to see your life points. Does it say 100? (type yes)')

if points_question == 'yes':
    print( '\n' + 'I already knew that but thank you. Ill give you an extra life and mana point for that')
    life_points = life_points_calc(life_points,1)
    mana_points = mana_points_calc(mana_points, 1)
    info_write(life_points,mana_points)
else:
    print('\n' + 'You are a liar and im taking away 2 life and mana points because I can')
    life_points = life_points_calc(life_points,-2)
    mana_points = mana_points_calc(mana_points, -2)
    info_write(life_points,mana_points)



# starting combat stuff


#normal enemy list (will extend after base gameplay is semi-solid)
enemy_dict = {'vampire' : 20, 'troll' : 10, 'dragon' : 30, 'slime' : 5, 'skeleton': 15}
enemy_list_1 = []

for key, value in enemy_dict.items():
    enemy_list_1.append(key + ':' + str(value))
enemy_list = [x.split(':') for x in enemy_list_1]

# all functions to help with combat (story functions to come later)
def enemy_selector(enemy_list):
    list_length = len(enemy_list)
    location = random.randrange(0, list_length,1)
    enemy_name = enemy_list[location][0]
    enemy_health = enemy_list[location][1]
    return enemy_name, enemy_health



def enemy_file_create(enemy_name,enemy_health):
    file_name = 'C:\game folder\\' + str(enemy_name) + '.txt'
    enemy_file = open(file_name, 'w')
    enemy_file.write(enemy_health)
    enemy_file.close()
    return file_name


def battle_visual(enemy_name):
    pointer.goto(100,200)
    pointer.write(str(player_name), move = False, align = 'center', font=('Arial',30,'normal'))
    pointer.up()
    pointer.goto(200,200)
    pointer.write('VS', move = True, align = 'center', font=('Arial',20,'normal'))
    pointer.up()
    pointer.goto(310,200)
    pointer.write(str(enemy_name), move = True, align = 'center', font=('Arial',30,'normal'))
    pointer.up()
    return None

def window_clear():
    pointer.clear()
    screen.bgpic('br.gif')
    screen.update()
    pointer.up()


def enemy_attacks():
    enemy_attack_dict =  {'bite' : -20, 'roar' : -10, 'claw' : -15 }
    enemy_attack_list = []
    for key, value in enemy_attack_dict.items():
        enemy_attack_list.append(key + ': ' + str(value))
    enemy_attack_list = [l.split(':') for l in enemy_attack_list]
    enemy_list_len = len(enemy_attack_list)
    choice_attack = random.randrange(0, enemy_list_len,1)
    return enemy_attack_list



def battle(remaining_hp, enemy_name, enemy_file, life_points, mana_points):
    life_points = life_points
    ef = enemy_file
    enemy_hp = remaining_hp
    print('You are fighting a ' + enemy_name + ' with ' + str(remaining_hp) + ' health left!')
    battle_visual(enemy_name)
    attack = input('What attck would you like to use? (stab, slash, excecute)')
    if attack == 'stab':
        damage = 3
        life_cost = -3
        mana_cost = -3
    if attack == 'slash':
        damage = 8
        life_cost = -6
        mana_cost = -5
    if attack == 'excecute':
        damage = 15
        life_cost = -10
        mana_cost = -15
    print('Used ' + attack + '!')
    attack_visual_player(attack)

    enemy_hp = str(int(enemy_hp) - damage)
    file_add = open(ef,'w')
    file_add.write('life: ' + str(enemy_hp))
    file_add.close()
    life_points = life_points_calc(life_points,life_cost)
    mana_points = mana_points_calc(mana_points,mana_cost)
    info_write(life_points,mana_points)
    print('Did ' + str(damage) + ' damage to ' + enemy_name + ' which costed ' + str(abs(life_cost)) + ' life points' + ' and ' + str(abs(mana_cost)) + ' mana points\n')
    
    enemy_battle_list = enemy_attacks()
    choice_attack = random.randrange(0, len(enemy_battle_list), 1)
    enemy_attack_name = enemy_battle_list[choice_attack][0]
    enemy_attack_damage = int(enemy_battle_list[choice_attack][1])
    print(enemy_name + ' Used ' + enemy_attack_name)
    attack_visual_enemy(enemy_attack_name)
    life_points = life_points_calc(life_points, enemy_attack_damage)
    info_write(life_points,mana_points)
    print(enemy_name + ' did ' + str(abs(enemy_attack_damage)) + ' damage to ' + player_name + '\n')
    print(player_name + ' now has ' + str(life_points) + ' life points and' + str(mana_points) + ' left\n')
    return enemy_hp, life_points, mana_points

def attack_visual_player(attack):
    pointer.goto(100,100)
    pointer.dot(120,'white')
    pointer.up()
    pointer.write(str(attack), move = True, align = 'center', font=('Arial',20,'normal'))
    pointer.up()
    return None

def attack_visual_enemy(enemy_attack_name):
    pointer.goto(310,100)
    pointer.dot(120,'white')
    pointer.up()
    pointer.write(str(enemy_attack_name), move = True, align = 'center', font=('Arial',20,'normal'))
    pointer.up()
    return None


# actual combat using function(lol short)

def encounter():
    life_points = life_info()
    mana_points = mana_info()
    en, enemy_hp = enemy_selector(enemy_list)
    ef = enemy_file_create(en,enemy_hp)
    enemy_hp, life_points, mana_points = battle(enemy_hp,en,ef,life_points, mana_points)
    while int(enemy_hp) > 0:
       enemy_hp, life_points, mana_points = battle(enemy_hp, en,ef,life_points,mana_points)
    print(en + ' has died. Good job!' + '\n')
    os.remove(ef)
    window_clear()

#2 test encounters to see if file writing works
encounter()
#encounter()

#using input enter to stop turtle from closing after monster has died (will use click to exit when im not lazy)
#input('enter')


# TIME FOR A STORY
player_birthday_age = int(age) + 1
print('It was an tragedy when you ' + player_name + ' died when you were struck by a car the day before your ' + str(player_birthday_age) + 'th birthday.')
print('Becasue of the timing of your death, the grim reaper decided to give you a chance to redeem yourself. Dont kid yourself. Your are dead. But maybe thats where your bad luck ends')
print('If you are able to fight through all of the circles of hell, you will be brought back to life and be abllowed to resume your mediocre existance')

pointer.goto(200,200)
pointer.write('FIRST CIRCLE', move = False, align = 'center', font = ('Lobster',30,'italic'))
pointer.up()
pointer.goto(200,100)
pointer.write('LIMBO', move = False, align = 'center', font = ('Lobster',20,'italic'))
#pointer.write(str(enemy_attack_name), move = True, align = 'center', font=('Arial',20,'normal'
print('You have entered Limbo the first Circle of hell.')
input('enter')