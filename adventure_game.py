import time
import random


def print_pause(text_to_print):
    print(text_to_print)
    time.sleep(1)


def valid_input(prompt, option1, option2):
    while True:
        answer = input(prompt).lower()
        if option1 in answer:
            break
        elif option2 in answer:
            break
        else:
            print_pause("mayday, I don't understand")
    return answer


def intro():
    print_pause("Hello, your friend has been abducted by aliens.\n")
    print_pause("Nasa has created a rescue mission,\n")
    print_pause("Where you are going to the moon.\n")
    print_pause("But there are some risk.\n")
    print_pause("You can get lost in space.\n")
    print_pause("You will have the option to pick between two spacecrafts.\n")
    print_pause("Each Spacecrafts has everithing that you need.\n")
    print_pause("To your rigth is Orion.\n")
    print_pause("And to your left is Apollo.\n")


def takeoff():
    n = 3
    while n > 0:
        print(n, flush=True)
        time.sleep(1)
        n -= 1
    print("takeoff!", flush=True)


def scenario_1():
    print_pause("Something went wrong\n")
    print_pause("Now you are orbiting around the moon.\n")
    print_pause("Mission Failed\n")
    print_pause("GAME OVER\n")


def scenario_2():
    print_pause("You are in the rigth direction!\n")
    print_pause("Get Ready you are approching the moon.\n")
    print_pause("Mission Acomplished!.\n")
    print_pause("Heading back home!.\n")


def scenario_3():
    print_pause("Oh no! Something doesn't look good\n")
    print_pause("You are heading to a Black Hole.\n")
    print_pause("Your Mission has failed.\n")
    print_pause("GAME OVER!.\n")


scenarios = (scenario_1, scenario_2, scenario_3)


def spacecraft():
    while True:
        print_pause("Please enter the NAME "
                    "of the spacecraft that you would like to use\n")
        options = input('apollo\n\norion\n\n').lower()
        if "orion" in options:
            print_pause("Orion it is!\n")
            print_pause("Orion was built to take humans farther\n")
            takeoff()
            return random.choice(scenarios)()
        elif "apollo" in options:
            print_pause("Apollo it is!\n")
            print_pause("Apollo landed the first humans on the Moon\n")
            takeoff()
            return random.choice(scenarios)()
        else:
            print_pause("Sorry, I don't understand")


def play_again():
    response = valid_input("Would you like to play again?"
                           "Say 'yes' or 'no'", "yes", "no")
    while True:
        if "no" in response:
            print_pause("Ok!See you Next Time!")
            break
        if "yes" in response:
            print_pause("Excelent, restarting the game...")
            return game()
        else:
            print_pause("Sorry, I don't understand")


def game():
    intro()
    spacecraft()
    play_again()


game()
