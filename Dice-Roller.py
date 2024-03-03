import random

def print_dice(number):
    if number == 1:
        print(" ----- ")
        print("|     |")
        print("|  o  |")
        print("|     |")
        print(" ----- ")
    elif number == 2:
        print(" ----- ")
        print("| o   |")
        print("|     |")
        print("|   o |")
        print(" ----- ")
    elif number == 3:
        print(" ----- ")
        print("| o   |")
        print("|  o  |")
        print("|   o |")
        print(" ----- ")
    elif number == 4:
        print(" ----- ")
        print("| o o |")
        print("|     |")
        print("| o o |")
        print(" ----- ")
    elif number == 5:
        print(" ----- ")
        print("| o o |")
        print("|  o  |")
        print("| o o |")
        print(" ----- ")
    elif number == 6:
        print(" ----- ")
        print("| o o |")
        print("| o o |")
        print("| o o |")
        print(" ----- ")

while True:
    number = random.randint(1, 6)
    print_dice(number)
    
    x = input("Press 'y' to roll again and 'n' to exit: ")
    print("\n")
    
    if x.lower() != "y":
        break
