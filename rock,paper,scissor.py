import random

while True:
    choices = ["rock", "paper", "scissor"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissor?: ").lower()

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("you lose!")
        if computer == "scissor":
            print("computer: ", computer)
            print("player: ", player)
            print("you win!")
    elif player == "paper":
        if computer == "scissor":
            print("computer: ", computer)
            print("player: ", player)
            print("you lose!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("you win!")
    elif player == "scissor":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("you lose!")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("you win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again == "no":
        break
    elif play_again == "yes":
        continue
    else:
        print("Uh-oh something went wrong! Try again!")

print("Buh-Byeee!")
