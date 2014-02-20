import random
import pygame, sys
from pygame.locals import *
import time

pygame.init()


#declare globals
name = ' '
entity = [1, 0] #player always  = 1
playerStats = playerStats = [65, 10, 1, 2, 5, 6] #just a health stat for staring simple
enemyStats = [65] #health
weaponGlock = 30 #example weapon damage
theBoard = [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ']
playerInitial = name[0]

boardSpawn = [1,  2,  3,  4,  5,  6,  7,  14,  21,  28,  27,  26,  25,  24,  23,  22,  15,  8]
global locale
locale = random.choice(boardSpawn)

theBoard[int(locale)] = playerInitial
commandDict = {
'shoot': 'You shoot.',
'cover': 'You stay low avoiding gun fire.',
'commands': 'shoot,' ' cover,' ' commands,' ' help,' ' look,'
' forward,' ' back,' ' left,' ' right,',
'help': 'Type "commands" for a list of commands',
'look': 'You take in the scene',
'forward': 'You move forward',
'back': 'You move back',
'left': 'You move to the left',
'right': 'You move to the right',
'stats': 'Select stats to allocate experience points to.'
}

def drawBoard(board):
    # This function prints out the board that it was passed.
    # "board" is a list of 29 strings representing the board (ignore index 0)
    print('|---+---+---+---+---+---+---|')
    print('|   |   |   |   |   |   |   |')
    print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' | ' + board[7] + ' | ')
    print('|   |   |   |   |   |   |   |')
    print('|---+---+---+---+---+---+---|')
    print('|   |   |   |   |   |   |   |')
    print('| ' + board[8] + ' | ' + board[9] + ' | ' + board[10] + ' | ' + board[11] + ' | ' + board[12] + ' | ' + board[13] + ' | ' + board[14] + ' | ')
    print('|   |   |   |   |   |   |   |')
    print('|---+---+---+---+---+---+---|')
    print('|   |   |   |   |   |   |   |')
    print('| ' + board[15] + ' | ' + board[16] + ' | ' + board[17] + ' | ' + board[18] + ' | ' + board[19] + ' | ' + board[20] + ' | ' + board[21] + ' | ')
    print('|   |   |   |   |   |   |   |')
    print('|---+---+---+---+---+---+---|')
    print('|   |   |   |   |   |   |   |')
    print('| ' + board[22] + ' | ' + board[23] + ' | ' + board[24] + ' | ' + board[25] + ' | ' + board[26] + ' | ' + board[27] + ' | ' + board[28] + ' | ')
    print('|   |   |   |   |   |   |   |')
    print('|---+---+---+---+---+---+---|')


def commandHandle():

#list of commands that validate against the main dictionary
    while True:

        command = input('Enter a command:')
        if command in commandDict:
            command = str(commandDict[command])
        if command == str(commandDict['shoot']):
            print(command)
            shoot()
        elif command == str(commandDict['cover']):
            print(command)
        elif command == str(commandDict['commands']):
            print(command)
        elif command == str(commandDict['help']):
            print(command)
        elif command == str(commandDict['look']):
            print(command)
        elif command == str(commandDict['forward']):
            print(command)
        elif command == str(commandDict['back']):
            print(command)
        elif command == str(commandDict['left']):
            print(command)
        elif command == str(commandDict['right']):
            print(command)
        elif command == str(commandDict['stats']):
            rollPlayerStats()
        else:
            print('that is not a valid command')
# system for allocating xp to different stats
def rollPlayerStats():
    global playerStats
    print('''attributes:
health, accuracy, wounds, movement, technology and experience''')
    print(playerStats)
    stat = input('''Type the name of the stat you would
like to increase. Type exit to leave stats menu:
''')
    if playerStats[5] <= 0:
        print('You have no experince points to allocate.')
    elif stat == 'health':
        stat = int(input('How many experience points would you like to allocate?'))
        if playerStats[5] >= stat:
            playerStats[5] = playerStats[5] - stat
            playerStats[0] = playerStats[0] + stat
            print('You now have ' + str(playerStats[0]) + ' health.')
        else:
            print('Not enough points to make that allocation.')
    elif stat == 'accuracy':
        stat = int(input('How many experience points would you like to allocate?'))
        if playerStats[5] >= stat:
            playerStats[5] = playerStats[5] - stat
            playerStats[1] = playerStats[1] + stat
            print('You now have ' + str(playerStats[1]) + ' accuracy.')
        else:
            print('Not enough points to make that allocation.')
    elif stat == 'movement':
        stat = int(input('How many experience points would you like to allocate?'))
        if playerStats[5] >= stat:
            playerStats[5] = playerStats[5] - stat
            playerStats[3] = playerStats[3] + stat
            print('You now have ' + str(playerStats[3]) + ' movement.')
        else:
            print('Not enough points to make that allocation.')
    elif stat == 'technology':
        stat = int(input('How many experience points would you like to allocate?'))
        if playerStats[5] >= stat:
            playerStats[5] = playerStats[5] - stat
            playerStats[4] = playerStats[4] + stat
            print('You now have ' + str(playerStats[4]) + ' technology.')
        else:
            print('Not enough points to make that allocation.')
    elif stat == 'exit':
        print('You exit the stats menu.')
    else:
        print('''Either the command was not recognised,
or the stat you selected isn't increasible
with experience points.
''')

#simple function to allow player to shoot enemies and take their helth down
def shoot():
    global enemyStats


    enemyStats[0] = int(enemyStats[0]) - int(weaponGlock)

    print('You hit enemy for ' + str(weaponGlock))
    if int(enemyStats[0]) <= 0:
        print('You have eliminated the enemy!')
        print('A new enemy enters the room.')
        enemyStats[0] = 65

    else:
        print('The enemy has, ' + str(enemyStats[0]) + ' health points left.')


pygame.init()
#load game music
pygame.mixer.music.load('textadventureone.mp3')
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(-1, 0.0)
time.sleep(1)

print('''
 _ _ _  ___  ___   _ _ _   _   ___ ___
| | | || __||_ _| | | | | / \ | o \ __|
| V V || _|  | |  | V V || o ||   / _|
 \_n_/ |___| |_|   \_n_/ |_n_||_|\\____|
''')
time.sleep(3)
name = input('Enter your name:')

print(drawBoard(theBoard))
commandHandle()
