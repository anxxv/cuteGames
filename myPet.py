import time
import os
import random

pink = "\033[95m"
blue = "\033[96m"
yellow = "\033[93m"
green = "\033[92m"
red = "\033[91m"
black = "\033[30m"
reset = "\033[0m"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50

    def show(self):
        clear()
        print(pink + f"\nВаш питомец: {self.name} (◕‿◕✿)" + reset)

        # Выбор мордочки
        if self.happiness > 70:
            face = black + "(◕‿◕✿)"
        elif self.happiness > 40:
            face = pink + "(◕‿◕)"
        else:
            face = blue + "(◕︿◕)"

        print(blue + f"\n     {face}\n" + reset)

        print(green + f"💖 Счастье: {self.happiness}" + reset)
        print(yellow + f"🍰 Сытость: {self.hunger}" + reset)
        print(blue + f"💤 Энергия: {self.energy}\n" + reset)

    def feed(self):
        self.hunger = min(100, self.hunger + random.randint(10, 25))
        print(green + f"\n{self.name} вкусно кушает! (っ˘ڡ˘ς) 🍰 " + reset)
        time.sleep(1.5)

    def play(self):
        if self.energy < 20:
            print(red + f"{self.name} слишком устал, чтобы играть… (҂◡_◡)" + reset)
            time.sleep(1.5)
            return

        self.happiness = min(100, self.happiness + random.randint(10, 25))
        self.energy = max(0, self.energy - random.randint(5, 15))

        print(pink + f"\n{self.name} играет и веселится! (◕ᴗ◕✿) 💖" + reset)
        time.sleep(1.5)

    def sleep(self):
        self.energy = min(100, self.energy + random.randint(20, 35))
        self.hunger = max(0, self.hunger - random.randint(5, 15))

        print(blue + f"\n{self.name} сладко спит… (≖‿≖✿) 💤" + reset)
        time.sleep(2)

    def tick(self):
        self.hunger = max(0, self.hunger - 2)
        self.happiness = max(0, self.happiness - 1)
        self.energy = max(0, self.energy - 1)

    def isAlive(self):
        return self.hunger > 0 and self.happiness > 0 and self.energy > 0


def main():
    clear()
    name = input(pink + "Как назовём питомца? ✨ " + reset)
    pet = Pet(name)

    while True:
        pet.show()

        if not pet.isAlive():
            print(red + f"\n{pet.name} умер... (╥﹏╥)" + reset)
            break

        print(yellow + "Выберите действие:" + reset)
        print("1 — 🍰 Покормить")
        print("2 — 🎲 Поиграть")
        print("3 - 💤 Уложить спать")
        print("4 - 💔 Убить питомца")
        
        choice = input(blue + "\nВаш выбор: " + reset)
        
        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.sleep()
        elif choice == "4":
            print(pink + f"\n{pet.name} помахал вам лапкой на последок...(╥﹏╥)" + reset)
            break 
        else:
            print(red + "\nТакой команды нет (｡•́︿•̀｡)" + reset)
            time.sleep(1)
            
        pet.tick()
        
if __name__ == "__main__":
    main()
