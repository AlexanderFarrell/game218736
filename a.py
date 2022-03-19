import random

name = input("Enter your name: ")
playing = True

while playing:
    i = input("What next?: ")
    if i == "move":
        pass
    elif i == 'say':
        print(f"{name}: {input('What would you like to say?: ')}")
    elif i == 'random':
        t = random.randint(1, 1990)
        p = random.randint(1, 1990)
        if t > p:
            print(f"{name}, you won!You got {t} and the computer got {p}!")
        else:
            print(f"Lost or tie.You got {t} and the computer got {p}.")
    elif i == "center":
        print("Fancy " + str(name.center(37, ".")))
    elif i == "quit":
        playing = False
    else: print("Invalid command")