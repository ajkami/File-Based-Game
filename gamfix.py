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


print('\n' + 'now make a new file in the same folder as the other file. THIS FILE IS YOUR LIFE. DO NOT LOSE IT')
file_new = input('Enter your life files location here (remember this): ')
file_life = open(file_new, 'w')

print( '\n' + 'You start off with 100 life points which will be displayed in your life file. After an update happens in game you will have to reopen your life file to see it')


def life_points_write(file_new,life_points,change):
    life_new = life_points + change
    file_life = file_new
    file_new.write(str(life_new))
    return life_new

life_points = life_points_write(file_life, 100, 0)

points_question = input('check your file to see your life points. Does it say 100? (type yes)')

if points_question == 'yes':
    print( '\n' + 'I already knew that but thank you. Ill give you an extra life point for that')
    life_points = life_points_write(file_life,life_points,1)
else:
    print('\n' + 'You are a liar and im taking away 2 life points because I can')
    life_points = life_points_write(file_life,life_points,-2)

# starting combat stuff

enemy_dict = {'vampire' : 20, 'troll' : 10, 'dragon' : 30, 'slime' : 5, 'skeleton': 15}
enemy_list_1 = []

for key, value in enemy_dict.items():
    enemy_list_1.append(key + ':' + str(value))
enemy_list = [x.split(':') for x in enemy_list_1]

def enemy_selector(enemy_list):
    list_length = len(enemy_list)
    location = random.randrange(0, list_length,1)
    enemy_name = enemy_list[location][0]
    enemy_health = enemy_list[location][1]
    return enemy_name, enemy_health


def battle_generator(enemy_list):
    name,health = enemy_selector(enemy_list)
    enemy_file = open(name + '.txt', 'w')
    enemy_file.write(health)
    print(name,health)
    return enemy_file, name, health


def battle_visual(enemy_list):
    monster_name, monster_health = enemy_selector(enemy_list)
    pointer.goto(100,200)
    pointer.write(str(player_name), move = False, align = 'center', font=('Arial',30,'normal'))
    pointer.up()
    pointer.goto(200,200)
    pointer.write('VS', move = True, align = 'center', font=('Arial',20,'normal'))
    pointer.up()
    pointer.goto(310,200)
    pointer.write(str(monster_name), move = True, align = 'center', font=('Arial',30,'normal'))

#pointer.write("No Intersect!", move=False, align ="center", font=("Arial",20,"normal"))

def battle(enemy_list):
    battle_visual(enemy_list)
    enemy_file_name, name, health = battle_generator(enemy_list)
    life_points_write(enemy_file_name,int(health),-5)
    print('Did 5 damage to ' + name)
    return None

'''
def death_check(enemy_list):
    file = battle_generator(enemy_list)
    for line in file:
        if line == 0:
            os.remove(file)
            print('monster died')
'''     
battle(enemy_list)
input('Enter whatever')


#death_check(enemy_list)