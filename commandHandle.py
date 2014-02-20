def commandHandle():

    while True:

        command = input('Enter a command')
        if command in commandDict:
            command = str(commandDict[command])
        if command == str(commandDict['shoot']):
            print('You shoot.')
            #shoot()
        elif command == str(commandDict['cover']):
            print('You take cover.')
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
        else:
            print('that is not a valid command')

commandHandle()