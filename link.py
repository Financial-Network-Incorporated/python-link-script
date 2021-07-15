import os
import json
import time

sleep = time.sleep

print("Checking for config file...\n")

if os.path.exists('config.txt'):

    config = open("config.txt", "r")
    configDir = config.read()


    if len(configDir) <= 1:
        print("Config found, but is empty. If you would like to run this application from another directory, paste the directory of your project files plainly in './config.txt'.\n\nUsing relative path.\n\n")
        dir_path = os.path.dirname(os.path.realpath(__file__)) 
    else:
        print("Config found, using specified directory.\n\n")
        dir_path = configDir
else:
    print('Config not found, creating one...\n')
    config = open("config.txt", 'w+')
    config.close()
    dir_path = os.path.dirname(os.path.realpath(__file__)) 
config.close()

    
print('Working directory: {}'.format(dir_path))

prevDir = ''

clear = lambda: os.system('clear')

def pushd(newDir):
    global prevDir
    prevDir = os.getcwd()
    os.chdir(newDir)

def popd():
    global prevDir
    os.chdir(prevDir)
    prevDir = ''

def ex(command):
    if type(command) == str:
        os.system(command)
    else:
        print("{} is not of type 'String'")

def link():
    clear()
    tempDirs = os.listdir(dir_path)
    dirs = []
    counter = 0
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    for dir in tempDirs:
        if os.path.isdir('{}/{}'.format(dir_path, dir)):
            dirs.append('{}/{}'.format(dir_path,dir))
            print("{} - {}".format(counter, dir))
            counter += 1

    userInp = int(input("\nType the number of the PARENT directory you are working with and press enter: "))
    parentDir = dirs[userInp]
    userInp = int(input("\nType the number of the CHILD directory you are linking and press enter: "))
    childDir = dirs[userInp]


    print('dir_path:' + dir_path)
    print('childDir: ' + childDir)
    #open package.json in child dir
    pushd(childDir)
    f = open('package.json', 'r')
    data = json.load(f)
    f.close()

    #grab list of peer dependencies
    peerDep = data['peerDependencies']
    peerDep = peerDep.keys()

    childProjName = data['name']


    #enter parent dir
    os.chdir(parentDir)

    # linking
    for dep in peerDep:
        pushd('node_modules/{}'.format(dep))

        print(os.getcwd())
        ex('yarn unlink')
        ex('yarn link')

        popd()

    

    # get link from yarn for each peer dep, then link child project to yarn

    pushd(childDir)
    print('\n')
    print(os.getcwd())

    for dep in peerDep:
        ex('yarn link {}'.format(dep))

    ex('yarn unlink')
    ex('yarn link')
    os.chdir(parentDir)
    ex('yarn link {}'.format(childProjName))


def unlink():
    print("Unlink is still in development.")


def start():

    initialInput = input("\n1 - Linking\n2 - UNlinking\nAre you linking or UNlinking?: ")

    if initialInput.isdigit():
        if int(initialInput) == 1:
            link()
        elif int(initialInput) == 2:
            unlink()
        else:
            print('{} is not one of the listed options above.\n'.format(initialInput))
            start()
    else:
        print('{} is not one of the listed options above.\n'.format(initialInput))
        start()


start()



