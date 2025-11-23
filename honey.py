import os
import time
import random

# Цвета
yellow = "\033[93m"
green = "\033[92m"
pink = "\033[95m"
blue = "\033[96m"
reset = "\033[0m"

honey = 0  

bee_frames = [
    "🐝     ",
    "  🐝   ",
    "    🐝 ",
    "  🐝   "
]

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def animate_bee(times=8):
    for i in range(times):
        clear()
        frame = bee_frames[i % len(bee_frames)]
        color = random.choice([yellow, pink, blue, green])
        print(color + "\n     " + frame + reset)
        print(yellow + f"🍯 Honey collected: {honey}\n" + reset)
        print("Actions: [C] Collect honey  [F] Feed flower  [Q] Quit")
        time.sleep(0.3)

def collect_honey():
    global honey
    gained = random.randint(1, 5)
    honey += gained
    print(yellow + f"\nThe bees buzz happily and collected {gained} honey! 🍯" + reset)
    time.sleep(1.5)

def feed_flower():
    print(green + "\nYou watered the flowers 🌸. The bees are happy! 🐝" + reset)
    time.sleep(1.5)

def main():
    global honey
    clear()
    print(pink + "Welcome to the Cute Beehive! 🐝✨" + reset)
    time.sleep(1)

    while True:
        animate_bee(4)
        choice = input("\nYour action: ").lower().strip()
        if choice == "c":
            collect_honey()
        elif choice == "f":
            feed_flower()
        elif choice == "q":
            print(pink + "\nThe bees buzz goodbye! 🐝💛" + reset)
            break
        else:
            print("Invalid action, try again! (C, F, Q)")
            time.sleep(1)

if __name__ == "__main__":
    main()
