import time
import os
import random


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_new_year():
    tree = [
        "*",
        "* *",
        "* * *",
        "* * * *",
        "* * * * *",
        "* * * * * *",
        "* * * * * * *",
        "* * * * * * * *",
        "* * *",
        "* * *"
    ]

    colors = [
        "\033[31m",  
        "\033[32m",  
        "\033[33m",  
        "\033[34m",  
        "\033[35m",  
        "\033[36m"  
    ]

    for line in tree:
        for char in line:
            if char == '*':
                color = random.choice(colors)
                print(color + char + "\033[0m", end="")
            else:
                print(" ", end="")
        print()  # перенос строки после строки ёлки


def main():
    while True:
        clear_console()
        print_new_year()
        time.sleep(0.5)


if __name__ == "__main__":
    main()
