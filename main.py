#!/usr/bin/env python3
from os import system, chdir, path, mkdir
from sys import argv

CODING_PATH = "/Users/shane/coding/"
SCHOOL_PATH = "/Users/shane/dropbox/school/fall2021/"
DEFAULTS_PATH = CODING_PATH + 'python/AutoProj/defaults/'
new_cmd = 'new_tab'

CPP_EXTS = ['c', 'cpp', 'c++']
PYTHON_EXTS = ['p', 'py', 'pyth', 'python']
JAVA_EXTS = ['j', 'jv', 'java']
WEB_EXTS = ['w', 'web', 'html', 'css', 'js', 'javascript']
RUST_EXTS = ['r', 'rs', 'rust']
ALL_EXTS = CPP_EXTS + PYTHON_EXTS + JAVA_EXTS + WEB_EXTS + RUST_EXTS

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
        except ValueError: pass
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
    mkdir(path)
    system(f'{new_cmd} {path} \'cp -r {DEFAULTS_PATH}c++/* .&&vim makefile src/main.cpp -O\'')

def make_new_python(name):
    bot = yes_or_no("Is this a discord bot?")
    path = CODING_PATH + "python/"
    if bot:
        path += "discordbots/"
    path += name
    print(path)
    mkdir(path)
    system(f'{new_cmd} {path} vim main.py')

def make_new_java(name):
    path = CODING_PATH + "java/"
    if yes_or_no("Is this for school?"):
        path = SCHOOL_PATH + "comp/"
    path += name
    mkdir(path)
    chdir(path)
    system(f'{new_cmd} {path} \'cp -r {DEFAULTS_PATH}java/* .&& vim * -O\'')

def make_new_web(name):
    PlainJS = yes_or_no("Is this plain javascript")
    path = CODING_PATH + "web/"
    if PlainJS:
        path += "JustJS/"
    path += name
    mkdir(path)
    chdir(path)
    if PlainJS:
        system(f'{new_cmd} {path} vim sketch.js')
    else:
        system(f'{new_cmd} {path} \'cp {DEFAULTS_PATH}/web/index.html .&& chmod 777 index.html&& vim index.html index.css index.js -O\'')

def make_new_rust(name):
    path = CODING_PATH + "rust/"
    chdir(path)
    system(f'{new_cmd} {path} \'cargo new {name}&& cd {name}&& vim Cargo.toml src/main.rs -O\'')

def parse_argv():
    try:
        projType, projName = argv[1:3]
    except:
        projType = argv[1]
        if projType not in ALL_EXTS:
            print("ERROR: A project type with that name does not exist")
            return
        projName = input("Enter Name: ")
    if projType.lower() in CPP_EXTS:
        make_new_c(projName)
    elif projType.lower() in PYTHON_EXTS:
        make_new_python(projName)
    elif projType.lower() in JAVA_EXTS:
        make_new_java(projName)
    elif projType.lower() in WEB_EXTS:
        make_new_web(projName)
    elif projType.lower() in RUST_EXTS:
        make_new_rust(projName)
    else:
        print("ERROR: A project type with that name does not exist")

def main():
    """Driver Code"""
    if '-w' in argv:
        argv.remove('-w')
        global new_cmd
        new_cmd = 'new_window'
    if len(argv) < 2:
        make_new()
    else:
        parse_argv()

if (__name__ == "__main__"):
    main()
