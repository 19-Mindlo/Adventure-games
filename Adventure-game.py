import time
import random


def print_pause(message, delay=0):
    print(message)
    time.sleep(delay)


def valid_input(prompt, choice):
    while True:
        response = input(prompt)
        if response in choice:
            return response
        else:
            print_pause(f"\nSorry {response} is invalid. Try again!")


def intro(villain):
    print_pause("\nYou are a private agent and has been sent"
                " on a mission to retrieve"
                " an encrypted document")
    print_pause("\nThe document contains an important information"
                " on vaccine for an outbreak.", 2)
    print_pause("\nRumor has it a vampire is guarding the house.", 2)
    print_pause("\nIn front of you is a house.", 2)
    print_pause("\nTo your right is a dark Cave", 2)
    print_pause("\nTo your hand you hold your trusty"
                " but no very effective) sword", 2)
    print_pause("\nEnter 1 to knock on the door of the house")
    print_pause("\nEnter 2 to peer into a Cave", 2)
    print_pause("\nWhat you would like to do ?")
    response = valid_input("\n(Please enter 1 or 2)\n\n", ['1', '2'])
    if response == '1':
        house(villain)
    elif response == '2':
        cave(villain)


def house(villain):
    print_pause("\nYou approach the door of the house.", 2)
    print_pause(f"\nYou are about to knock when you realise a {villain} "
                "\nis guarding the house.", 2)
    response = valid_input("\nWould you like to enter the front or back door"
                           "\nEnter 'back' or 'front'\n\n",
                           ['back', 'front']).lower()
    if 'front' in response:
        print_pause(f"\nYou do your best to fight the {villain} attacking you",
                    2)
        print_pause("\nYou realise the sword is not going to help", 2)
        print_pause(f"\nUnfortunately the {villain} is very fast", 2)
        print_pause("\nYou lost game....", 2)
        play_again()
    elif 'back' in response:
        print_pause("\nYou realise the back is unguarded ...", 2)
        print_pause("\nYou proceed to enter the house and"
                    "aquire the document", 2)
        print_pause("\nTo your surprise, you see"
                    " white Oak Ash dagger on the safe", 2)
        print_pause(f"\nYou get dagger before the {villain} attacks", 2)
        print_pause(f"\nAnd overpower the {villain} just before"
                    " the attacsk", 2)
        print_pause("\nWould like to comtinue with your mision ?")
        answer = valid_input("\nPlease enter 'yes' or 'no'\n\n",
                             ['yes', 'no']).lower()
        if 'yes' in answer:
            mission(villain)
        elif 'no' in answer:
            print_pause("\nMision not completed...", 2)
            print_pause("\nThank you for playing", 2)


def cave(villain):
    print_pause("\nUp ahead in the cave there's a bridge-border"
                " that is heavily guraded by...")
    print_pause(f"\n{villain} to search anyone who passes through.", 2)
    print_pause("\nYou need to proceed to the bridge and recieve"
                " further instruction.", 2)
    print_pause("\nWhat you like to do ?")
    response2 = valid_input("\nPleae enter 'proceed' or 'turn'\n\n",
                            ['proceed', 'turn']).lower()
    if 'proceed' in response2:
        print_pause("\nYou take out a sniper", 2)
        print_pause("\nand find a nice quiet spot", 2)
        print_pause("\nyou proceed to broder-bridge and"
                    " recieve your mission", 2)
        print_pause("\nWould you like continue mission", 2)
        response3 = valid_input("\nPlease enter 'yes' or 'no'\n\n",
                                ['yes', 'no']).lower()
        if response3 == 'yes':
            mission(villain)
        elif response3 == 'no':
            print_pause("\nMission not complete, 2")
            print_pause("\nExiting the game...", 2)

    elif 'turn' in response2:
        print_pause("\nMission not complete", 2)
        print_pause("\nExiting the game...", 2)


def mission(villain):
    print_pause("\nYour task is to continue to the field-lab"
                " and retieve an encrypted document", 2)
    print_pause(f"\nThe field is heavily guarded by a herd of {villain}", 2)
    print_pause("\nIn front of you is a sniper with limited ammo", 2)
    print_pause("\nAnd dagger (very lethal white Oak Ash dagger)", 2)
    decision = valid_input("\nPlease pick your weapon?\n\n",
                           ['sniper', 'dagger']).lower()
    if decision == 'sniper':
        print_pause("\nYou run towards the field-labs and")
        print_pause(f"\ntry to shoot at couple of {villain}", 2)
        print_pause("\nUnfortunately you are running out of ammo", 2)
        print_pause(f"\n{villain} overwhelm you", 2)
        print_pause("\nYou have lost the game", 2)
        play_again()
    elif decision == 'dagger':
        print_pause(f"\nYou head straight to the {villain} guards of"
                    " the lab-field", 2)
        print_pause("\nThe powerful sword of Orgorth crafted in"
                    " uranium shines in your hands", 2)
        print_pause(f"\nCutting through every {villain} in your path")
        print_pause("\nYou retrieve the encypted document and head"
                    " straight to the helicopter", 2)
        print_pause("\nCongratulations!!!!", 2)
        print_pause("\nYou have won the game", 2)


def play_again():
    play = valid_input("\nwould you like to play again ? (y/n)\n\n",
                       ['y', 'n']).lower()
    if 'n' in play:
        print_pause("\nThank you for playing")
        print_pause("\nGoodbye!")
    elif 'y' in play:
        print_pause("\nRestarting the game.........", 2)
        main()


def main():

    villain = random.choice(["Vampires", "Wolfs", "Witches"])
    intro(villain)


main()
