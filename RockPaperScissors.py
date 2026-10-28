#Rock Paper Scissors Game

import random

options = ["rock", "paper", "scissors"]


playing = True

while playing is True:

    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Player choose rock, paper, or scissors: ")

    print(f"Player: {player}")
    print(f"Computer:{computer}")

    if player == computer:
        print(f"It's a tie")
    elif player =="rock" and computer == "scissors":
        print("You win")
    elif player =="paper" and computer == "rock":
        print("You win")
    elif player =="scissors" and computer == "paper":
        print("You win")
    else:
        print("You lose")

    play_again = input("Do you want to play again? (y/n): ").lower()

    if not play_again == "y":
        playing = False

        # if not input("Do you want to play again? (y/n): ").lower() == "y":
        #     playing =False

print(f"Thanks for playing")






