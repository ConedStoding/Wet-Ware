import random

playerStats = [65, 10, 1, 2, 5, 6]

def rollPlayerStats():
    global playerStats
    print('''attributes:
health, accuracy, wounds, movement, technology and experience''')
    print(playerStats)
    stat = input('''Type the name of the stat you would
like to increase:
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
    else:
        print('''Either the command was not recognised,
or the stat you selected isn't increasible
with experience points.
''')
