import random

def game(player , computer):
    if player == computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("It's a tie!")

    elif player == "rock":
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")
        else:
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose!")

    elif player == "paper":
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")
        else:
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose!")

    elif player == "scissors":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")
        else:
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose!")


choices = ["rock","paper","scissors"]

while True:
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, scissors?: ").lower()

    game(player, computer)

    replay = input("\n"+"Play again? (y/n): ").lower()
    if replay != "y":
        break
print("Thanks for playing. Goodbye!")






