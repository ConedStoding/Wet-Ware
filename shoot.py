#shoot function for combat module

import random
def shoot():
    global gangerStats


    gangerStats[0] = int(gangerStats[0]) - int(weaponGlock)

    print('You hit enemy for ' + str(weaponGlock))
    if int(gangerStats[0]) <= 0:
        print('You have eliminated the enemy!')
        print('A new enemy enters the room.')
        gangerStats[0] = 65

    else:
        print('The enemy has, ' + str(gangerStats[0]) + ' health points left.')
#declare globals

entity = [1, 0] #player always  = 1
playerStats = [100] #just a health stat for staring simple
gangerStats = [65] #health
weaponGlock = 30 #example weapon damage
commandDict = {
'shoot': 'Attack With a gun',
'cover': 'Crouch or take cover from enemy fire',
'commands': 'shoot' 'crouch'
}
command = ''
print('A grim looking street-rude enters the room. ')
print('He flexes his gun arm.')
shoot()