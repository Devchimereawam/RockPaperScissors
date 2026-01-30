import sys
import random
from enum import Enum

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3 # Uppercase letter variables mean constant variables

    # Creating a play-again loop

    # print(RPS(2))
    # print(RPS.ROCK)
    # print(RPS['ROCK'])
    # print(RPS.ROCK.value)
    # sys.exit()

    # Input 
    playerchoice = input("\nEnter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()

    # Choices for player
    player = int(playerchoice)

    # Computer uses random choices
    computerchoice = random.choice("123")

    computer = int(computerchoice)

    # Prints your choice and the computers choice
    print("\nYou chose " + str(RPS(player)).replace('RPS.','') + ".")
    print("Computer chose " + str(RPS(computer)).replace('RPS.','') + ".\n")

    # Winning or losing logic implemented
    if player == 1 and computer == 3:
        print("🎉 You win!")
    elif player == 2 and computer == 1:
        print("🎉 You win!")
    elif player == 3 and computer == 2:
        print("🎉 You win!")
    elif player == computer:
        print("😮‍💨 Tie game!")
    else:
        print("🐍 Python wins!")

    print("\nPlay again?")

    while True:
        playagain = input("\nY for Yes or \nQ to Quit \n\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n🎉 🎉 🎉 🎉")
        print("Thank you for playing!\n")
        playagain = False
        sys.exit("Bye! 👋")

play_rps()