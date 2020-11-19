from os import system, chdir
from msvcrt import getch
from sys import argv

CODING_PATH = "C:\\users\\shane\\desktop\\coding\\"

def YesOrNo():
    print("(Y/N)")
    while 1:
        try:
            choice = getch().decode("utf-8").lower()
            if choice == 'y':
                return True
            elif choice == 'n':
                return False
            else:
                raise
        except:
            print("Please Enter y or n")

def makeNew():
    print("1) New C++ Project")
    print("2) New Python Project")
    print("3) New Java Project")
    print("4) New web Project")
    print("5) New rust Project")
    print("6) Cancel")
    while 1:
        try:
            choice = int(getch().decode("utf-8"))
            if choice > 6:
                raise
            break
        except:
            print("enter valid number")
    if choice != 6:
        name = input("Enter Name: ")
        if choice == 1:
            makeNewC(name)
        elif choice == 2:
            makeNewPython(name)
        elif choice == 3:
            makeNewJava(name)
        elif choice == 4:
            makeNewWeb(name)
        elif choice == 5:
            makeNewRust(name)

def makeNewC(name):
    print("Is this a personal project", end="")
    personal = YesOrNo()
    path = ""
    if personal:
        path = CODING_PATH + "c++\\"+name
    else:
        path = "C:\\users\\shane\\dropbox\\school\\fall2020\\cs\\"+name
    system("md " + "\"" + path + "\"")
    chdir(path)
    system("cp -r \"" + CODING_PATH +"python\\autoproj\\defaults\\c++\\makefile\" .")
    system("cp -r \"" + CODING_PATH +"python\\autoproj\\defaults\\c++\\src\" .")
    system("cp -r \"" + CODING_PATH +"python\\autoproj\\defaults\\c++\\.ycm_extra_conf.py\" .")
    system("start gvim -O makefile src\\main.cpp")

def makeNewPython(name):
    print("Is this a discord bot?", end="")
    bot = YesOrNo()
    path = CODING_PATH + "python\\"
    if bot:
        path += "discordbots\\"
    path += name
    system("md "+path)
    chdir(path)
    system("start gvim main.py")

def makeNewJava(name):
    print("not implimented yet")

def makeNewWeb(name):
    print("Is this plain javascript", end="")
    PlainJS = YesOrNo()
    path = CODING_PATH + "web\\"
    if PlainJS:
        path += "JustJS\\"
    path += name
    system("md "+path)
    chdir(path)
    if PlainJS:
        system("start gvim sketch.js")
    else:
        system("cp " + CODING_PATH + "python\\autoproj\\defaults\\web\\index.html .")
        system("chmod 777 index.html");
        system("touch styles.css")
        system("touch sketch.js")
        system("gexit")

def makeNewRust(name):
    path = CODING_PATH + "rust\\"
    chdir(path)
    system("cargo new " + name)
    chdir(path + name)
    system("start gvim src/main.rs")

def parseArgv():
    try:
        projType, projName = argv[1:3]
    except:
        projType = argv[1]
        projName = input("Enter Name: ")
    cppList = ['c', 'cpp', 'c++']
    pythonList = ['p', 'py', 'pyth', 'python']
    javaList = ['j', 'jv', 'java']
    webList = ['w', 'web', 'html', 'css', 'js', 'javascript']
    rustList = ['r', 'rs', 'rust']
    if projType.lower() in cppList:
        makeNewC(projName)
    elif projType.lower() in pythonList:
        makeNewPython(projName)
    elif projType.lower() in javaList:
        makeNewJava(projName)
    elif projType.lower() in webList:
        makeNewWeb(projName)
    elif projType.lower() in rustList:
        makeNewRust(projName)
    else:
        print("ERROR: A project type with that name does not exist")


if (__name__ == "__main__"):
    if(len(argv) < 2):
        makeNew()
    else:
        parseArgv()
