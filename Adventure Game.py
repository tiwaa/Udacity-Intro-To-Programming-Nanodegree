import time
import random

nouns = ["giant panda", "wicked witch", "big bad wolf", "lioness"]
n = random.choice(nouns)
items = ["magic wand", "spear",
         "mysterious bow and arrows"]
i = random.choice(items)


def print_pause(message_to_print):
    print(message_to_print, flush=True)
    time.sleep(2)


def enter_1_or_2():
    print_pause("Enter 1 to knock on "
                "the door of the tower.")
    print_pause("Enter 2 to walk through the dark tunnel.")


def good_bye():
    print_pause("Thanks for playing! See you next time.")


def intro():
    print_pause("You find yourself in the outskirts of a village,"
                "with trees and bushes all around you.")
    print_pause(f"According to hearsay, there's a {n} "
                "around here,\nof which the whole village "
                "is afraid of.")


def run_away():
    print_pause("You run back into the bushes. "
                f"Luckily, the {n} couldn't"
                " follow you\n")


def fight_without_weapon():
    while True:
        response = input("Would you like to (1) fight"
                         " or (2) run away?\n")
        if response == '1':
            print_pause("You fight bravely...")
            print_pause("but your knife is just too small"
                        f" for the {n}")
            print_pause("You have been killed!\n")
            break
        elif response == '2':
            run_away()
            break
        else:
            print_pause("Invalid input. Please "
                        "try again!")


def tower():
    print_pause("You move closer to the door of the tower.")
    print_pause("And just as you begin to knock, the "
                f"door swangs open and out steps a {n}.")
    print_pause(f"Whao! This is the {n}'s tower!")
    print_pause(f"The {n} moves forward to attack you!\n")
    print_pause("You begin to sweat profusely, fight with"
                " only a small knife?")
    fight_without_weapon()


def tunnel():
    print_pause("You walk cautiously through the tunnel.")
    print_pause("You find out its quite a long one.")
    print_pause("As you passage through the dark tunnel"
                f"with your lamp, you come across a {i} ")
    print_pause("You drop your small knife and "
                f"take the {i} with you")
    print_pause("You run back into the bushes.\n")


def select_path():
    while True:
        print_pause("Behind you is a tower.")
        print_pause("Infront of you is a dark tunnel.")
        print_pause("In your hand you hold your "
                    "small knife\n")
        enter_1_or_2()
        choice = input("What would you like to do?\n"
                       "(Please enter 1 or 2).\n")
        if choice == '1':
            tower()
            break
        elif choice == '2':
            tunnel()
            break
        else:
            print_pause("Invalid input. Please "
                        "try again!")


def ran_away_play():
    run_away()
    select_path()


def victory():
    print_pause("You move closer to the door of the tower.")
    print_pause("And just as you begin to knock, the "
                f"door swangs open and out steps a {n}.")
    print_pause(f"Whao! This is the {n}'s tower!")
    print_pause(f"The {n} moves forward to attack you!\n")
    print_pause(f"As the {n} moves closer to you, "
                f"you bring out the {i}.")
    print_pause(f"The {i} glows in your hand "
                "as you brace yourself for the attack.")
    print_pause(f"But the {n} take a glance at your weapon "
                "and vanishes into thin air!")
    print_pause(f"Bravo! You have rid the entire"
                f" village of a {n}. "
                "Yaay!\n Congratulations!\n")


def fight_with_weapon():
    while True:
        enter_1_or_2()
        with_weapon = input("Please enter 1 or 2: ")
        if with_weapon == '1':
            victory()
            break
        elif with_weapon == '2':
            tunnel()
            break
        else:
            print_pause("Invalid input! Please try again.")


def play_again():
    while True:
        print_pause("Alright, game is restarting...")
        intro()
        select_path()
        break


def welcome():
    print_pause("Hello! And welcome to the world"
                " of ADVENTURE!")
    print_pause("Please select one:")
    print_pause("1. are you a first-timer?")
    print_pause("2. or just came out of the "
                "tunnel?")
    print_pause("3. or just ran away from"
                " the enemy?")
    print_pause("4. or would like to play "
                "this game again?")
    print_pause("5. or would like to exit"
                " this game\n")


def game():
    while True:
        welcome()
        play = input("Please make a choice: ")
        if play == '1':
            intro()
            select_path()
        elif play == '2':
            print_pause("Great! You have your "
                        "weapon now.")
            fight_with_weapon()
        elif play == '3':
            ran_away_play()
        elif play == '4':
            play_again()
        elif play == '5':
            print_pause("Thanks! Goodbye!")
            break
        else:
            print_pause("Invalid input! Please try again.")


game()
