from os import system
from msvcrt import getch

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
    if choice == 1:
        makeNewC()
    elif choice == 2:
        makeNewPython()
    elif choice == 3:
        makeNewJava()
    elif choice == 4:
        makeNewWeb()
    elif choice == 5:
        makeNewRust()


def makeNewC():
    pass

def makeNewPython():
    pass

def makeNewJava():
    pass

def makeNewWeb():
    pass

def makeNewrust():
    pass

def makeNewRust():
    pass

makeNew()
