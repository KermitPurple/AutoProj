#!/usr/bin/env python3
from os import system, chdir, path
from sys import argv

CODING_PATH = "/Users/shane/coding/"
SCHOOL_PATH = "/Users/shane/dropbox/school/fall2021/"

def yes_or_no(prompt: str) -> bool:
    """Asks the user for input and returns a boolean
    :prompt: The question to be posed to the user
    :returns: True if yes, false if no
    """
    while 1:
        response = input(f'{prompt} (yes, no)> ').lower()
        if response == 'y' or response == 'yes':
            return True
        elif response == 'n' or response == 'no':
            return False

def get_int_between(low: int, high: int) -> int:
    """gets and validates user input. returns a valid int
    :low: the lowest the validated input can be
    :high: the highest the validated input can be
    :returns: An integer chosen by the user in the range
    """
    if low > high:
        raise ValueError("Low cannot be greater than high")
    while 1:
        try:
            num = int(input(f'Enter an integer between {low}, and {high}> '))
            if low <= num <= high:
                return num
        except: pass
    return num

def get_name() -> str:
    """Get and validate user input for a name
    :returns: validated name
    """
    while 1:
        name = input("Enter Name> ")
        if len(name.split()) <= 1:
            break
        print("Please make it one god damn word")
    return name

def make_new():
    print("1) New C++ Project")
    print("2) New Python Project")
    print("3) New Java Project")
    print("4) New web Project")
    print("5) New rust Project")
    print("6) Cancel")
    choice = get_int_between(1, 6)
    if choice != 6:
        name = get_name()
        if choice == 1:
            make_new_c(name)
        elif choice == 2:
            make_new_python(name)
        elif choice == 3:
            make_new_java(name)
        elif choice == 4:
            make_new_web(name)
        elif choice == 5:
            make_new_rust(name)

def make_new_c(name):
    path = CODING_PATH + "c++/"+ name + "/"
    print(path)
    system("mkdir " + path)
    chdir(path)
    system("cd " + path)
    system("cp -r \"" + CODING_PATH +"python/autoproj/defaults/c++/makefile\" .")
    system("cp -r \"" + CODING_PATH +"python/autoproj/defaults/c++/src\" .")
    system("cp -r \"" + CODING_PATH +"python/autoproj/defaults/c++/.ycm_extra_conf.py\" .")
    system("vim -O makefile src/main.cpp")

def make_new_python(name):
    bot = yes_or_no("Is this a discord bot?")
    path = CODING_PATH + "python/"
    if bot:
        path += "discordbots/"
    path += name
    system("mkdir "+path)
    chdir(path)
    system("vim main.py")

def make_new_java(name):
    path = CODING_PATH + "java/"
    if yes_or_no("Is this for school?"):
        path = SCHOOL_PATH + "comp/"
    path += name
    system("mkdir " + path)
    chdir(path)
    system("cp -r \"" + CODING_PATH + "python/autoproj/defaults/java/makefile\" .")
    system("cp -r \"" + CODING_PATH + "python/autoproj/defaults/java/Main.java\" .")
    system("vim * -O")


def make_new_web(name):
    PlainJS = yes_or_no("Is this plain javascript")
    path = CODING_PATH + "web/"
    if PlainJS:
        path += "JustJS/"
    path += name
    system("mkdir "+path)
    chdir(path)
    if PlainJS:
        system("vim sketch.js")
    else:
        system("cp " + CODING_PATH + "python/autoproj/defaults/web/index.html .")
        system("chmod 777 index.html");
        system("touch index.css")
        system("touch index.js")
        system("vim * -O")

def make_new_rust(name):
    path = CODING_PATH + "rust/"
    chdir(path)
    system("cargo new " + name)
    chdir(path + name)
    system("vim Cargo.toml src/main.rs -O")

def parse_argv():
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
        make_new_c(projName)
    elif projType.lower() in pythonList:
        make_new_python(projName)
    elif projType.lower() in javaList:
        make_new_java(projName)
    elif projType.lower() in webList:
        make_new_web(projName)
    elif projType.lower() in rustList:
        make_new_rust(projName)
    else:
        print("ERROR: A project type with that name does not exist")

def main():
    """Driver Code"""
    if len(argv) < 2:
        make_new()
    else:
        parse_argv()

if (__name__ == "__main__"):
    main()
