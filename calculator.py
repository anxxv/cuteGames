import time
import os

PINK = "\033[95m"
BLUE = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def cute_intro():
    clear()
    print(PINK + "✧･ﾟ: *✧･ﾟ:*  CUTE CALCULATOR  *:･ﾟ✧*:･ﾟ✧" + RESET)
    print(BLUE + "(⌒‿⌒) 💖 Добро пожаловать!" + RESET)
    time.sleep(1)

def cute_menu():
    print(YELLOW + "\nВыбери операцию, милота ✨" + RESET)
    print(GREEN + "1 ➜ Сложение (⁄ ⁄>⁄ ▽ ⁄<⁄ ⁄)" + RESET)
    print(GREEN + "2 ➜ Вычитание (｡•́︿•̀｡)" + RESET)
    print(GREEN + "3 ➜ Умножение ✧(>o<)ﾉ✧" + RESET)
    print(GREEN + "4 ➜ Деление (•̀ᴗ•́)و ̑̑" + RESET)
    print(GREEN + "5 ➜ Выход (˘• ₃ •˘)" + RESET)

def get_number(order):
    return float(input(PINK + f"\nВведите {order} число: " + RESET))

def calculate():
    while True:
        clear()
        cute_intro()
        cute_menu()

        choice = input(BLUE + "\nВаш выбор ➜ " + RESET)

        if choice == "5":
            print(PINK + "\nСпасибо, что пользовался мной! (｡•́‿•̀｡)♡\n" + RESET)
            break

        if choice not in ("1", "2", "3", "4"):
            print(YELLOW + "Ой! Это не то! Попробуй снова ☺️" + RESET)
            time.sleep(1.2)
            continue

        a = get_number("первое")
        b = get_number("второе")

        clear()
        print(PINK + "\nРезультат готов! ✨" + RESET)

        if choice == "1":
            print(GREEN + f"{a} + {b} = {a + b}  (≧◡≦)" + RESET)
        elif choice == "2":
            print(GREEN + f"{a} - {b} = {a - b}  (•︵•)" + RESET)
        elif choice == "3":
            print(GREEN + f"{a} × {b} = {a * b}  ✧٩(ˊᗜˋ*)و✧" + RESET)
        elif choice == "4":
            if b == 0:
                print(YELLOW + "Ай! Деление на ноль нельзя (╥﹏╥)" + RESET)
            else:
                print(GREEN + f"{a} ÷ {b} = {a / b}  (•̀ᴗ•́)و" + RESET)

        input(BLUE + "\nНажми Enter, чтобы продолжить..." + RESET)

if __name__ == "__main__":
    calculate()
