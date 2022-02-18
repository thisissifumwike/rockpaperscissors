import random

choices = ['rock', 'paper', 'scissor']

computer = random.choice(choices)

player = None
while player not in choices:
    player = input("Enter rock paper or scissor: ").lower()

if computer == player:
    print("Computer Chose: ", computer)
    print("Player Chose: ", player)
    print("Its a Tie!")

elif player == 'rock':
    if computer == 'paper':
        print("Computer Chose: ", computer)
        print("Player Chose: ", player)
        print("You lose!")
    elif computer == 'scissor':
        print("Computer Chose: ", computer)
        print("Player Chose: ", player)
        print("You win!")

elif player == 'paper':
    if computer == 'rock':
        print("Computer Chose: ", computer)
        print("Player Chose: ", player)
        print("You lose!")
    elif computer == 'scissor':
        print("Computer Chose: ", computer)
        print("Player Chose: ", player)
        print("You win!")

elif player == 'scissor':
    if computer == 'paper':
        print("Computer Chose: ", computer)
        print("Player Chose: ", player)
        print("You you lose!")
    elif computer == 'rock':
        print("Computer Chose: ", computer)
        print("Player Chose: ", player)
        print("You win!")
