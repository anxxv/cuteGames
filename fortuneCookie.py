import random
import os
import time

pink = "\033[95m"
blue = "\033[96m"
yellow = "\033[93m"
green = "\033[92m"
red = "\033[91m"
black = "\033[30m"
reset = "\033[0m"

fortunes = [
    "Your hug could fix someone’s broken heart today",
    "Stars are twinkling extra bright tonight just to make you smile",
    "A little fairy just whispered that you are loved more than you know",
    "Somewhere, a little heart is beating extra fast just thinking of you",
    "Somewhere, someone is smiling because you exist",
    "Sitting in silence with you - is all the noise I need",
    "Be careful who you trust! - Salt and sugar look the same.",
    "never dream about success - work for it."
]

cookieFrames = [
    "(っ˘ڡ˘ς)  🍪 ",
    "🍪  (っ˘ڡ˘ς)",
    "(っ˘ڡ˘ς)  🍪 ",
    "  🍪 (っ˘ڡ˘ς)"
]

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
def animeteCookie(times = 8):
    for i in range(times):
        clear()
        frame = cookieFrames[i % len(cookieFrames)]
        color = random.choice([pink, blue, yellow, green])
        print(color + "\n" + frame + reset)
        time.sleep(0.5)
        
def fortuneCookie():
    clear()
    print(pink + "\n🍪 pening the fortune cookie..." + reset)
    time.sleep(1)
    animeteCookie()
    fortune = random.choice(fortunes)
    print(blue + "\n Your fortune cookie says: " + reset)
    print(green + f" «{fortune}»\n" + reset)
    
def main():
    while True:
        fortuneCookie()
        again = input(blue + "\nOpen another cookie? (y/n): " + reset)
        
        if again != "y":
            print(pink + "\nThe fortune cookies are flying away… but they will always come back! 🍪✨" + reset)
            break
        
if __name__ == "__main__":
    main()

