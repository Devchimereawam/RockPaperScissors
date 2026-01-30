import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3 # Uppercase letter variables mean constant variables

# Creating a play-again loop
playagain = True

while playagain:
    # print(RPS(2))
    # print(RPS.ROCK)
    # print(RPS['ROCK'])
    # print(RPS.ROCK.value)
    # sys.exit()

    # Input 
    playerchoice = input("\nEnter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    # Choices for player
    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")

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

    playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\n🎉 🎉 🎉 🎉")
        print("Thank you for playing!\n")
        playagain = False

sys.exit("Bye! 👋")