
def character_select():
    selection = input("Choose your character: 1 = Gandalf, 2 = Cloud\n")
    while selection != "1" and selection != "2":
        print("Unrecognized selection. Please choose 1 for Gandalf or 2 for Cloud\n")
        selection = input("Choose your character: 1 = Gandalf, 2 = Cloud\n")
    if selection == "1":
        print("You've selected Gandalf.")
        input("Hit enter to continue")
        return "Gandalf"
    elif selection == "2":
        print("You've selected Cloud")
        input("Hit enter to continue")
        return "Cloud"



