import random

choices = ["Paper", "Rock", "Scissor"]

player1 = 0
player2 = 0

while player1 or player2 < 3:
    first_user = input("Rock, Paper, Scissor: ").capitalize()
    second_user = random.choice(choices)
    print(second_user)
    if first_user == "Rock" and second_user == "Scissor":
        print("Player 1 gets a point!")
        player1 += 1
        print(player1)
    elif first_user == "Rock" and second_user == "Paper":
        print("player 2 gets a point!")
        player2 += 1
        print(player2)
    elif first_user == "Paper" and second_user == "Scissor":
        print("player 2 gets a point!")
        player2 += 1
        print(player2)
    elif first_user == "Paper" and second_user == "Rock":
        print("Player 1 gets a point!")
        player1 += 1
        print(player1)
    elif first_user == "Scissor" and second_user == "Rock":
        print("Player 2 gets a point!")
        player2 += 1
        print(player2)
    elif first_user == "Scissor" and second_user == "Paper":
        print("Player 1 gets a point!")
        player1 += 1
        print(player1)
    elif first_user == second_user:
        print("It is a tie!")
    else:
        print("Sorry! You didn't type any of the given options.")
    if player1 >= 3:
        print("Player 1 wins!")
        break
    if player2 >= 3:
        print("Bot wins!")
        break
