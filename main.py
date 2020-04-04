from os import system, chdir
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
        path = "C:\\users\\shane\\dropbox\\desktop\\coding\\c++\\"+name
    else:
        path = "C:\\users\\shane\\dropbox\\desktop\\school\\senior year\\semester 2\\cs\\"+name
    system("md " + "\"" + path + "\"")
    chdir(path)
    system("cp -r \"C:\\users\\shane\\dropbox\\desktop\\coding\\defaults\\c++\\makefile\" .")
    system("cp -r \"C:\\users\\shane\\dropbox\\desktop\\coding\\defaults\\c++\\src\" .")
    system("cp -r \"C:\\users\\shane\\dropbox\\desktop\\coding\\defaults\\c++\\bin\" .")
    system("cp -r \"C:\\users\\shane\\dropbox\\desktop\\coding\\defaults\\c++\\include\" .")
    system("g src\\main.cpp")

def makeNewPython(name):
    print("Is this a discord bot?", end="")
    bot = YesOrNo()
    if bot:
        path = "C:\\users\\shane\\dropbox\\desktop\\coding\\python\\discordbots\\"+name
    else:
        path = "C:\\users\\shane\\dropbox\\desktop\\coding\\python\\"+name
    system("md "+path)
    chdir(path)
    system("g main.py")

def makeNewJava(name):
    print("not implimented yet")

def makeNewWeb(name):
    print("Is this plain javascript", end="")
    bot = YesOrNo()
    if bot:
        path = "C:\\users\\shane\\dropbox\\desktop\\coding\\web\\JustJS\\"+name
    else:
        path = "C:\\users\\shane\\dropbox\\desktop\\coding\\web\\"+name
    system("md "+path)
    chdir(path)
    system("cp C:\\Users\\Shane\\Dropbox\\Desktop\\Coding\\defaults\\web\\index.html .")
    system("touch styles.css")
    system("touch sketch.js")
    system("gexit")

def makeNewRust(name):
    print("not implimented yet")

makeNew()
