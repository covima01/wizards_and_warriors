import random
from classes import *
from combat import *
from characters import *


def main():
    selection = input("Choose your character: 1 = Gandalf, 2 = Cloud\n")
    while selection != "1" and selection != "2":
        print("Unrecognized selection. Please choose 1 for Gandalf or 2 for Cloud\n")
        selection = input("Choose your character: 1 = Gandalf, 2 = Cloud\n")
    if selection == "1":
        input("\nYou've selected Gandalf. Hit enter to do battle. ")
        print("======================================================================\n")
        combat(Gandalf, Cloud)

    elif selection == "2":
        input("\nYou've selected Cloud. Hit enter to do battle.\n")
        print("======================================================================\n")
        combat(Cloud, Gandalf)


if __name__ == "__main__":
    main()