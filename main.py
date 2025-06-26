import random
from classes import *
from combat import *
from characters import *


def main():
    selection = input("Choose your character: 1 = Gandalf, 2 = Cloud".center(70))
    while selection != "1" and selection != "2":
        print("Unrecognized selection. Please choose 1 for Gandalf or 2 for Cloud".center(70))
        selection = input("Choose your character: 1 = Gandalf, 2 = Cloud".center(70))
    if selection == "1":
        input("You've selected Gandalf. Hit enter to do battle.".center(70))
        print(border)
        combat(Gandalf, Cloud)
    elif selection == "2":
        input("You've selected Cloud. Hit enter to do battle.".center(70))
        print(border)
        combat(Cloud, Gandalf)


if __name__ == "__main__":
    main()