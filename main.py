#!/usr/bin/env python3
import TerminalGameTools as tgt
import os, argparse
from os import system, chdir, path, mkdir, environ
from sys import argv

CODING_PATH = environ['CODING_DIR']
SCHOOL_PATH = environ['SCHOOL_DIR']
DEFAULTS_PATH = os.path.join(CODING_PATH, 'python/AutoProj/defaults/')

CPP_EXTS = ['c', 'cpp', 'c++']
PYTHON_EXTS = ['p', 'py', 'pyth', 'python']
JAVA_EXTS = ['j', 'jv', 'java']
WEB_EXTS = ['w', 'web', 'html', 'css', 'js', 'javascript']
RUST_EXTS = ['r', 'rs', 'rust']
ALL_EXTS = CPP_EXTS + PYTHON_EXTS + JAVA_EXTS + WEB_EXTS + RUST_EXTS

new_cmd: str = 'new_tab'
g_repo: bool = False
gh_repo: bool = False
override_path: str | None = None

def get_name() -> str:
    '''
    Get and validate user input for a name
    :returns: validated name
    '''
    while 1:
        name = input('Enter Name> ')
        if len(name.split()) <= 1:
            break
        print('Please make it one god damn word')
    return name

def get_defaults_path(folder: str) -> str:
    '''
    :folder: str, foldername in DEFAULTS_PATH
    '''
    return os.path.join(DEFAULTS_PATH, f'{folder}/*')

def make_new():
    choice = tgt.give_options([
        'New c++ Project',
        'New python Project',
        'New java Project',
        'New web Project',
        'New rust Project',
        'Cancel'
    ])[0]
    if choice != 5:
        name = get_name()
        match choice:
            case 0:
                make_new_c(name)
            case 1:
                make_new_python(name)
            case 2:
                make_new_java(name)
            case 3:
                make_new_web(name)
            case 4:
                make_new_rust(name)

def make_repo(name: str = None, whitelist: str = '*'):
    '''
    create a git repo and a github repo
    :name: str, the name of the repo
    if name is none, no github repository is created
    '''
    system(f'git init &&\
        git add {whitelist} &&\
        git commit -mInitial')
    if name:
        system(f'gh repo create {name} --public &&\
            git remote add origin git@github.com:kermitpurple/{name} &&\
            git push --set-upstream origin main')

def make_new_c(name: str):
    '''
    Make a new project in c or c++
    :name: str, the name of the project
    '''
    path = override_path if override_path else os.path.join(CODING_PATH, 'c++')
    path = os.path.join(path, name)
    mkdir(path)
    chdir(path)
    system(f'cp -r {get_defaults_path("c++")} .')
    if g_repo:
        make_repo(name if gh_repo else None)
    system(f'{new_cmd} \'{path}\' \'vim makefile src/main.cpp -O\'')

def make_new_python(name: str):
    '''
    Make a new project in Python
    :name: str, the name of the project
    '''
    path = override_path if override_path else os.path.join(CODING_PATH, 'python')
    path = os.path.join(path, name)
    mkdir(path)
    chdir(path)
    system(f'cp -r {get_defaults_path("python")} .')
    if g_repo:
        make_repo(name if gh_repo else None)
    system(f'{new_cmd} \'{path}\' vim main.py')

def make_new_java(name: str):
    '''
    Make a new project in Java
    :name: str, the name of the project
    '''
    path = override_path if override_path else os.path.join(CODING_PATH, 'java')
    path = os.path.join(path, name)
    mkdir(path)
    chdir(path)
    system(f'cp -r {get_defaults_path("java")} .')
    if g_repo:
        make_repo(name if gh_repo else None)
    system(f'{new_cmd} \'{path}\' \'vim * -O\'')

def make_new_web(name: str):
    '''
    Make a new web project
    :name: str, the name of the project
    '''
    path = override_path if override_path else os.path.join(CODING_PATH, 'web')
    path = os.path.join(path, name)
    mkdir(path)
    chdir(path)
    if PlainJS:
        system(f'touch index.js')
    else:
        system(f'cp {get_defaults_path("web")} .')
    if g_repo:
        make_repo(name if gh_repo else None)
    system(f'{new_cmd} \'{path}\' \'vim * -O\'')

def make_new_rust(name: str):
    '''
    Make a new project in Rust
    :name: str, the name of the project
    '''
    path = override_path if override_path else os.path.join(CODING_PATH, 'rust')
    chdir(path);
    system(f'cargo new {name}')
    path = os.path.join(path, name)
    chdir(path)
    if g_repo:
        make_repo(name if gh_repo else None, 'src Cargo.toml')
    system(f'{new_cmd} \'{path}\' \'vim Cargo.toml src/main.rs -O\'')

def parse_argv():
    '''
    Parse the args of the program
    edit sys.argv
    '''
    global new_cmd, g_repo, gh_repo, argv, override_path
    parser = argparse.ArgumentParser(prog='new', description='creates a new project')
    parser.add_argument(
        'type',
        type=str,
        nargs='?',
        default=None,
        help='type of project i.e. c++|python|java|web|rust'
    )
    parser.add_argument(
        'name',
        type=str,
        nargs='?',
        default=None,
        help='name of the project, what the folder/repo will be named'
    )
    parser.add_argument(
        '-w',
        '--window',
        action='store_true',
        default=False,
        help='create new window instead of new tab'
    )
    parser.add_argument(
        '-g',
        '--git',
        action='store_true',
        default=False,
        help='create a git repository'
    )
    parser.add_argument(
        '-H',
        '--github',
        action='store_true',
        default=False,
        help='create a github repository'
    )
    parser.add_argument(
        '-p',
        '--path',
        type=str,
        default=None,
        help='Override path and write to'
    )
    args = parser.parse_args()
    if args.window:
        new_cmd = 'new_window'
    g_repo = args.git
    gh_repo = args.github
    if args.type is None:
        make_new()
        return
    elif args.name is None:
        name = get_name()
    else:
        name = args.name
    if args.path is not None:
        override_path = os.path.abspath(args.path)
    typ = args.type.lower()
    if typ in CPP_EXTS:
        make_new_c(name)
    elif typ in PYTHON_EXTS:
        make_new_python(name)
    elif typ in JAVA_EXTS:
        make_new_java(name)
    elif typ in WEB_EXTS:
        make_new_web(name)
    elif typ in RUST_EXTS:
        make_new_rust(name)
    else:
        eprint('ERROR: A project type with that name does not exist')
        exit(1)

def main():
    '''Driver Code'''
    parse_argv()

if (__name__ == '__main__'):
    main()
