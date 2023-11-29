
import random

def play_round(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
        return "Player wins!"
    else:
        return "Computer wins!"

def get_player_choice():
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ")
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def play_game():
    player_score = 0
    computer_score = 0
    rounds = 3

    for _ in range(rounds):
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print(f"Player chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        result = play_round(player_choice, computer_choice)
        print(result)

        if result == "Player wins!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1

    print("Game over!")
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")

play_game()
