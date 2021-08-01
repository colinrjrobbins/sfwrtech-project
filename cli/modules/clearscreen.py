from os import system, name

def clear():
    """Strictly used to clear the terminal screen depending on the operating system."""
    if name == 'nt':
        system('cls')
    else:
        system('clear')